r"""
Early Character Unlock Mod for Crimson Desert
=============================================
Removes the Mission_Intro_Abyss_Tutorial gate from Damian and Oongka's
playability conditions, making them available from the start like Kliff.

The game uses GTA5-style character switching. Kliff has a standalone
condition `CheckCharacterKey(Kliff)` that always passes. Damian and
Oongka have compound conditions:
  CheckCharacterKey(X) && CompleteMission(Mission_Intro_Abyss_Tutorial)

This mod rewrites those compound conditions to standalone character checks,
matching Kliff's pattern exactly.

Usage:
  python mod_early_character_unlock.py --game-dir "C:\Program Files (x86)\Steam\steamapps\common\Crimson Desert"

Or just build the modded files without packing:
  python mod_early_character_unlock.py --build-only
"""

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from parse_conditioninfo import (
    parse_conditioninfo_files,
    serialize_conditioninfo_entry,
    _read_pabgh_index,
    _build_pabgh,
    _first_diff,
)

PABGB_SOURCE = SCRIPT_DIR / "1.0.4 PABGB_PABGH" / "conditioninfo.pabgb"
PABGH_SOURCE = SCRIPT_DIR / "1.0.4 PABGB_PABGH" / "pabgh" / "conditioninfo.pabgh"

OVERLAY_GROUP = "0062"

# --- Target conditions ---

PATCHES = {
    4294959693: {
        "name": "Damian",
        "original": "01030e000400000000034800ac440f0000000001",
        # CheckCharacterKey(4) && CheckCharacterKey(4) — same size, always passes
        "patched": "01030e000400000000030e000400000000000001",
    },
    4294959694: {
        "name": "Oongka",
        "original": "01030e000600000000034800ac440f0000000001",
        # CheckCharacterKey(6) && CheckCharacterKey(6) — same size, always passes
        "patched": "01030e000600000000030e000600000000000001",
    },
}


def build_mod(pabgb_path, pabgh_path):
    pabgb_path = Path(pabgb_path)
    pabgh_path = Path(pabgh_path)
    pabgb_bytes = pabgb_path.read_bytes()
    pabgh_bytes = pabgh_path.read_bytes()

    count_size, key_size, records = _read_pabgh_index(pabgh_bytes)
    parsed = parse_conditioninfo_files(pabgb_path, pabgh_path, include_raw=True)
    entries = parsed["entries"]
    by_offset = {entry["file_offset"]: entry for entry in entries}

    patched_count = 0
    for entry in entries:
        key = entry["_key"]
        if key in PATCHES:
            patch = PATCHES[key]
            if entry["compiled_condition_hex"] != patch["original"]:
                print(f"  WARNING: {patch['name']} (key {key}) bytecode doesn't match expected!")
                print(f"    Expected: {patch['original']}")
                print(f"    Found:    {entry['compiled_condition_hex']}")
                continue

            print(f"  Patching {patch['name']} (key {key}):")
            print(f"    Before: CheckCharacterKey({patch['name']}) && CompleteMission(...)")
            print(f"      hex: {patch['original']} ({len(bytes.fromhex(patch['original']))}B)")
            print(f"    After:  CheckCharacterKey({patch['name']})")
            print(f"      hex: {patch['patched']} ({len(bytes.fromhex(patch['patched']))}B)")
            entry["compiled_condition_hex"] = patch["patched"]
            patched_count += 1

    if patched_count != len(PATCHES):
        found_keys = {e["_key"] for e in entries}
        for ckey, patch in PATCHES.items():
            if ckey not in found_keys:
                print(f"  ERROR: {patch['name']} condition key {ckey} not found in table!")
        if patched_count == 0:
            return None

    # Rebuild pabgb with patched entries, preserving offset order
    rebuilt = bytearray()
    rebuilt_records_by_key = {}

    for key, original_offset in sorted(records, key=lambda item: item[1]):
        entry = by_offset[original_offset]
        new_offset = len(rebuilt)
        rebuilt_entry = serialize_conditioninfo_entry(entry)

        if entry["_key"] not in PATCHES:
            raw_entry = bytes.fromhex(entry["raw_entry_hex"])
            diff = _first_diff(raw_entry, rebuilt_entry)
            if diff is not None:
                print(f"  ROUNDTRIP FAIL: key {entry['_key']} ({entry['_stringKey']}) "
                      f"diff at byte {diff}")
                return None

        rebuilt += rebuilt_entry
        rebuilt_records_by_key[key] = new_offset

    rebuilt_pabgb = bytes(rebuilt)

    # Rebuild pabgh with updated offsets
    new_records = [(key, rebuilt_records_by_key[key]) for key, _ in records]
    rebuilt_pabgh = _build_pabgh(count_size, key_size, new_records)

    print(f"\n  Roundtrip OK: {len(entries)} entries, {patched_count} patched")
    print(f"  pabgb: {len(pabgb_bytes):,}B -> {len(rebuilt_pabgb):,}B "
          f"(delta: {len(rebuilt_pabgb) - len(pabgb_bytes):+,}B)")
    print(f"  pabgh: {len(pabgh_bytes):,}B -> {len(rebuilt_pabgh):,}B")

    return rebuilt_pabgb, rebuilt_pabgh


