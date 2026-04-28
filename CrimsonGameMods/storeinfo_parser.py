"""storeinfo.pabgb / .pabgh parser for Crimson Desert v1.04.02+.

Layout discovered from live 4-24-26 game build (see _store_probe*.py):

  pabgh:
    u16 store_count
    repeat: u16 store_key, u32 body_offset

  pabgb (per store, addressed by header):
    u16 store_key
    u32 name_len, name[name_len]
    Header overhead (51 bytes) - format_tag at +0x1A is 0x09 0xFD on standard
        family stores. item_count u32 at +0x26, item_count_2 u32 at +0x2F.
    Items: variable-length walk
    Tail: 17 bytes (TAIL_SIZE_STD)

  Per-item entry layout (110-byte default, 123-byte trade variant):
    +0x00 u16 store_key_ref   (== owning store's key)
    +0x02 u64 buy_price
    +0x0A u64 sell_price
    +0x12 u32 purchase_limit
    +0x16 u32 field_1
    +0x1A u32 field_2
    +0x1E u8  pre_marker_a   (do NOT use for size; not stable)
    +0x1F u8  pre_marker_b
    +0x20 u16 marker          (== 0x0101)
    +0x22 u32 item_key
    +0x26 .. +0x60   item_data block (53+4 bytes; 4 bytes wider than old layout)
    +0x5F u16 separator       (== 0xFFFF)
    +0x61 u32 item_key_dup    (must == item_key)
    +0x65 u32 tail_field_a
    +0x69 u8  ext_flag         <-- DISCRIMINATOR: 0 -> entry size 110, 1 -> 123
    if ext_flag == 1:
       +0x6A .. +0x76   12-byte trailing block (likely game-event/trade meta)

We only edit fields the player UI exposes:

    buy_price (+0x02 u64)
    sell_price (+0x0A u64)
    purchase_limit (+0x12 u32)
    item_key (+0x22 u32) and item_key_dup (+0x61 u32) - kept in lock-step

The 53/57-byte item_data block is NEVER touched. This is what previous
attempts corrupted (writing dup at the OLD +0x5D offset clobbered bytes
inside item_data, which is what produced the "items become unsellable"
regression).

Stores are classified into four kinds:
    "standard": format_tag 0x09 0xFD AND item_count == item_count_2 > 0
    "empty":    format_tag 0x09 0xFD AND item_count == item_count_2 == 0
    "trade":    format_tag 0x09 0xFD but item_count != item_count_2
                (variable-length entries; not editable here)
    "special":  any other format_tag (Camp/Church/StreetVendor/BlackMarket etc.)
"""

from __future__ import annotations

import logging
import struct
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

log = logging.getLogger(__name__)

# Layout constants (do not change without re-verifying with _store_probe*.py)
HEADER_OVERHEAD = 51
TAIL_SIZE_STD = 17
TAIL_SIZE_SHORT = 15
ENTRY_SIZE_BASE = 110
ENTRY_SIZE_EXT = 123

OFF_BUY = 0x02
OFF_SELL = 0x0A
OFF_LIMIT = 0x12
OFF_MARKER = 0x20
OFF_ITEM_KEY = 0x22
OFF_ITEM_DUP = 0x61
OFF_EXT_FLAG = 0x69
MARKER = 0x0101

OFF_FORMAT_TAG = 0x1A
OFF_ITEM_COUNT = 0x26
OFF_ITEM_COUNT_2 = 0x2F


@dataclass
class StoreItemEntry:
    """One item slot in a store. ``offset`` is absolute into pabgb body."""

    offset: int
    size: int
    store_key_ref: int
    buy_price: int
    sell_price: int
    purchase_limit: int
    item_key: int
    item_key_dup: int
    raw: bytes


