"""
GamePlayTriggerInfo parser — decoded from IDA sub_1410E0100.

Binary layout per entry (pabgh-bounded):
  u32   _key
  CStr  _stringKey (u32 len + bytes, NO null terminator)
  u8    _isBlocked
  u8    field_u8_1
  u8    field_u8_2
  u8    field_u8_3
  u32   conditionInfoKey_hash (looked up in ConditionInfo dict at runtime)
  u32   unknown_hash_1 (looked up in another dict at runtime → u16)
  u8[12] params_block (3x float or 3x u32)
  u32   field_u32_1
  u8    field_u8_4
  u32   skillGroupInfoKey_hash (looked up in SkillGroupInfo dict at runtime)
  CArray tagged_list (u32 count + count * {u8 tag + variant payload})

Tagged list variants:
  tag=0: sub_2594 reader (u16)
  tag=1: sub_2614 reader (u32)
  tag=2: sub_2591 reader (u16)
  tag=3: sub_2589 reader (u16)
"""

import argparse
import json
import struct
from pathlib import Path


def read_cstring(data, pos):
    length = struct.unpack_from("<I", data, pos)[0]
    pos += 4
    value = data[pos:pos + length].decode("utf-8", errors="replace")
    pos += length
    return value, pos


def read_pabgh_index(pabgh_bytes):
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
        raise ValueError("could not detect pabgh format")

    count_size, count, key_size = candidates[0]
    records = []
    pos = count_size
    for _ in range(count):
        key = int.from_bytes(pabgh_bytes[pos:pos + key_size], "little")
        offset = struct.unpack_from("<I", pabgh_bytes, pos + key_size)[0]
        records.append((key, offset))
        pos += key_size + 4
    return count_size, key_size, records


def parse_tagged_list(data, pos, end):
    if pos + 4 > end:
        return [], pos
    count = struct.unpack_from("<I", data, pos)[0]
    pos += 4
    items = []
    for _ in range(count):
        if pos >= end:
            break
        tag = data[pos]
        pos += 1
        if tag == 0:
            val = struct.unpack_from("<H", data, pos)[0]
            pos += 2
            items.append({"tag": 0, "value": val})
        elif tag == 1:
            val = struct.unpack_from("<I", data, pos)[0]
            pos += 4
            items.append({"tag": 1, "value": val})
        elif tag == 2:
            val = struct.unpack_from("<H", data, pos)[0]
            pos += 2
            items.append({"tag": 2, "value": val})
        elif tag == 3:
            val = struct.unpack_from("<H", data, pos)[0]
            pos += 2
            items.append({"tag": 3, "value": val})
        else:
            items.append({"tag": tag, "error": "unknown tag"})
            break
    return items, pos


def parse_entry(data, start, end):
    pos = start
    key = struct.unpack_from("<I", data, pos)[0]
    pos += 4
    string_key, pos = read_cstring(data, pos)
    is_blocked = data[pos]; pos += 1
    field_u8_1 = data[pos]; pos += 1
    field_u8_2 = data[pos]; pos += 1
    field_u8_3 = data[pos]; pos += 1

    # Complex field: reads u32 hash from stream (4 bytes consumed)
    condition_hash = struct.unpack_from("<I", data, pos)[0]
    pos += 4

    # Second hash lookup: reads u32 hash (4 bytes consumed)
    unknown_hash_1 = struct.unpack_from("<I", data, pos)[0]
    pos += 4

    # 12-byte params block
    params = struct.unpack_from("<fff", data, pos)
    params_raw = data[pos:pos + 12].hex()
    pos += 12

    field_u32_1 = struct.unpack_from("<I", data, pos)[0]
    pos += 4

    field_u8_4 = data[pos]
    pos += 1

    # SkillGroupInfo hash
    skill_group_hash = struct.unpack_from("<I", data, pos)[0]
    pos += 4

    # Tagged polymorphic array
    tagged_list, pos = parse_tagged_list(data, pos, end)

    consumed = pos - start
    expected = end - start

    return {
        "_key": key,
        "_stringKey": string_key,
        "_isBlocked": is_blocked,
        "field_u8_1": field_u8_1,
        "field_u8_2": field_u8_2,
        "field_u8_3": field_u8_3,
        "conditionInfoKey_hash": f"0x{condition_hash:08X}",
        "conditionInfoKey_raw": condition_hash,
        "unknown_hash_1": f"0x{unknown_hash_1:08X}",
        "params_float": [round(p, 4) for p in params],
        "params_hex": params_raw,
        "field_u32_1": field_u32_1,
        "field_u8_4": field_u8_4,
        "skillGroupInfoKey_hash": f"0x{skill_group_hash:08X}",
        "skillGroupInfoKey_raw": skill_group_hash,
        "tagged_list": tagged_list,
        "entry_offset": start,
        "entry_size": expected,
        "consumed": consumed,
        "parse_ok": consumed == expected,
    }


