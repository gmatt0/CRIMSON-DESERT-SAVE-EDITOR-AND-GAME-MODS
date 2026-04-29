# How to Apply a Mod Overlay (PAZ)

## Reference Implementation

See `gui/tabs/reserveslot.py` `_apply_to_game()` (line 283) for the canonical pattern used across all CrimsonGameMods tabs.

## Step-by-Step

### 1. Pack with PackGroupBuilder (NONE compression)

**NEVER use `pack_mod()`** — it applies LZ4 compression which inflates small files like `.pabgh` (compressed > uncompressed), causing game crashes.

```python
import crimson_rs
import tempfile, os

INTERNAL_DIR = "gamedata/binary__/client/bin"
GROUP = "0062"

with tempfile.TemporaryDirectory() as tmp_dir:
    group_dir = os.path.join(tmp_dir, GROUP)
    builder = crimson_rs.PackGroupBuilder(
        group_dir, crimson_rs.Compression.NONE, crimson_rs.Crypto.NONE)
    builder.add_file(INTERNAL_DIR, "conditioninfo.pabgb", pabgb_bytes)
    builder.add_file(INTERNAL_DIR, "conditioninfo.pabgh", pabgh_bytes)
    pamt_bytes = bytes(builder.finish())
    pamt_checksum = crimson_rs.parse_pamt_bytes(pamt_bytes)["checksum"]
```

### 2. Copy overlay to GAME ROOT (not paz/)

```
CORRECT:  Crimson Desert/0062/0.paz
CORRECT:  Crimson Desert/0062/0.pamt
WRONG:    Crimson Desert/paz/0062/0.paz   <-- NEVER DO THIS
```

```python
game_overlay = os.path.join(game_dir, GROUP)
os.makedirs(game_overlay, exist_ok=True)
for f in os.listdir(group_dir):
    shutil.copy2(os.path.join(group_dir, f),
                 os.path.join(game_overlay, f))
```

### 3. Update PAPGT

```python
papgt_path = os.path.join(game_dir, "meta", "0.papgt")

# Backup FIRST (only once — don't overwrite existing backup)
bak = papgt_path + ".yourtool_bak"
if not os.path.exists(bak) and os.path.isfile(papgt_path):
    shutil.copy2(papgt_path, bak)

# Parse, remove old entry for this group, add new entry
cur = crimson_rs.parse_papgt_file(papgt_path)
cur["entries"] = [e for e in cur["entries"]
                  if e.get("group_name") != GROUP]
cur = crimson_rs.add_papgt_entry(
    cur, GROUP, pamt_checksum,
    is_optional=0, language=0x3FFF)
crimson_rs.write_papgt_file(cur, papgt_path)
```

### 4. Verify

```python
# PAPGT roundtrips
verify = crimson_rs.parse_papgt_file(papgt_path)
for e in verify["entries"]:
    if e["group_name"] == GROUP:
        assert e["pack_meta_checksum"] == pamt_checksum
```

## Internal PAZ Path

**ALWAYS** use the full internal path for game data files:

```
gamedata/binary__/client/bin/filename.pabgb
```

NOT `gamedata/filename.pabgb`. The PAMT maps the full path. Wrong path = game loads vanilla instead of mod.

## Overlay Group Numbers

- Use numeric names: `0058`, `0059`, `0062`, `0063`, etc.
- PAPGT rejects non-numeric group names (exception: `dmmsa`/`dmmgen` are legacy)
- Don't reuse groups already in use:
  - `0058` = iteminfo (ItemBuffs)
  - `0059` = equipslotinfo
  - `0060` = storeinfo (Stores)
  - `0062` = conditioninfo (character unlock mod)
  - `0064`, `0066`, `0085` = other mods

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| `pack_mod()` with LZ4 | pabgh inflates (compressed > uncompressed), game crash |
| Overlay in `paz/0062/` | Game ignores it, loads vanilla |
| Backup already-modded PAPGT | Restoring "backup" still broken |
| Missing `is_optional=0, language=0x3FFF` | `add_papgt_entry` throws TypeError |
| Not removing old entry before add | Duplicate entries (add_papgt_entry upserts, but be explicit) |
| Wrong internal path | PAMT entry has wrong path, game loads vanilla silently |

## Revert

1. Delete the overlay directory: `Crimson Desert/0062/`
2. Restore PAPGT from backup: copy `.yourtool_bak` back to `0.papgt`
3. Or: Steam → Verify Integrity of Game Files (nuclear option)