@dataclass
class StoreRecord:
    index: int
    key: int
    name: str
    offset: int           # absolute byte offset of u16 store_key in pabgb body
    size: int             # full record size including name+header+items+tail
    after_name: int       # absolute offset where header overhead begins
    format_tag: int       # u16 read from after_name + 0x1A
    kind: str             # "standard" | "empty" | "trade" | "special"
    item_count: int
    item_count_2: int
    items: List[StoreItemEntry] = field(default_factory=list)
    tail_size: int = TAIL_SIZE_STD
    # Compat fields used by some existing callers/diagnostics.
    name_offset: int = 0
    header_raw: bytes = b""
    tail_raw: bytes = b""

    @property
    def is_standard(self) -> bool:
        """Backwards-compatible flag used by older callers/UI code."""
        return self.kind in ("standard", "empty")

    @property
    def is_editable(self) -> bool:
        return self.kind == "standard"


class StoreinfoParser:
    """Reads, edits, and re-emits storeinfo.pabgh + storeinfo.pabgb."""

    def __init__(self):
        self.stores: List[StoreRecord] = []
        self._header_data: bytes = b""
        self._body_data: bytearray = bytearray()
        self._header_entries: List[Tuple[int, int]] = []
        self._name_lookup: Dict[int, str] = {}
        self._loaded = False

    # ----- loaders ----------------------------------------------------------

    def load_from_files(self, pabgh_path: str, pabgb_path: str) -> bool:
        try:
            with open(pabgh_path, "rb") as f:
                self._header_data = f.read()
            with open(pabgb_path, "rb") as f:
                self._body_data = bytearray(f.read())
            self._parse_header()
            self._parse_all_stores()
            self._loaded = True
            return True
        except Exception as exc:
            log.error("Failed to load storeinfo: %s", exc)
            return False

    def load_from_bytes(self, header_bytes: bytes, body_bytes: bytes) -> bool:
        self._header_data = header_bytes
        self._body_data = bytearray(body_bytes)
        self._parse_header()
        self._parse_all_stores()
        self._loaded = True
        return True

    def load_names(self, names_path: str = "") -> None:
        try:
            from data_db import get_connection
        except Exception:  # pragma: no cover - data_db is part of the repo
            return
        try:
            db = get_connection()
            for row in db.execute("SELECT item_key, name FROM items"):
                self._name_lookup[row["item_key"]] = row["name"]
        except Exception as exc:
            log.warning("load_names failed: %s", exc)

    def get_item_name(self, key: int) -> str:
        return self._name_lookup.get(key, f"Unknown({key})")

    # ----- header -----------------------------------------------------------

    def _parse_header(self) -> None:
        count = struct.unpack_from("<H", self._header_data, 0)[0]
        self._header_entries = []
        for i in range(count):
            base = 2 + i * 6
            key = struct.unpack_from("<H", self._header_data, base)[0]
            off = struct.unpack_from("<I", self._header_data, base + 2)[0]
            self._header_entries.append((key, off))

    # ----- body -------------------------------------------------------------

    def _classify(self, body: bytes) -> Tuple[str, int, int, int]:
        """Return (kind, item_count, item_count_2, tail_size_guess)."""
        if len(body) < HEADER_OVERHEAD + TAIL_SIZE_SHORT:
            return ("special", 0, 0, 0)
        fmt_a = body[OFF_FORMAT_TAG]
        fmt_b = body[OFF_FORMAT_TAG + 1]
        if fmt_a != 0x09 or fmt_b != 0xFD:
            return ("special", 0, 0, 0)
        cnt = struct.unpack_from("<I", body, OFF_ITEM_COUNT)[0]
        cnt2 = struct.unpack_from("<I", body, OFF_ITEM_COUNT_2)[0]
        if cnt2 == 0 and cnt == 0:
            tail_left = len(body) - HEADER_OVERHEAD
            tail = TAIL_SIZE_STD if tail_left == TAIL_SIZE_STD else TAIL_SIZE_SHORT
            return ("empty", 0, 0, tail)
        if cnt != cnt2 or cnt2 > 1000:
            return ("trade", cnt, cnt2, 0)
        return ("standard", cnt, cnt2, TAIL_SIZE_STD)

    def _parse_all_stores(self) -> None:
        self.stores.clear()
        data = self._body_data
        n = len(self._header_entries)

        for idx, (skey, soff) in enumerate(self._header_entries):
            if idx + 1 < n:
                rec_size = self._header_entries[idx + 1][1] - soff
            else:
                rec_size = len(data) - soff
            if soff + 6 > len(data):
                continue
            name_len = struct.unpack_from("<I", data, soff + 2)[0]
            name = data[soff + 6:soff + 6 + name_len].decode(
                "ascii", errors="replace"
            )
            after_name = soff + 6 + name_len
            body = bytes(data[after_name:soff + rec_size])

            kind, cnt, cnt2, tail_size = self._classify(body)
            fmt_tag = (
                struct.unpack_from("<H", body, OFF_FORMAT_TAG)[0]
                if len(body) >= OFF_FORMAT_TAG + 2
                else 0
            )

            store = StoreRecord(
                index=idx,
                key=skey,
                name=name,
                offset=soff,
                size=rec_size,
                name_offset=soff + 2,
                after_name=after_name,
                format_tag=fmt_tag,
                kind=kind,
                item_count=cnt,
                item_count_2=cnt2,
                tail_size=tail_size or TAIL_SIZE_STD,
            )

            if kind == "standard":
                self._parse_standard_items(store, body)
            self.stores.append(store)

    def _parse_standard_items(self, store: StoreRecord, body: bytes) -> None:
        p = HEADER_OVERHEAD
        body_len = len(body)
        for _ in range(store.item_count_2):
            if p + ENTRY_SIZE_BASE > body_len:
                log.warning(
                    "Store %s truncated at entry %d (p=%d body=%d)",
                    store.name, len(store.items), p, body_len,
                )
                store.kind = "trade"
                store.items.clear()
                return
            marker = struct.unpack_from("<H", body, p + OFF_MARKER)[0]
            if marker != MARKER:
                log.warning(
                    "Store %s bad marker at entry %d (got 0x%04X)",
                    store.name, len(store.items), marker,
                )
                store.kind = "trade"
                store.items.clear()
                return
            item_key = struct.unpack_from("<I", body, p + OFF_ITEM_KEY)[0]
            item_dup = struct.unpack_from("<I", body, p + OFF_ITEM_DUP)[0]
            if item_key != item_dup:
                log.warning(
                    "Store %s entry %d dup mismatch (key=%d dup=%d)",
                    store.name, len(store.items), item_key, item_dup,
                )
                store.kind = "trade"
                store.items.clear()
                return
            ext_flag = body[p + OFF_EXT_FLAG]
            size = ENTRY_SIZE_EXT if ext_flag == 1 else ENTRY_SIZE_BASE
            entry_body = body[p:p + size]
            store.items.append(StoreItemEntry(
                offset=store.after_name + p,
                size=size,
                store_key_ref=struct.unpack_from("<H", entry_body, 0)[0],
                buy_price=struct.unpack_from("<Q", entry_body, OFF_BUY)[0],
                sell_price=struct.unpack_from("<Q", entry_body, OFF_SELL)[0],
                purchase_limit=struct.unpack_from("<I", entry_body, OFF_LIMIT)[0],
                item_key=item_key,
                item_key_dup=item_dup,
                raw=bytes(entry_body),
            ))
            p += size

        # Remaining bytes are the tail.
        tail_left = body_len - p
        if tail_left in (TAIL_SIZE_STD, TAIL_SIZE_SHORT):
            store.tail_size = tail_left
        else:
            log.warning(
                "Store %s unexpected tail %d after %d items",
                store.name, tail_left, len(store.items),
            )

    # ----- editing ----------------------------------------------------------

    def get_store_by_key(self, key: int) -> Optional[StoreRecord]:
        return next((s for s in self.stores if s.key == key), None)

    def _find_item(self, store_key: int, item_key: int) -> Optional[Tuple[StoreRecord, StoreItemEntry]]:
        for store in self.stores:
            if store.key != store_key or not store.is_editable:
                continue
            for item in store.items:
                if item.item_key == item_key:
                    return store, item
        return None

    def set_buy_price(self, store_key: int, item_key: int, price: int) -> bool:
        hit = self._find_item(store_key, item_key)
        if not hit:
            return False
        _store, item = hit
        struct.pack_into("<Q", self._body_data, item.offset + OFF_BUY, int(price))
        item.buy_price = int(price)
        return True

    def set_sell_price(self, store_key: int, item_key: int, price: int) -> bool:
        hit = self._find_item(store_key, item_key)
        if not hit:
            return False
        _store, item = hit
        struct.pack_into("<Q", self._body_data, item.offset + OFF_SELL, int(price))
        item.sell_price = int(price)
        return True

    def set_purchase_limit(self, store_key: int, item_key: int, limit: int) -> bool:
        hit = self._find_item(store_key, item_key)
        if not hit:
            return False
        _store, item = hit
        struct.pack_into(
            "<I", self._body_data, item.offset + OFF_LIMIT, int(limit) & 0xFFFFFFFF
        )
        item.purchase_limit = int(limit)
        return True

    def swap_item(self, store_key: int, old_item_key: int, new_item_key: int) -> bool:
        hit = self._find_item(store_key, old_item_key)
        if not hit:
            log.warning("swap_item: not found store=%d old=%d", store_key, old_item_key)
            return False
        _store, item = hit
        struct.pack_into(
            "<I", self._body_data, item.offset + OFF_ITEM_KEY, int(new_item_key)
        )
        struct.pack_into(
            "<I", self._body_data, item.offset + OFF_ITEM_DUP, int(new_item_key)
        )
        item.item_key = int(new_item_key)
        item.item_key_dup = int(new_item_key)
        log.info(
            "Swapped %d -> %d in store %d", old_item_key, new_item_key, store_key
        )
        return True

    # ----- output -----------------------------------------------------------

    def get_header_bytes(self) -> bytes:
        return self._header_data

    def get_body_bytes(self) -> bytes:
        return bytes(self._body_data)

    def get_summary(self) -> str:
        std = sum(1 for s in self.stores if s.kind == "standard")
        empty = sum(1 for s in self.stores if s.kind == "empty")
        trade = sum(1 for s in self.stores if s.kind == "trade")
        special = sum(1 for s in self.stores if s.kind == "special")
        total_items = sum(len(s.items) for s in self.stores)
        return (
            f"{len(self.stores)} stores ({std} standard, {empty} empty, "
            f"{trade} trade, {special} special), {total_items} editable items, "
            f"body={len(self._body_data):,} bytes"
        )

    def validate(self) -> List[str]:
        issues: List[str] = []
        for store in self.stores:
            if not store.is_editable:
                continue
            for item in store.items:
                if item.item_key != item.item_key_dup:
                    issues.append(
                        f"{store.name}: item {item.item_key} dup mismatch "
                        f"{item.item_key_dup}"
                    )
                blob = bytes(self._body_data[item.offset:item.offset + item.size])
                if struct.unpack_from("<Q", blob, OFF_BUY)[0] != item.buy_price:
                    issues.append(
                        f"{store.name}: buy roundtrip mismatch on {item.item_key}"
                    )
        return issues


def parse_storeinfo(pabgh_path: str, pabgb_path: str) -> StoreinfoParser:
    parser = StoreinfoParser()
    parser.load_from_files(pabgh_path, pabgb_path)
    parser.load_names()
    return parser


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: storeinfo_parser.py <pabgh> <pabgb>")
        sys.exit(1)
    pabgh = sys.argv[1]
    pabgb = sys.argv[2]
    parser = parse_storeinfo(pabgh, pabgb)
    print(parser.get_summary())
    issues = parser.validate()
    if issues:
        print(f"Validation issues ({len(issues)}):")
        for iss in issues[:30]:
            print(f"  {iss}")
    else:
        print("Validation: all editable stores OK")

    for s in parser.stores:
        if s.kind == "standard" and s.items:
            preview = ", ".join(
                f"{parser.get_item_name(it.item_key)}({it.item_key})"
                for it in s.items[:3]
            )
            if len(s.items) > 3:
                preview += f", ... +{len(s.items)-3} more"
            print(f"  {s.name} (key={s.key}): {len(s.items)} items - {preview}")
