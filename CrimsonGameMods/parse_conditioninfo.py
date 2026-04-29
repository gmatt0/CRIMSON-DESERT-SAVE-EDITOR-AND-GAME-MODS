import argparse
import json
import struct
from pathlib import Path

from tools.pabgb_toolkit.universal_pabgb_parser import parse_from_files


def _read_u32_string(data, pos, *, has_null=False):
    length = struct.unpack_from("<I", data, pos)[0]
    pos += 4
    value = data[pos:pos + length].decode("utf-8", errors="replace")
    pos += length
    if has_null:
        if pos >= len(data) or data[pos] != 0:
            raise ValueError(f"missing string terminator at 0x{pos:X}")
        pos += 1
    return value, pos


def _is_condition_text(value):
    return all(ord(ch) >= 32 or ch in "\r\n\t" for ch in value)


def _split_condition_payload(payload):
    """Split ConditionInfo payload into compiled bytes, original string, parser type.

    ConditionInfo entries are variable-sized. After the universal entry header
    (_key + nul-terminated _stringKey), the tail is:

        compiled_condition_bytes + u32 originalStringLen + originalString + u8 parserType

    The bytes before _originalString contain the game's compiled expression and
    likely cover the RTTI fields _isBlocked and _gameCondition. Those bytes are
    preserved verbatim until the bytecode format is mapped.
    """
    candidates = []
    for offset in range(max(0, len(payload) - 5)):
        length = struct.unpack_from("<I", payload, offset)[0]
        string_start = offset + 4
        string_end = string_start + length
        if string_end + 1 != len(payload):
            continue
        try:
            original = payload[string_start:string_end].decode("utf-8")
        except UnicodeDecodeError:
            continue
        if _is_condition_text(original):
            candidates.append((offset, original, payload[-1]))

    if not candidates:
        raise ValueError("could not locate terminal _originalString/_parserType")

    original_offset, original, parser_type = candidates[-1]
    return {
        "compiled_condition_offset": 0,
        "compiled_condition_size": original_offset,
        "compiled_condition_hex": payload[:original_offset].hex(),
        "_originalString_offset": original_offset,
        "_originalString": original,
        "_parserType": parser_type,
    }


def _read_pabgh_index(pabgh_bytes):
    """Return (count_size, key_size, records) preserving pabgh record order."""
    if len(pabgh_bytes) < 2:
        raise ValueError("pabgh too small")

    count_u16 = struct.unpack_from("<H", pabgh_bytes, 0)[0]
    candidates = []

    for count_size, count in ((2, count_u16),):
        if count <= 0:
            continue
        total_key_size = len(pabgh_bytes) - count_size - count * 4
        if total_key_size > 0 and total_key_size % count == 0:
            key_size = total_key_size // count
            if key_size in (1, 2, 4, 8):
                candidates.append((count_size, count, key_size))

    if len(pabgh_bytes) >= 4:
        count_u32 = struct.unpack_from("<I", pabgh_bytes, 0)[0]
        total_key_size = len(pabgh_bytes) - 4 - count_u32 * 4
        if count_u32 > 0 and total_key_size > 0 and total_key_size % count_u32 == 0:
            key_size = total_key_size // count_u32
            if key_size in (1, 2, 4, 8):
                candidates.append((4, count_u32, key_size))

    if not candidates:
        raise ValueError("could not detect pabgh index format")

    # Prefer the smallest count prefix that exactly explains the file.
    count_size, count, key_size = candidates[0]
    records = []
    pos = count_size
    for _ in range(count):
        key = int.from_bytes(pabgh_bytes[pos:pos + key_size], "little")
        offset = struct.unpack_from("<I", pabgh_bytes, pos + key_size)[0]
        records.append((key, offset))
        pos += key_size + 4
    return count_size, key_size, records


