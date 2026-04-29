"""Swap Hernand furniture shop with barbershop gimmick.

The furniture store location in Hernand will now spawn the barbershop instead.
Deploys as overlay 0067.
"""
import struct, os, sys, shutil, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import crimson_rs

GAME_PATH = "C:/Program Files (x86)/Steam/steamapps/common/Crimson Desert"
DP = "gamedata/binary__/client/bin"
OVERLAY = "0067"

gb = bytearray(crimson_rs.extract_file(GAME_PATH, "0008", DP, "levelgimmicksceneobjectinfo.pabgb"))
gh = bytearray(crimson_rs.extract_file(GAME_PATH, "0008", DP, "levelgimmicksceneobjectinfo.pabgh"))
print(f"Loaded: pabgb={len(gb):,}B pabgh={len(gh):,}B")

# Parse pabgh
c = struct.unpack_from("<I", gh, 0)[0]
records = []
for i in range(c):
    pos = 4 + i * 8
    records.append((struct.unpack_from("<I", gh, pos)[0], struct.unpack_from("<I", gh, pos + 4)[0]))

# Swap: Shop_Furniture_Hernand -> Shop_barbershop_BaseCamp
OLD_NAME = b"Shop_Furniture_Hernand"
NEW_NAME = b"Shop_barbershop_BaseCamp"

old_cstring = struct.pack("<I", len(OLD_NAME)) + OLD_NAME
new_cstring = struct.pack("<I", len(NEW_NAME)) + NEW_NAME
print(f'Swapping: "{OLD_NAME.decode()}" ({len(old_cstring)}B) -> "{NEW_NAME.decode()}" ({len(new_cstring)}B)')

idx = gb.find(old_cstring)
if idx < 0:
    print("ERROR: target string not found!")
    sys.exit(1)

print(f"Found at pabgb offset {idx}")

# Splice
gb[idx:idx + len(old_cstring)] = new_cstring
size_delta = len(new_cstring) - len(old_cstring)
print(f"Spliced: delta={size_delta:+d}B, new pabgb size={len(gb):,}B")

# Rebuild pabgh with shifted offsets
new_records = []
for key, orig_off in records:
    if orig_off > idx:
        new_records.append((key, orig_off + size_delta))
    else:
        new_records.append((key, orig_off))

new_gh = bytearray(struct.pack("<I", len(new_records)))
for k, o in new_records:
    new_gh += struct.pack("<II", k, o)

# Verify
verify_new = gb.find(new_cstring)
verify_old = gb.find(old_cstring)
print(f"Verify: new string at offset {verify_new}")
if verify_old >= 0:
    print(f"WARNING: old string still exists at {verify_old}")
else:
    print("Verify: old string removed OK")

# Deploy
with tempfile.TemporaryDirectory() as tmp_dir:
    group_dir = os.path.join(tmp_dir, OVERLAY)
    builder = crimson_rs.PackGroupBuilder(
        group_dir, crimson_rs.Compression.NONE, crimson_rs.Crypto.NONE)
    builder.add_file(DP, "levelgimmicksceneobjectinfo.pabgb", bytes(gb))
    builder.add_file(DP, "levelgimmicksceneobjectinfo.pabgh", bytes(new_gh))
    pamt_bytes = bytes(builder.finish())
    pamt_checksum = crimson_rs.parse_pamt_bytes(pamt_bytes)["checksum"]

    game_overlay = os.path.join(GAME_PATH, OVERLAY)
    os.makedirs(game_overlay, exist_ok=True)
    for f in os.listdir(group_dir):
        shutil.copy2(os.path.join(group_dir, f), os.path.join(game_overlay, f))
        sz = os.path.getsize(os.path.join(game_overlay, f))
        print(f"  Installed: {OVERLAY}/{f} ({sz:,}B)")

    papgt_path = os.path.join(GAME_PATH, "meta", "0.papgt")
    cur = crimson_rs.parse_papgt_file(papgt_path)
    cur["entries"] = [e for e in cur["entries"] if e.get("group_name") != OVERLAY]
    cur = crimson_rs.add_papgt_entry(cur, OVERLAY, pamt_checksum, is_optional=0, language=0x3FFF)
    crimson_rs.write_papgt_file(cur, papgt_path)
    print(f"  PAPGT updated: {OVERLAY} checksum 0x{pamt_checksum:08X}")

print(f"\nDone! Hernand furniture store location now spawns the barbershop.")
print("Restart game and visit the furniture store spot in Hernand.")
print(f"To revert: delete {GAME_PATH}/{OVERLAY}/ and verify game files.")
