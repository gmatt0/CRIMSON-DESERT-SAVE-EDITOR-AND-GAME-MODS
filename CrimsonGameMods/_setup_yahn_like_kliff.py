"""Set up Yahn (charKey=2) as a playable character matching Kliff's configuration.

Changes:
1. conditioninfo: Add CheckCharacterKey(Yahn) condition + Damian/Oongka patches
2. characterinfo: Yahn _spawnActorType 4->1 (match Kliff)
3. mercenaryinfo: all types playable/controllable, summon limit >=3

All deployed as overlay 0062.
"""
import struct, os, shutil, sys, tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from parse_conditioninfo import (
    parse_conditioninfo_files, serialize_conditioninfo_entry,
    _read_pabgh_index, _build_pabgh,
)
import characterinfo_parser_v2 as cp
import crimson_rs

GAME_PATH = "C:/Program Files (x86)/Steam/steamapps/common/Crimson Desert"
DP = "gamedata/binary__/client/bin"
OVERLAY = "0062"

# ===== 1. CONDITIONINFO =====
print("=== Building conditioninfo ===")
pabgb_path = SCRIPT_DIR / "1.0.4 PABGB_PABGH" / "conditioninfo.pabgb"
pabgh_path = SCRIPT_DIR / "1.0.4 PABGB_PABGH" / "pabgh" / "conditioninfo.pabgh"

pabgb_bytes = pabgb_path.read_bytes()
pabgh_bytes = pabgh_path.read_bytes()
count_size, key_size, records = _read_pabgh_index(pabgh_bytes)
parsed = parse_conditioninfo_files(pabgb_path, pabgh_path, include_raw=True)
entries = parsed["entries"]
by_offset = {e["file_offset"]: e for e in entries}

# Patch Damian/Oongka conditions
PATCHES = {
    4294959693: "01030e000400000000030e000400000000000001",
    4294959694: "01030e000600000000030e000600000000000001",
}
for entry in entries:
    if entry["_key"] in PATCHES:
        entry["compiled_condition_hex"] = PATCHES[entry["_key"]]
        print(f"  Patched condition {entry['_key']}")

# Rebuild pabgb with all existing entries
rebuilt = bytearray()
rebuilt_records = []
for key, original_offset in sorted(records, key=lambda item: item[1]):
    entry = by_offset[original_offset]
    new_offset = len(rebuilt)
    rebuilt += serialize_conditioninfo_entry(entry)
    rebuilt_records.append((key, new_offset))

# Append Yahn's new condition at the end
yahn_cond = {
    "_key": 4294959692,
    "_stringKey": "PlayableCharacter_Yahn",
    "_originalString": "CheckCharacterKey(Yahn)",
    "compiled_condition_hex": "030e000200000000000001",
    "_parserType": 0,
}
yahn_offset = len(rebuilt)
rebuilt += serialize_conditioninfo_entry(yahn_cond)
rebuilt_records.append((yahn_cond["_key"], yahn_offset))

cond_pabgb = bytes(rebuilt)
cond_pabgh = _build_pabgh(count_size, key_size, rebuilt_records)
print(f"  conditioninfo: {len(pabgb_bytes):,}B -> {len(cond_pabgb):,}B "
      f"({len(records)} -> {len(rebuilt_records)} entries)")

# ===== 2. CHARACTERINFO =====
print("\n=== Building characterinfo ===")
ci_gb = crimson_rs.extract_file(GAME_PATH, "0008", DP, "characterinfo.pabgb")
ci_gh = crimson_rs.extract_file(GAME_PATH, "0008", DP, "characterinfo.pabgh")
ci_entries = cp.parse_all(ci_gh, ci_gb)

yahn = cp.get_entry_by_key(ci_entries, 2)
print(f"  Yahn: spawnActorType={yahn.get('_spawnActorType')}, "
      f"mercenaryInfo={yahn.get('_mercenaryInfo')}")

# Find _spawnActorType offset
r = cp.StreamReader(ci_gb, yahn["_pabgh_offset"],
                    yahn["_pabgh_offset"] + len(yahn["_raw"]))
r.read_u32()        # key
r.read_cstring()    # string_key
r.read_u8()         # is_blocked
r.read_locstr()     # characterName
r.read_locstr()     # characterDesc
r.read_hash_u32()   # uiIconPath
r.read_hash_u32()   # category
r.read_cstring()    # characterEditName
sat_off = r.pos - yahn["_pabgh_offset"]

