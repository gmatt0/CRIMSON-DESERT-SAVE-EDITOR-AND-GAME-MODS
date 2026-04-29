r"""
Quest Character Unlock Mod for Crimson Desert
==============================================
Patches questinfo.pabgb to allow all 3 playable characters (Kliff, Damiane,
Oongka) on every quest that has a non-empty start_player_list.

72 quests have explicit character restrictions. This mod expands ALL of them
to [1, 4, 6] (all three) so any character can play any quest without camera
bugs or being kicked out. The 833 quests with empty lists are untouched.

Usage:
  # Build + install overlay in one step:
  python mod_quest_char_unlock.py --game-dir "C:\Program Files (x86)\Steam\steamapps\common\Crimson Desert"

  # Build modded files only (no install):
  python mod_quest_char_unlock.py --build-only

  # Revert:
  python mod_quest_char_unlock.py --game-dir "..." --revert
"""

import argparse
import os
import shutil
import struct
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

OVERLAY_GROUP = "0063"
INTERNAL_DIR = "gamedata/binary__/client/bin"
PLAYER_KEYS = [1, 4, 6]  # Kliff, Damiane, Oongka
BACKUP_SUFFIX = ".questcharmod_bak"


# ── Binary readers (mirrors dmm-parser wire format) ─────────────────────────

def _read_u8(d, p):
    return d[p], p + 1

def _read_u16(d, p):
    return struct.unpack_from('<H', d, p)[0], p + 2

def _read_u32(d, p):
    return struct.unpack_from('<I', d, p)[0], p + 4

def _read_u64(d, p):
    return struct.unpack_from('<Q', d, p)[0], p + 8

def _skip_cstring(d, p):
    ln, p = _read_u32(d, p)
    return p + ln

def _skip_locstr(d, p):
    _, p = _read_u8(d, p)
    _, p = _read_u64(d, p)
    return _skip_cstring(d, p)

def _skip_carray_u8(d, p):
    cnt, p = _read_u32(d, p)
    return p + cnt

def _read_carray_u32(d, p):
    cnt, p = _read_u32(d, p)
    vals = []
    for _ in range(cnt):
        v, p = _read_u32(d, p)
        vals.append(v)
    return vals, p


def _parse_pabgh(pabgh_bytes):
    count = struct.unpack_from('<I', pabgh_bytes, 0)[0]
    records = []
    for i in range(count):
        pos = 4 + i * 8
        k = struct.unpack_from('<I', pabgh_bytes, pos)[0]
        off = struct.unpack_from('<I', pabgh_bytes, pos + 4)[0]
        records.append((k, off))
    return count, records


def _entry_boundaries(records, data_len):
    sorted_recs = sorted(records, key=lambda x: x[1])
    bounds = {}
    for i, (k, off) in enumerate(sorted_recs):
        nxt = sorted_recs[i + 1][1] if i + 1 < len(sorted_recs) else data_len
        bounds[k] = (off, nxt)
    return bounds


def _find_start_player_list(D, start, end):
    """Skip fields 1-11 of QuestInfo to locate start_player_list (field 12).

    Returns (spl_start, spl_end, values) or None on parse failure.
    """
    p = start
    try:
        _, p = _read_u32(D, p)       # 1  key
        p = _skip_cstring(D, p)      # 2  string_key
        _, p = _read_u8(D, p)        # 3  is_blocked
        _, p = _read_u8(D, p)        # 4  quest_type
        _, p = _read_u8(D, p)        # 5  quest_category
        p = _skip_locstr(D, p)       # 6  name
        p = _skip_locstr(D, p)       # 7  desc
        _, p = _read_u16(D, p)       # 8  quest_group_info
        _, p = _read_u32(D, p)       # 9  faction_info
        # 10 FactionStateData
        p = _skip_carray_u8(D, p)    #    activate_faction_state_list
        _, p = _read_u32(D, p)       #    player_condition_info
        _, p = _read_u32(D, p)       #    relation_target_faction_info
        _, p = _read_u8(D, p)        #    relation_type
        # 11 BranchData (18 bytes fixed)
        _, p = _read_u32(D, p)       #    quest_key
        _, p = _read_u32(D, p)       #    cond_key
        _, p = _read_u8(D, p)        #    byte_a
        _, p = _read_u8(D, p)        #    byte_b
        _, p = _read_u32(D, p)       #    u32_a
        _, p = _read_u32(D, p)       #    u32_b
        # 12 start_player_list
        spl_start = p
        spl_vals, p = _read_carray_u32(D, p)
        return spl_start, p, spl_vals
    except (struct.error, IndexError):
        return None