def _build_pabgh(count_size, key_size, records):
    out = bytearray()
    if count_size == 2:
        out += struct.pack("<H", len(records))
    elif count_size == 4:
        out += struct.pack("<I", len(records))
    else:
        raise ValueError(f"unsupported count_size {count_size}")

    for key, offset in records:
        out += int(key).to_bytes(key_size, "little")
        out += struct.pack("<I", offset)
    return bytes(out)


def _first_diff(a, b):
    limit = min(len(a), len(b))
    for i in range(limit):
        if a[i] != b[i]:
            return i
    if len(a) != len(b):
        return limit
    return None


def serialize_conditioninfo_entry(entry):
    name = entry["_stringKey"].encode("utf-8")
    original = entry["_originalString"].encode("utf-8")
    compiled = bytes.fromhex(entry["compiled_condition_hex"])

    out = bytearray()
    out += struct.pack("<I", entry["_key"])
    out += struct.pack("<I", len(name))
    out += name
    out += b"\x00"
    out += compiled
    out += struct.pack("<I", len(original))
    out += original
    out += bytes([entry["_parserType"]])
    return bytes(out)


def parse_conditioninfo_entry(data, pos=0, end=None):
    """Parse one complete ConditionInfo entry.

    `data[pos:end]` must be a full entry slice, using boundaries from the pabgh
    index. For whole-table parsing, use `parse_conditioninfo_files()`.
    """
    if end is None:
        end = len(data)

    start = pos
    key = struct.unpack_from("<I", data, pos)[0]
    pos += 4
    string_key, pos = _read_u32_string(data, pos, has_null=True)
    payload = data[pos:end]

    entry = {
        "_key": key,
        "_stringKey": string_key,
        "entry_offset": start,
        "entry_size": end - start,
        "payload_size": len(payload),
    }
    entry.update(_split_condition_payload(payload))
    return entry, end


def parse_conditioninfo_files(pabgb_path, pabgh_path, *, include_raw=False):
    pabgb_bytes = Path(pabgb_path).read_bytes()
    pabgh_bytes = Path(pabgh_path).read_bytes()
    parser = parse_from_files(str(pabgb_path), str(pabgh_path), deep=False)
    entries = []
    for parsed_entry in parser.entries:
        raw_entry = pabgb_bytes[
            parsed_entry.file_offset:parsed_entry.file_offset + parsed_entry.entry_size
        ]
        entry = {
            "_key": parsed_entry.key,
            "_stringKey": parsed_entry.name,
            "file_offset": parsed_entry.file_offset,
            "entry_size": parsed_entry.entry_size,
            "payload_size": len(parsed_entry.payload),
        }
        entry.update(_split_condition_payload(parsed_entry.payload))
        if include_raw:
            entry["raw_entry_hex"] = raw_entry.hex()
        entries.append(entry)

    return {
        "table": "conditioninfo",
        "entry_count": len(entries),
        "key_size": parser.key_size,
        "data_size": parser.data_size,
        "schema_size": parser.schema_size,
        "fields": [
            "_key",
            "_stringKey",
            "_isBlocked/_gameCondition (compiled_condition_hex, unmapped)",
            "_originalString",
            "_parserType",
        ],
        "entries": entries,
    }