def pack_overlay(game_dir, pabgb_bytes, pabgh_bytes):
    import crimson_rs.pack_mod
    import crimson_rs

    with tempfile.TemporaryDirectory() as tmp_dir:
        mod_dir = os.path.join(tmp_dir, "gamedata", "binary__", "client", "bin")
        os.makedirs(mod_dir, exist_ok=True)

        with open(os.path.join(mod_dir, "conditioninfo.pabgb"), "wb") as f:
            f.write(pabgb_bytes)
        with open(os.path.join(mod_dir, "conditioninfo.pabgh"), "wb") as f:
            f.write(pabgh_bytes)

        out_dir = os.path.join(tmp_dir, "output")
        os.makedirs(out_dir, exist_ok=True)

        crimson_rs.pack_mod.pack_mod(
            game_dir=game_dir,
            mod_folder=tmp_dir,
            output_dir=out_dir,
            group_name=OVERLAY_GROUP,
        )

        paz_src = os.path.join(out_dir, OVERLAY_GROUP, "0.paz")
        pamt_src = os.path.join(out_dir, OVERLAY_GROUP, "0.pamt")

        # Overlays go in game root (e.g. CrimsonDesert/0062/), NOT paz/0062/
        overlay_dst = os.path.join(game_dir, OVERLAY_GROUP)
        os.makedirs(overlay_dst, exist_ok=True)

        for src_file in (paz_src, pamt_src):
            if os.path.isfile(src_file):
                dst_file = os.path.join(overlay_dst, os.path.basename(src_file))
                shutil.copy2(src_file, dst_file)
                print(f"  Installed: {dst_file} ({os.path.getsize(dst_file):,}B)")

        papgt_path = os.path.join(game_dir, "meta", "0.papgt")
        papgt_backup = papgt_path + ".charmod_bak"
        if os.path.isfile(papgt_path):
            if not os.path.isfile(papgt_backup):
                shutil.copy2(papgt_path, papgt_backup)
                print(f"  PAPGT backed up: {papgt_backup}")

            papgt_data = crimson_rs.parse_papgt_file(papgt_path)
            pamt_bytes = Path(pamt_src).read_bytes() if os.path.isfile(pamt_src) else None
            if pamt_bytes:
                pamt_info = crimson_rs.parse_pamt_bytes(pamt_bytes)
                checksum = pamt_info["checksum"]
            else:
                checksum = crimson_rs.calculate_checksum(pabgb_bytes + pabgh_bytes)

            papgt_data = crimson_rs.add_papgt_entry(
                papgt_data, OVERLAY_GROUP, checksum, 0, 0x3FFF)
            crimson_rs.write_papgt_file(papgt_data, papgt_path)
            print(f"  PAPGT updated with group {OVERLAY_GROUP} (checksum 0x{checksum:08X})")

    return True


def main():
    ap = argparse.ArgumentParser(
        description="Early Character Unlock Mod — removes mission gate from Damian & Oongka"
    )
    ap.add_argument("--game-dir",
                     help="Crimson Desert install directory (for PAZ overlay packing)")
    ap.add_argument("--build-only", action="store_true",
                     help="Build modded files to output/ without packing")
    ap.add_argument("--pabgb", default=str(PABGB_SOURCE),
                     help="Source conditioninfo.pabgb")
    ap.add_argument("--pabgh", default=str(PABGH_SOURCE),
                     help="Source conditioninfo.pabgh")
    args = ap.parse_args()

    if not args.game_dir and not args.build_only:
        ap.error("Either --game-dir or --build-only is required")

    print("Early Character Unlock Mod")
    print("=" * 40)
    print(f"Source pabgb: {args.pabgb}")
    print(f"Source pabgh: {args.pabgh}")
    print()

    if not os.path.isfile(args.pabgb):
        print(f"ERROR: pabgb not found: {args.pabgb}")
        return 1
    if not os.path.isfile(args.pabgh):
        print(f"ERROR: pabgh not found: {args.pabgh}")
        return 1

    print("Patching conditions...")
    result = build_mod(args.pabgb, args.pabgh)
    if result is None:
        print("\nMod build FAILED.")
        return 1

    pabgb_bytes, pabgh_bytes = result

    if args.build_only:
        out_dir = SCRIPT_DIR / "output" / "early_character_unlock"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "conditioninfo.pabgb").write_bytes(pabgb_bytes)
        (out_dir / "conditioninfo.pabgh").write_bytes(pabgh_bytes)
        print(f"\nModded files written to: {out_dir}")
        print("Use pack_mod to create PAZ overlay, or test with the roundtrip parser.")
        return 0

    print(f"\nPacking PAZ overlay (group {OVERLAY_GROUP})...")
    if pack_overlay(args.game_dir, pabgb_bytes, pabgh_bytes):
        print(f"\nMod installed! Restart the game to test.")
        print(f"To revert: delete paz/{OVERLAY_GROUP}/ and restore meta/0.papgt from .charmod_bak")
    else:
        print("\nPacking failed.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