def _build_carray_u32(vals):
    out = struct.pack('<I', len(vals))
    for v in vals:
        out += struct.pack('<I', v)
    return out


# ── Core patcher ─────────────────────────────────────────────────────────────

def build_mod(pabgb_bytes, pabgh_bytes):
    D = bytearray(pabgb_bytes)
    count, records = _parse_pabgh(pabgh_bytes)
    bounds = _entry_boundaries(records, len(D))

    to_patch = {}
    for key, (start, end) in bounds.items():
        result = _find_start_player_list(D, start, end)
        if result is None:
            continue
        spl_start, spl_end, spl_vals = result
        if spl_vals and sorted(spl_vals) != sorted(PLAYER_KEYS):
            to_patch[key] = (spl_start, spl_end, spl_vals)

    print(f"  Found {len(to_patch)} character-restricted quests to patch")

    new_spl = _build_carray_u32(PLAYER_KEYS)

    rebuilt_pabgb = bytearray()
    new_offsets = {}
    size_delta = 0

    for key, orig_off in sorted(records, key=lambda x: x[1]):
        start, end = bounds[key]
        new_offsets[key] = len(rebuilt_pabgb)

        if key in to_patch:
            spl_start, spl_end, old_vals = to_patch[key]
            old_size = spl_end - spl_start
            rebuilt_pabgb += D[start:spl_start]
            rebuilt_pabgb += new_spl
            rebuilt_pabgb += D[spl_end:end]
            size_delta += len(new_spl) - old_size
        else:
            rebuilt_pabgb += D[start:end]

    rebuilt_pabgh = bytearray(struct.pack('<I', count))
    for key, _ in records:
        rebuilt_pabgh += struct.pack('<I', key)
        rebuilt_pabgh += struct.pack('<I', new_offsets[key])

    growth = len(rebuilt_pabgb) - len(D)
    print(f"  pabgb: {len(D):,}B -> {len(rebuilt_pabgb):,}B (delta: {growth:+}B)")
    assert growth == size_delta, f"size mismatch: got {growth:+}, expected {size_delta:+}"

    # Verify
    count2, recs2 = _parse_pabgh(bytes(rebuilt_pabgh))
    bounds2 = _entry_boundaries(recs2, len(rebuilt_pabgb))
    verified = 0
    for key in to_patch:
        result = _find_start_player_list(rebuilt_pabgb, *bounds2[key])
        assert result is not None, f"re-parse failed for key {key}"
        assert result[2] == PLAYER_KEYS, f"key {key}: expected {PLAYER_KEYS}, got {result[2]}"
        verified += 1
    print(f"  Verified {verified} patched entries have {PLAYER_KEYS}")

    return bytes(rebuilt_pabgb), bytes(rebuilt_pabgh)