raw = bytearray(yahn["_raw"])
print(f"  _spawnActorType at offset {sat_off}: {raw[sat_off]} -> 1")
raw[sat_off] = 1
yahn["_raw"] = bytes(raw)

new_ci_gh, new_ci_gb = cp.serialize_all_roundtrip(ci_entries, ci_gh)
diffs = sum(1 for i in range(len(ci_gb)) if new_ci_gb[i] != ci_gb[i])
print(f"  characterinfo: {diffs} byte(s) changed")

# ===== 3. MERCENARYINFO =====
print("\n=== Building mercenaryinfo ===")
MI = bytearray(crimson_rs.extract_file(GAME_PATH, "0008", DP, "mercenaryinfo.pabgb"))
MH = crimson_rs.extract_file(GAME_PATH, "0008", DP, "mercenaryinfo.pabgh")

p = 0
merc_changes = 0
while p < len(MI):
    MI[p]; p += 1
    ln = struct.unpack_from("<I", MI, p)[0]; p += 4 + ln
    p += 1
    summon_off = p
    summon = struct.unpack_from("<I", MI, p)[0]; p += 4
    p += 4 + 4 + 1 + 4
    ctrl_off = p; ctrl = MI[p]; p += 1
    play_off = p; play = MI[p]; p += 1
    p += 8
    sc = struct.unpack_from("<I", MI, p)[0]; p += 4 + sc * 8
    if summon <= 1:
        struct.pack_into("<I", MI, summon_off, 3); merc_changes += 1
    if ctrl == 0:
        MI[ctrl_off] = 1; merc_changes += 1
    if play == 0:
        MI[play_off] = 1; merc_changes += 1
print(f"  mercenaryinfo: {merc_changes} fields patched")

# ===== 4. DEPLOY =====
print(f"\n=== Deploying overlay {OVERLAY} ===")
with tempfile.TemporaryDirectory() as tmp_dir:
    group_dir = os.path.join(tmp_dir, OVERLAY)
    builder = crimson_rs.PackGroupBuilder(
        group_dir, crimson_rs.Compression.NONE, crimson_rs.Crypto.NONE)
    builder.add_file(DP, "conditioninfo.pabgb", cond_pabgb)
    builder.add_file(DP, "conditioninfo.pabgh", cond_pabgh)
    builder.add_file(DP, "mercenaryinfo.pabgb", bytes(MI))
    builder.add_file(DP, "mercenaryinfo.pabgh", bytes(MH))
    builder.add_file(DP, "characterinfo.pabgb", bytes(new_ci_gb))
    builder.add_file(DP, "characterinfo.pabgh", bytes(new_ci_gh))
    pamt_bytes = bytes(builder.finish())
    pamt_checksum = crimson_rs.parse_pamt_bytes(pamt_bytes)["checksum"]

    game_overlay = os.path.join(GAME_PATH, OVERLAY)
    os.makedirs(game_overlay, exist_ok=True)
    for f in os.listdir(group_dir):
        shutil.copy2(os.path.join(group_dir, f), os.path.join(game_overlay, f))
        sz = os.path.getsize(os.path.join(game_overlay, f))
        print(f"  {OVERLAY}/{f} ({sz:,}B)")

    papgt_path = os.path.join(GAME_PATH, "meta", "0.papgt")
    cur = crimson_rs.parse_papgt_file(papgt_path)
    cur["entries"] = [e for e in cur["entries"]
                      if e.get("group_name") not in (OVERLAY, "0064")]
    cur = crimson_rs.add_papgt_entry(
        cur, OVERLAY, pamt_checksum, is_optional=0, language=0x3FFF)
    crimson_rs.write_papgt_file(cur, papgt_path)
    print(f"  PAPGT updated: {OVERLAY} checksum 0x{pamt_checksum:08X}")

# Clean up old 0064
old = os.path.join(GAME_PATH, "0064")
if os.path.isdir(old):
    shutil.rmtree(old)
    print("  Removed old 0064/")

print("\nDone! Yahn set up like Kliff:")
print("  - conditioninfo: CheckCharacterKey(Yahn) added")
print("  - characterinfo: _spawnActorType 4->1")
print("  - mercenaryinfo: all types playable+controllable")
print("  - Save already has Yahn MercenarySaveData (from earlier)")
print("Restart game and check F1 wheel.")
