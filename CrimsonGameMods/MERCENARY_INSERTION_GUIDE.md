# Mercenary / Character Insertion Guide

Date: 2026-04-26 — Confirmed working in-game

## Overview

This guide documents how to insert new playable characters (or mounts/pets) into a Crimson Desert save file. The technique was proven by inserting Damian and Oongka into a Chapter 1 save where they don't normally exist, enabling GTA5-style character switching from the start of the game.

The same technique is used by the StandaloneSaveEditor for mount unlocking (wolf, dragon, etc.).

## Prerequisites

- StandaloneSaveEditor codebase (save_crypto, save_parser, parc_serializer, parc_inserter3)
- For playable characters: PAZ overlay with `mercenaryinfo.pabgb` patched (`is_playable=1`, `is_controllable=1`)
- For playable characters: PAZ overlay with `conditioninfo.pabgb` patched (mission gate removed)

## The Core Principle

**Use minimal 155-byte templates, NOT full entries from other saves.**

Every save has its own PARC schema with unique type indices. A full MercenarySaveData entry from a late-game save (5000+ bytes) references dozens of types (ItemDyeSaveData, SkillLearnElementSaveData, etc.) that don't exist in early saves. Inserting those entries causes crashes because the type indices are wrong.

Minimal templates only use types that exist in EVERY save:
- MercenarySaveData (the entry itself)
- Basic sub-types for _levelData

The game auto-populates equipment, skills, buffs, and other data when you first interact with the character.

## Template Structure

A minimal MercenarySaveData entry is ~155 bytes and contains:

```
Offset  Size  Field                    Value
------  ----  -----                    -----
0       2     mbc (mask byte count)    0x0006
2       mbc   mask bytes               [05, 01, 00, 30, 08, 00]
2+mbc   2     type_index               MUST match target save's MercenarySaveData index
10      8     sentinel                 FF FF FF FF FF FF FF FF
18      4     PO (parent offset)       calculated at insertion time
22+     4     _characterKey            u32 character key
26+     8     _mercenaryNo             u64 unique mercenary number
34+     var   _levelData               ~104 bytes, contains 3 nested entries with sentinels
138+    1     _isMainMercenary         0 or 1
139+    1     _isInitialize            1
140+    1     _occupationState         1
        ...   trailing padding/flags
```

### Template Hex (Damian, charKey=4, mercNo=160)

```
0600050100300800260000ffffffffffffffff
5a0305000000000004000000a0000000000000
0001001c1a0000ffffffffffffffff7c030500
00000000010000280000ffffffffffffffff92
0305000000000004000000010000280000ffff
ffffffffffffac03050000000000040000000100
00280000ffffffffffffffffc6030500000000
000400000052000000010101010001010180000000
```

### Template Hex (Oongka, charKey=6, mercNo=522)

```
0600050100300800260000ffffffffffffffff
5a03050000000000060000000a020000000000
0001001c1a0000ffffffffffffffff7c030500
00000000010000280000ffffffffffffffff92
0305000000000004000000010000280000ffff
ffffffffffffac03050000000000040000000100
00280000ffffffffffffffffc6030500000000
000400000052000000010101010001010180000000
```

### Creating a Template for Any Character

Start with the simple mount base (from any working save — the second mount entry is typically 155B). Then:

1. Find `_characterKey` position: search for the 4-byte LE charKey of the base mount
2. Overwrite with your target charKey (u32 LE)
3. Overwrite `_mercenaryNo` (u64 LE, immediately after charKey) with a unique number
   - Use a number not already in the save
   - Convention: use the mercNo from a save where the character exists, or pick a high unused number

### Known Character Keys