def pack_and_install(game_dir, pabgb_bytes, pabgh_bytes):
    import crimson_rs

    with tempfile.TemporaryDirectory() as tmp_dir:
        group_dir = os.path.join(tmp_dir, OVERLAY_GROUP)
        builder = crimson_rs.PackGroupBuilder(
            group_dir, crimson_rs.Compression.NONE, crimson_rs.Crypto.NONE)
        builder.add_file(INTERNAL_DIR, "questinfo.pabgb", pabgb_bytes)
        builder.add_file(INTERNAL_DIR, "questinfo.pabgh", pabgh_bytes)
        pamt_bytes = bytes(builder.finish())
        pamt_checksum = crimson_rs.parse_pamt_bytes(pamt_bytes)["checksum"]

        # Copy overlay to game root
        game_overlay = os.path.join(game_dir, OVERLAY_GROUP)
        os.makedirs(game_overlay, exist_ok=True)
        for f in os.listdir(group_dir):
            src = os.path.join(group_dir, f)
            dst = os.path.join(game_overlay, f)
            shutil.copy2(src, dst)
            print(f"  Installed: {dst} ({os.path.getsize(dst):,}B)")

        # Update PAPGT
        papgt_path = os.path.join(game_dir, "meta", "0.papgt")
        bak = papgt_path + BACKUP_SUFFIX
        if os.path.isfile(papgt_path) and not os.path.isfile(bak):
            shutil.copy2(papgt_path, bak)
            print(f"  PAPGT backed up: {bak}")

        cur = crimson_rs.parse_papgt_file(papgt_path)
        cur["entries"] = [e for e in cur["entries"]
                          if e.get("group_name") != OVERLAY_GROUP]
        cur = crimson_rs.add_papgt_entry(
            cur, OVERLAY_GROUP, pamt_checksum,
            is_optional=0, language=0x3FFF)
        crimson_rs.write_papgt_file(cur, papgt_path)
        print(f"  PAPGT updated: group {OVERLAY_GROUP} checksum 0x{pamt_checksum:08X}")

        # Verify
        verify = crimson_rs.parse_papgt_file(papgt_path)
        found = False
        for e in verify["entries"]:
            if e["group_name"] == OVERLAY_GROUP:
                assert e["pack_meta_checksum"] == pamt_checksum
                found = True
        assert found, f"group {OVERLAY_GROUP} not found in PAPGT after write"
        print("  PAPGT verification OK")

    return True


def revert(game_dir):
    game_overlay = os.path.join(game_dir, OVERLAY_GROUP)
    if os.path.isdir(game_overlay):
        shutil.rmtree(game_overlay)
        print(f"  Deleted overlay: {game_overlay}")
    else:
        print(f"  No overlay to delete: {game_overlay}")

    papgt_path = os.path.join(game_dir, "meta", "0.papgt")
    bak = papgt_path + BACKUP_SUFFIX
    if os.path.isfile(bak):
        shutil.copy2(bak, papgt_path)
        print(f"  PAPGT restored from: {bak}")
    else:
        print(f"  No PAPGT backup found ({bak})")
        print("  Run Steam -> Verify Integrity to restore PAPGT")


def main():
    ap = argparse.ArgumentParser(
        description="Quest Character Unlock — allow Damiane & Oongka on all quests")
    ap.add_argument("--game-dir",
                     help="Crimson Desert install directory")
    ap.add_argument("--build-only", action="store_true",
                     help="Build modded files to output/ without installing")
    ap.add_argument("--revert", action="store_true",
                     help="Remove overlay and restore PAPGT")
    args = ap.parse_args()

    if args.revert:
        if not args.game_dir:
            ap.error("--game-dir required for --revert")
        print("Reverting Quest Character Unlock mod...")
        revert(args.game_dir)
        return 0

    if not args.game_dir and not args.build_only:
        ap.error("Either --game-dir or --build-only is required")

    print("Quest Character Unlock Mod")
    print("=" * 40)

    # Extract vanilla questinfo from game
    import crimson_rs
    game_dir = args.game_dir or "C:/Program Files (x86)/Steam/steamapps/common/Crimson Desert"
    dp = "gamedata/binary__/client/bin"

    print("Extracting questinfo from game archives...")
    pabgb = crimson_rs.extract_file(game_dir, "0008", dp, "questinfo.pabgb")
    pabgh = crimson_rs.extract_file(game_dir, "0008", dp, "questinfo.pabgh")
    print(f"  questinfo: {len(pabgb):,}B pabgb, {len(pabgh):,}B pabgh")

    print("\nPatching start_player_list...")
    patched_pabgb, patched_pabgh = build_mod(pabgb, pabgh)

    if args.build_only:
        out_dir = SCRIPT_DIR / "output" / "quest_char_unlock"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "questinfo.pabgb").write_bytes(patched_pabgb)
        (out_dir / "questinfo.pabgh").write_bytes(patched_pabgh)
        print(f"\nModded files written to: {out_dir}")
        return 0

    print(f"\nInstalling overlay (group {OVERLAY_GROUP})...")
    if pack_and_install(args.game_dir, patched_pabgb, patched_pabgh):
        print(f"\nMod installed! Restart the game to test.")
        print(f"To revert: python {Path(__file__).name} --game-dir \"{args.game_dir}\" --revert")

    return 0


if __name__ == "__main__":
    sys.exit(main())