def parse_gameplaytriggerinfo(pabgb_path, pabgh_path):
    pabgb = Path(pabgb_path).read_bytes()
    pabgh = Path(pabgh_path).read_bytes()
    count_size, key_size, records = read_pabgh_index(pabgh)

    sorted_records = sorted(records, key=lambda r: r[1])
    offsets = [r[1] for r in sorted_records]

    entries = []
    parse_errors = 0
    for i, (key, offset) in enumerate(sorted_records):
        end = sorted_records[i + 1][1] if i + 1 < len(sorted_records) else len(pabgb)
        try:
            entry = parse_entry(pabgb, offset, end)
            if not entry["parse_ok"]:
                parse_errors += 1
            entries.append(entry)
        except Exception as e:
            parse_errors += 1
            entries.append({
                "_key": key,
                "entry_offset": offset,
                "entry_size": end - offset,
                "error": str(e),
            })

    return {
        "table": "gameplaytriggerinfo",
        "entry_count": len(entries),
        "parse_errors": parse_errors,
        "pabgh_count_size": count_size,
        "pabgh_key_size": key_size,
        "entries": entries,
    }


def main():
    ap = argparse.ArgumentParser(description="Parse gameplaytriggerinfo.pabgb")
    ap.add_argument("pabgb")
    ap.add_argument("pabgh")
    ap.add_argument("--json", "-j", help="Write to JSON file")
    ap.add_argument("--filter", "-f", help="Filter entries by name substring")
    ap.add_argument("--limit", type=int, default=0, help="Limit output rows (0=all)")
    args = ap.parse_args()

    result = parse_gameplaytriggerinfo(args.pabgb, args.pabgh)

    if args.json:
        Path(args.json).write_text(
            json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote {result['entry_count']} entries ({result['parse_errors']} errors) to {args.json}")
        return

    print(f"gameplaytriggerinfo: {result['entry_count']} entries, {result['parse_errors']} parse errors")
    print()

    shown = 0
    for entry in result["entries"]:
        if "error" in entry:
            print(f"  ERROR key={entry['_key']}: {entry['error']}")
            continue

        name = entry["_stringKey"] or f"0x{entry['_key']:08X}"
        if args.filter and args.filter.lower() not in name.lower():
            continue

        ok = "OK" if entry["parse_ok"] else f"MISMATCH({entry['consumed']}/{entry['entry_size']})"
        print(f"  {name}")
        print(f"    key={entry['_key']} blocked={entry['_isBlocked']} [{ok}]")
        print(f"    conditionHash={entry['conditionInfoKey_hash']}  unknownHash={entry['unknown_hash_1']}")
        print(f"    params={entry['params_float']}  u32={entry['field_u32_1']}  u8s=[{entry['field_u8_1']},{entry['field_u8_2']},{entry['field_u8_3']},{entry['field_u8_4']}]")
        print(f"    skillGroupHash={entry['skillGroupInfoKey_hash']}")
        if entry["tagged_list"]:
            print(f"    tagged_list={entry['tagged_list']}")
        print()

        shown += 1
        if args.limit and shown >= args.limit:
            break


if __name__ == "__main__":
    main()