| charKey | Character | mercNo (from slot108) |
|:-------:|-----------|:---------------------:|
| 1 | Kliff | — (always exists) |
| 4 | Damian | 160 |
| 6 | Oongka | 522 |
| 1003120 | Rokade (Kliff's Horse) | — (always exists) |
| 1001173 | Damian's Horse | auto-granted by game |
| 1001172 | Oongka's Horse | auto-granted by game |
| 1003918 | Silver Fang (Wolf) | varies |
| 1000799 | Dragon (Blackstar) | varies |

## Insertion Procedure

### Step 1: Load Save and Parse

```python
import save_crypto, save_parser as sp, parc_serializer as ps, parc_inserter3 as pi

save = save_crypto.load_save_file(save_path)
raw = bytearray(save.decompressed_blob)
original_raw = bytes(raw)  # Keep pristine copy for fixup reference
header = save.raw_header

result = sp.build_result_from_raw(bytes(raw), {'input_kind': 'raw_blob'})
parc = ps.parse_parc_blob(bytes(raw))
```

### Step 2: Find _mercenaryDataList and Reference Entry

```python
sentinel = b'\xff' * 8

for obj in result['objects']:
    if 'MercenaryClan' in obj.class_name:
        for f in obj.fields:
            if f.name == '_mercenaryDataList' and f.list_elements:
                merc_list_field = f
        break

# Use the LAST existing entry as type index reference
ref_elem = merc_list_field.list_elements[-1]
ref_raw = bytes(raw)[ref_elem.start_offset:ref_elem.end_offset]
ref_mbc = struct.unpack_from('<H', ref_raw, 0)[0]
ref_main_ti = struct.unpack_from('<H', ref_raw, 2 + ref_mbc)[0]

# Collect nested type indices from reference (sentinel-adjacent)
ref_nested = []
for pos in range(23, len(ref_raw) - 8):
    if ref_raw[pos:pos+8] == sentinel and pos >= 3:
        ref_nested.append(struct.unpack_from('<H', ref_raw, pos - 3)[0])
```

### Step 3: Check Character Doesn't Already Exist

```python
existing_keys = set()
for elem in merc_list_field.list_elements:
    if hasattr(elem, 'child_fields'):
        for cf in elem.child_fields:
            if cf.name == '_characterKey' and cf.present:
                existing_keys.add(struct.unpack_from('<I', bytes(raw), cf.start_offset)[0])

if target_char_key in existing_keys:
    raise RuntimeError(f"charKey={target_char_key} already exists")
```

### Step 4: Fix Type Indices in Template

This is critical. The template has placeholder type indices that must be replaced with the target save's actual indices.

```python
template = bytearray(bytes.fromhex(TEMPLATE_HEX))
mbc = struct.unpack_from('<H', template, 0)[0]

# Fix main type index (right after mask bytes)
struct.pack_into('<H', template, 2 + mbc, ref_main_ti)

# Fix nested type indices (found by scanning for sentinel markers)
tmpl_nested_pos = []
for pos in range(23, len(template) - 8):
    if template[pos:pos+8] == sentinel and pos >= 3:
        tmpl_nested_pos.append(pos - 3)

for i, npos in enumerate(tmpl_nested_pos):
    if i < len(ref_nested):
        struct.pack_into('<H', template, npos, ref_nested[i])
    elif ref_nested:
        struct.pack_into('<H', template, npos, ref_nested[-1])
```

### Step 5: Fix PO (Parent Offset) Values

Every sentinel (0xFF*8) is followed by a 4-byte PO. The PO value = absolute offset of the PO field itself + 4.

```python
for pos in range(len(template) - 12):
    if template[pos:pos+8] == sentinel:
        po_pos = pos + 8
        absolute_offset = insert_pos + po_pos
        struct.pack_into('<I', template, po_pos, absolute_offset + 4)
```

When inserting multiple entries sequentially, add `total_growth` (bytes already inserted) to `insert_pos`:

```python
absolute_offset = (insert_pos + total_growth_so_far) + po_pos
```

### Step 6: Insert Bytes

```python
insert_pos = merc_list_field.list_elements[-1].end_offset
actual_pos = insert_pos + total_growth_so_far
raw[actual_pos:actual_pos] = template
total_growth += len(template)
```

### Step 7: Fix Trailing Sizes

PARC inline objects have a trailing u32 size field. When bytes are inserted, all trailing sizes in ancestor nodes must be updated.

```python
pi._fixup_trailing_sizes(raw, original_raw, insert_pos, total_growth, 'MercenaryClanSaveData')
```

**IMPORTANT**: `original_raw` must be the pristine copy from BEFORE any insertions. `raw` is the modified buffer. `insert_pos` is where the FIRST insertion happened. `total_growth` is the combined size of ALL insertions.

### Step 8: Update List Count

The `_mercenaryDataList` has a count prefix. Format depends on the prefix byte:

```python
list_start = merc_list_field.start_offset
prefix = raw[list_start]

if prefix == 1:  # Big-endian u16 count
    old_c = (raw[list_start+1] << 8) | raw[list_start+2]
    new_c = old_c + num_inserted
    raw[list_start+1] = (new_c >> 8) & 0xFF
    raw[list_start+2] = new_c & 0xFF

elif prefix == 0:  # Little-endian u24 count
    old_c = raw[list_start+1] | (raw[list_start+2] << 8) | (raw[list_start+3] << 16)
    new_c = old_c + num_inserted
    raw[list_start+1] = new_c & 0xFF
    raw[list_start+2] = (new_c >> 8) & 0xFF
```

### Step 9: Fix External POs

All PO values outside the MercenaryClan block that point past the insertion point must be shifted.

```python
# Find MercenaryClan TOC index
merc_toc = None
for i, e in enumerate(parc.toc_entries):
    td = parc.type_by_index.get(e.class_index)
    if td and 'MercenaryClan' in td.name:
        merc_toc = i
        break

po_fixed = pi._fixup_external(raw, original_raw, parc, merc_toc, insert_pos, total_growth)
```

### Step 10: Save

```python
save_crypto.write_save_file(save_path, bytes(raw), header)
```

**IMPORTANT**: Pass `header` (= `save.raw_header`) as the third argument. The header contains version info needed for re-encryption.

### Step 11: Verify

```python
verify = save_crypto.load_save_file(save_path)
v_result = sp.build_result_from_raw(bytes(verify.decompressed_blob), {'input_kind': 'raw_blob'})
# Check _mercenaryDataList has the expected count and charKeys
```

## What the Game Does After Insertion

When loading a save with minimal character entries:

1. **Auto-grants companion mounts** — Damian's Horse (1001173) and Oongka's Horse (1001172) are added automatically
2. **Adds spawn position/yaw** — game populates _spawnPosition and _spawnYaw (entries grow from 155B to ~170B)
3. **Does NOT add equipment/skills** — those get created when you first switch to the character
4. **Preserves all other save data** — only 2 bytes of position float differ on resave

## For Playable Characters: Required PAZ Overlay

Character insertion in the save is necessary but not sufficient. You also need a PAZ overlay (e.g. group 0062) with:

### mercenaryinfo.pabgb

Set `is_playable` and `is_controllable` to 1 for the target character:

| Character | is_controllable offset | is_playable offset | Change |
|-----------|:---------------------:|:-----------------:|--------|
| Damian (key 4) | 0x0086 | 0x0087 | 00 → 01 |
| Oongka (key 6) | 0x00D8 | 0x00D9 | 00 → 01 |

### conditioninfo.pabgb

Replace `CompleteMission(Mission_Intro_Abyss_Tutorial)` with duplicate `CheckCharacterKey(X)` in conditions 4294959693 and 4294959694. **Must keep same 20-byte size**:

```
Damian:  01030e000400000000034800ac440f0000000001  →  01030e000400000000030e000400000000000001
Oongka:  01030e000600000000034800ac440f0000000001  →  01030e000600000000030e000600000000000001
```

### Overlay Packing

Use `PackGroupBuilder(NONE, NONE)` — **NEVER `pack_mod()`** (LZ4 inflates small pabgh files).

```python
builder = crimson_rs.PackGroupBuilder(
    group_dir, crimson_rs.Compression.NONE, crimson_rs.Crypto.NONE)
builder.add_file("gamedata/binary__/client/bin", "mercenaryinfo.pabgb", merc_bytes)
builder.add_file("gamedata/binary__/client/bin", "mercenaryinfo.pabgh", merc_pabgh)
builder.add_file("gamedata/binary__/client/bin", "conditioninfo.pabgb", cond_bytes)
builder.add_file("gamedata/binary__/client/bin", "conditioninfo.pabgh", cond_pabgh)
pamt_bytes = bytes(builder.finish())
```

Install to `CrimsonDesert/0062/` (game root, NOT `paz/0062/`).

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| Using full entries from different save | Type index mismatch → crash |
| Not fixing type indices from reference | Wrong schema types → crash |
| Not passing `original_raw` to fixup functions | Wrong PO calculations → corruption |
| Inserting into already-modified save | Compound errors → corruption |
| Using `pack_mod()` for overlay | LZ4 inflates pabgh → crash |
| Overlay in `paz/` instead of game root | Game ignores overlay |
| Forgetting `raw_header` in write_save_file | Encryption error |

## MercenarySaveData Fields (IDA-confirmed)

| Runtime Offset | Field | Type |
|:-:|---|---|
| 56 (a1[14]) | _ownedCharacterKey | u32 |
| 236 | _isMainMercenary | u8 |
| 237 | _isInitialize | u8 |
| 238 | _isDead | u8 |
| 239 | _isBlockedAbility | u8 |
| 240 | _isHyosiMercenary | u8 |

## MercenaryInfo (pabgb) Fields

12 entries, 452 bytes. CString = u32 len + bytes (NO null terminator).

```
u8    key
CStr  string_key
u8    is_blocked
u32   default_limit_summon_count
u32   default_limit_hire_count
u32   max_limit_hire_count
u8    far_from_leader_option
u8[4] combat_targeting_flags
u8    is_controllable          ← F1 wheel gate
u8    is_playable              ← F1 wheel gate
u8    set_new_mercenary_is_main
u8    main_mercenary_per_tribe
u8    is_force_stackable
u8    is_sellable
u8    use_camp_level
u8    apply_equip_item_stat
u8    spawn_position_type
u8    parent_mercenary_group_info
CArr  hired_skill_info_list
```

## Reference Files

| File | Purpose |
|------|---------|
| `Character unlock Gates.md` | Full research narrative and test results |
| `howtoapplymodoverlay.md` | PAZ overlay installation procedure |
| `MERCENARY_SAVE_FIELDS.md` | IDA-decoded field map |
| `mod_early_character_unlock.py` | conditioninfo patcher |
| `parse_gameplaytriggerinfo.py` | GamePlayTriggerInfo parser (644 entries) |
| `tools/Ship-It/crimson-rs-1.0.4.x/src/tables/mercenary_info/info.rs` | Rust struct definition |