def roundtrip_conditioninfo_files(pabgb_path, pabgh_path, *, write_prefix=None):
    pabgb_path = Path(pabgb_path)
    pabgh_path = Path(pabgh_path)
    pabgb_bytes = pabgb_path.read_bytes()
    pabgh_bytes = pabgh_path.read_bytes()
    count_size, key_size, records = _read_pabgh_index(pabgh_bytes)

    parsed = parse_conditioninfo_files(pabgb_path, pabgh_path, include_raw=True)
    entries = parsed["entries"]
    by_offset = {entry["file_offset"]: entry for entry in entries}

    rebuilt = bytearray()
    rebuilt_records_by_key = {}
    for key, original_offset in sorted(records, key=lambda item: item[1]):
        entry = by_offset[original_offset]
        new_offset = len(rebuilt)
        rebuilt_entry = serialize_conditioninfo_entry(entry)
        raw_entry = bytes.fromhex(entry["raw_entry_hex"])
        diff = _first_diff(raw_entry, rebuilt_entry)
        if diff is not None:
            return {
                "ok": False,
                "phase": "entry",
                "key": key,
                "offset": original_offset,
                "diff": diff,
                "original_len": len(raw_entry),
                "rebuilt_len": len(rebuilt_entry),
                "original_hex": raw_entry[max(0, diff - 16):diff + 32].hex(" "),
                "rebuilt_hex": rebuilt_entry[max(0, diff - 16):diff + 32].hex(" "),
            }
        rebuilt += rebuilt_entry
        rebuilt_records_by_key[key] = new_offset

    rebuilt_pabgb = bytes(rebuilt)
    diff = _first_diff(pabgb_bytes, rebuilt_pabgb)
    if diff is not None:
        return {
            "ok": False,
            "phase": "pabgb",
            "diff": diff,
            "original_len": len(pabgb_bytes),
            "rebuilt_len": len(rebuilt_pabgb),
            "original_hex": pabgb_bytes[max(0, diff - 16):diff + 32].hex(" "),
            "rebuilt_hex": rebuilt_pabgb[max(0, diff - 16):diff + 32].hex(" "),
        }

    rebuilt_records = [(key, rebuilt_records_by_key[key]) for key, _ in records]
    rebuilt_pabgh = _build_pabgh(count_size, key_size, rebuilt_records)
    diff = _first_diff(pabgh_bytes, rebuilt_pabgh)
    if diff is not None:
        return {
            "ok": False,
            "phase": "pabgh",
            "diff": diff,
            "original_len": len(pabgh_bytes),
            "rebuilt_len": len(rebuilt_pabgh),
            "original_hex": pabgh_bytes[max(0, diff - 16):diff + 32].hex(" "),
            "rebuilt_hex": rebuilt_pabgh[max(0, diff - 16):diff + 32].hex(" "),
        }

    if write_prefix:
        prefix = Path(write_prefix)
        prefix.parent.mkdir(parents=True, exist_ok=True)
        prefix.with_suffix(".pabgb").write_bytes(rebuilt_pabgb)
        prefix.with_suffix(".pabgh").write_bytes(rebuilt_pabgh)

    return {
        "ok": True,
        "entry_count": len(entries),
        "pabgb_size": len(rebuilt_pabgb),
        "pabgh_size": len(rebuilt_pabgh),
        "count_size": count_size,
        "key_size": key_size,
    }


def main():
    ap = argparse.ArgumentParser(description="Parse conditioninfo.pabgb/.pabgh")
    ap.add_argument("pabgb")
    ap.add_argument("pabgh")
    ap.add_argument("--json", "-j", help="Write parsed entries to JSON")
    ap.add_argument("--limit", type=int, default=20, help="Preview row count")
    ap.add_argument("--roundtrip", action="store_true", help="Parse and rebuild byte-identical pabgb/pabgh")
    ap.add_argument("--write-prefix", help="With --roundtrip, write rebuilt files using this path prefix")
    args = ap.parse_args()

    if args.roundtrip:
        result = roundtrip_conditioninfo_files(
            args.pabgb,
            args.pabgh,
            write_prefix=args.write_prefix,
        )
        print(json.dumps(result, indent=2))
        raise SystemExit(0 if result["ok"] else 1)

    result = parse_conditioninfo_files(args.pabgb, args.pabgh)

    if args.json:
        out_path = Path(args.json)
        out_path.write_text(
            json.dumps(result, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"Wrote {result['entry_count']} entries to {out_path}")
        return

    print(f"conditioninfo: {result['entry_count']} entries")
    for entry in result["entries"][:args.limit]:
        name = entry["_stringKey"] or f"0x{entry['_key']:08X}"
        expr = entry["_originalString"].replace("\r", "\\r").replace("\n", "\\n")
        print(
            f"{name}: parserType={entry['_parserType']} "
            f"compiled={entry['compiled_condition_size']}B expr={expr[:120]}"
        )


if __name__ == "__main__":
    main()
