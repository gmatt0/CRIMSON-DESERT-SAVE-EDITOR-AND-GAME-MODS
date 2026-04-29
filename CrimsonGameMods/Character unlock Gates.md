# Character Unlock Gates — Crimson Desert

Date: 2026-04-26 (updated after testing)

## Goal

Unlock the other 2 playable characters (Damian, Oongka) from the start of the game. The game uses GTA5-style character switching — once unlocked, you hold F1 to open the character wheel and swap. We want to remove the story gates so all 3 are available immediately.

## The 3 Playable Characters

| Key | Character | Tribe Hashes | Notes |
|-----|-----------|-------------|-------|
| 1 | Kliff | 11 hashes (superset) | Default, always available |
| 4 | Damiane | 4 hashes (subset of Kliff) | Gated behind story mission |
| 6 | Oongka | 6 hashes (subset of Kliff) | Gated behind story mission |

### Tribe Hash Mapping

**Kliff (11):**
`0x13FB2B6E`, `0x26BE971F`, `0x87D08287`, `0x8BF46446`, `0xABFCD791`, `0xBFA1F64B`, `0xD0A2E1EF`, `0xF96C1DD4`, `0xFC66D914`, `0xFE7169E2`, `0xFF16A579`

**Damiane (4):**
`0x26BE971F`, `0x8BF46446`, `0xABFCD791`, `0xF96C1DD4`

**Oongka (6):**
`0x13FB2B6E`, `0x87D08287`, `0xBFA1F64B`, `0xD0A2E1EF`, `0xFC66D914`, `0xFE7169E2`

**Union set (12):** All of above + `0xF21FE2D6` (unknown/NPC hash)

Source: `gui/tabs/buffs_v319.py` lines 7137-7149, `_CHAR_TRIBE_HASHES` / `_PLAYER_CHAR_KEYS`

## Two-Layer Unlock System (Confirmed)

Character availability is controlled by **two independent systems**. Both must be satisfied.

### Layer 1: F1 Wheel Visibility — `mercenaryinfo.pabgb`

The F1 character wheel reads `is_playable` and `is_controllable` from `mercenaryinfo.pabgb`.

| Key | Character | is_playable | is_controllable | In F1 Wheel |
|-----|-----------|:-----------:|:---------------:|:-----------:|
| 1 | Kliff | 1 | 1 | Yes |
| 4 | Damian | 0 | 0 | No |
| 6 | Oongka | 0 | 0 | No |

**Fix:** Set both fields to 1 for Damian and Oongka.

Byte offsets in mercenaryinfo.pabgb (452B, 12 entries, no pabgh needed for parsing):

| Character | is_controllable offset | is_playable offset |
|-----------|:---------------------:|:-----------------:|
| Damian (key 4) | 0x0086 | 0x0087 |
| Oongka (key 6) | 0x00D8 | 0x00D9 |

**Confirmed: is_playable alone is NOT sufficient.** User tested previously — characters don't appear in wheel without also addressing Layer 2.

### Layer 2: Condition Gate — `conditioninfo.pabgb`

The game evaluates compiled bytecode conditions to determine if a character switch is allowed.

**Kliff has a standalone condition (always passes):**
- Key: `4294967060`
- Expression: `CheckCharacterKey(Kliff)`
- Bytecode (11B): `03 0e 00 01 00 00 00 00 00 00 01`

**Damian and Oongka have compound conditions (require mission completion):**

| Character | Condition Key | Expression | Bytecode (20B) |
|-----------|:------------:|------------|----------------|
| Damian | 4294959693 | `CheckCharacterKey(Damian) && CompleteMission(Mission_Intro_Abyss_Tutorial)` | `01030e000400000000034800ac440f0000000001` |
| Oongka | 4294959694 | `CheckCharacterKey(Oongka) && CompleteMission(Mission_Intro_Abyss_Tutorial)` | `01030e000600000000034800ac440f0000000001` |

Gate mission: `Mission_Intro_Abyss_Tutorial` (key `1000620`, "Realm of Uncertainty").

**Fix:** Replace `CompleteMission` with a duplicate `CheckCharacterKey` (same size, always passes):

```
Damian:  01030e000400000000034800ac440f0000000001  (original, 20B)
      -> 01030e000400000000030e000400000000000001  (patched, 20B)

Oongka:  01030e000600000000034800ac440f0000000001  (original, 20B)
      -> 01030e000600000000030e000600000000000001  (patched, 20B)
```

**CRITICAL: Patched bytecodes MUST be the same size as originals.** Shorter bytecodes shift all pabgh offsets and cause crashes.

### Bytecode Structure

```
Compound: [01] [03 0e00 KKKKKKKK 00] [03 4800 MMMMMMMM 00] [00 00 01]
           AND  CheckCharacterKey(K)   CompleteMission(M)    trailing

Patched:  [01] [03 0e00 KKKKKKKK 00] [03 0e00 KKKKKKKK 00] [00 00 01]
           AND  CheckCharacterKey(K)   CheckCharacterKey(K)   trailing
```

- Tag `0x0e` (14) = CheckCharacterKey, payload = u32 character key
- Tag `0x48` (72) = CompleteMission, payload = u32 mission key
- `0x000F44AC` = 1000620 = Mission_Intro_Abyss_Tutorial

## MercenaryInfo Full Structure

12 entries, 452 bytes total. No pabgh needed (sequential read). CString = u32 len + bytes (NO null terminator).

```
u8    key
CStr  string_key
u8    is_blocked
u32   default_limit_summon_count
u32   default_limit_hire_count
u32   max_limit_hire_count
u8    far_from_leader_option
u8[4] combat_targeting_flags
u8    is_controllable          <-- GATE
u8    is_playable              <-- GATE
u8    set_new_mercenary_is_main
u8    main_mercenary_per_tribe
u8    is_force_stackable
u8    is_sellable
u8    use_camp_level
u8    apply_equip_item_stat
u8    spawn_position_type
u8    parent_mercenary_group_info
CArr  hired_skill_info_list    (u32 count + count * {u32, u32})
```

Source: `tools/Ship-It/crimson-rs-1.0.4.x/src/tables/mercenary_info/info.rs`

## Additional Triggers (Unknown Effect)

12 `GamePlayTrigger_PlayableCharacter_*` entries tied to specific regions:
- `Her_HalsiusHospital`, `Her_ReedDevil`, `Her_KildenKukuWorkshop`, `Her_ScholarStoneInstitute`
- `Del_ClockTower`, `Del_GorthakIron`, `Del_AIMarni`
- `Crim_EnlightenShrine`
- `Dem_HexeSanctuary`, `Dem_JiJeongTemple`
- `Her_GoldenFistsArena`, `Her_GreyWolfCamp`

These are in `gameplaytriggerinfo.pabgb` which is a **blob table** (not decoded). Their effect on character availability is unknown — they may be secondary gates checked at specific map locations.

Debug command `/execute playmctest` grants both characters (from BLACKSPACE_GAME_COMMANDS.md). This likely sets both mercenaryinfo flags AND completes the mission.

## characterchangeinfo.pabgb — Red Herring

Despite the name, this table controls **weapon/appearance changes** (WeaponType_OneHandWeapon, Tier, Job_A-E, Gender_A), NOT character switching. 10 entries, blob format, not relevant to this mod.

## What We Ruled Out

| Approach | Result |
|----------|--------|
| `reserveslotinfo` editing alone | Can rearrange slots but game enforces unlock |
| `mercenaryinfo` is_playable alone | Not sufficient (user tested) |
| `conditioninfo` condition removal alone | Overlay loads, bytes patched correctly, but F1 wheel doesn't show characters (need mercenaryinfo too) |
| `mercenaryinfo` + `conditioninfo` combined (overlay 0062) | Overlay loads, both patches verified in memory, **still no effect on either save** |
| Save editing (mark mission complete) | Doesn't work (user tested) |
| `characterchangeinfo` | Wrong table — it's about weapon/appearance changes |

## Current Mod: Combined Overlay (0062)

Overlay group `0062` in game root directory contains:

| File | Size | Changes |
|------|------|---------|
| conditioninfo.pabgb | 786,534B | 2 condition bytecodes patched (same size) |
| conditioninfo.pabgh | 71,474B | Unchanged (offsets identical due to same-size patch) |
| mercenaryinfo.pabgb | 452B | 4 bytes changed (is_playable + is_controllable for Damian & Oongka) |
| mercenaryinfo.pabgh | 62B | Unchanged |

Packed with `PackGroupBuilder(NONE, NONE)` — no LZ4 compression.

**Status: TESTED — NOT SUFFICIENT. See test results below.**

## Test Results (2026-04-26)

### What the mod does
- mercenaryinfo: is_playable=1, is_controllable=1 for Damian & Oongka
- conditioninfo: removed CompleteMission gate from conditions 4294959693/4294959694

### What happened
**No effect on either save.** Tested on two saves:

1. **Chapter 1 save (characters never unlocked):** Damian and Oongka still not available in F1 wheel. No change.

2. **Post-chapter-9 save (characters were unlocked then relocked by story):** Characters still locked. Cannot use them or summon them due to mission/quest state.

### Key insight from testing
The game has a **three-phase unlock system**:
- **Phase 1 (story intro):** Characters temporarily unlock during specific story missions
- **Phase 2 (relocked):** Characters get relocked after intro missions for story reasons
- **Phase 3 (chapter 9+):** Characters permanently unlock and are available anytime

This means there's a **runtime state controller** — not just static data tables — that tracks which phase each character is in. The mercenaryinfo `is_playable` flag and conditioninfo gates are necessary but NOT sufficient. Something else is actively preventing the switch based on current quest/mission progress.

### What we still need to find
The **runtime controller** that gates character availability based on story progress. Candidates:
- **GamePlayTrigger_PlayableCharacter_*** (12 regional triggers) — blob table, not decoded
- **GamePlayVariable** entries — could track unlock phase state
- **MercenaryClanSaveData** in the save file — might have per-character lock flags
- **Quest/Mission completion state** checked at runtime — the game may check mission completion directly, not through conditioninfo
- **A hardcoded engine check** that reads save data directly

The `playmctest` debug command bypasses all of this. Understanding what it sets would solve the puzzle.

## Deep Dive Results (IDA + Parser)

### GamePlayTriggerInfo — DECODED (644 entries)

Parser: `parse_gameplaytriggerinfo.py`. Binary layout from IDA `sub_1410E0100`:

```
u32    _key
CStr   _stringKey
u8     _isBlocked
u8     field_u8_1  (triggerType? always 5 for PlayableChar, varies for others)
u8     field_u8_2  (always 1 for PlayableChar)
u8     field_u8_3  (always 0 for PlayableChar)
u32    conditionInfoKey_hash → runtime lookup in ConditionInfo dict
u32    unknown_hash → runtime lookup in another dict
3xf32  world_position (xyz coordinates of the trigger point)
u32    field_u32 (varies)
u8     field_u8_4 (radius? varies: 120-210 for PlayableChar)
u32    skillGroupInfoKey_hash → runtime lookup
CArray tagged_list (u32 count + {u8 tag + variant})
```

### The 12 PlayableCharacter Triggers → TEMPORARY STORY GATES

All 12 triggers use `PlayingMission(X)` or `PlayingQuest(X)` conditions — they check if a mission is **currently active**, NOT permanently completed. These enable character switching at specific locations DURING specific quests:

| Trigger | Location | Condition | Mission/Quest Gate |
|---------|----------|-----------|-------------------|
| Her_HalsiusHospital | -9540,576,-4168 | 0xFFFFDD89 | PlayingMission(Mission_Halsius_Yann_Meet) |
| Her_ReedDevil | -20440,1236,-9695 | 0xFFFFDD88 | PlayingMission(4 missions OR'd) |
| Her_KildenKukuWorkshop | -11241,705,-3911 | 0xFFFFDD87 | PlayingQuest(Quest_KukuBird_Kuku) |
| Her_ScholarStoneInstitute | -11848,695,-5255 | 0xFFFFDD86 | PlayingMission(6 missions OR'd) |
| Del_ClockTower | -6383,528,-2617 | 0xFFFFDD85 | PlayingMission(Mission_BloodCoronation_BastionDead) |
| Crim_EnlightenShrine | -6954,536,-1380 | 0xFFFFDD84 | PlayingQuest(5 quests OR'd) |
| Dem_HexeSanctuary | -8149,555,-1655 | 0xFFFFDD83 | PlayingQuest(Quest_Goblin_Master_Doo_Trial_Hexe) |
| Dem_JiJeongTemple | -7706,401,-4298 | 0xFFFFDD82 | PlayingQuest(Quest_Goblin_Master_Doo_Trial_JijeongTemple) |
| Del_GorthakIron | -6584,457,-3590 | 0xFFFFDD81 | PlayingMission(5 missions OR'd) |
| Del_AIMarni | -5671,535,-4340 | 0xFFFFDD80 | PlayingMission(7 missions/quests OR'd) |
| Her_GoldenFistsArena | -10745,556,-4243 | 0xFFFFDD7F | PlayingMission(Mission_GreymaneCamp_Contents_Fight) |
| Her_GreyWolfCamp | -10513,609,-4401 | 0xFFFFDD7E | PlayingMission(Mission_GreyWolf_Camp_RepairCamp_Cook) |

**Conclusion: These are NOT the permanent unlock.** They're location-specific triggers active only while playing certain quests. The permanent unlock (chapter 9+) is controlled elsewhere.

### GamePlayVariableInfo — No Character Unlock Variable

All 46 variables are construction/building projects and content gates. The closest is `GameContentOpen_Hyosi` (1000036, "combat companion feature activation") but this enables the companion system, not character switching.

### MercenarySaveData — No Playable Flag in Save

IDA binder analysis confirmed MercenarySaveData fields. **There is no `_isPlayable` field in the save data.** The save tracks: `_ownedCharacterKey`, `_isMainMercenary`, `_isInitialize`, `_isDead`, `_isBlockedAbility`, `_isHyosiMercenary`.

Save comparison (slot108 vs slot101): only 4 bytes differ (position floats). Both saves have Damian/Oongka entries.

### What's Left to Investigate

The permanent character switch availability is likely:
1. **Hardcoded in the game engine** — checks quest/mission completion directly from save data at runtime, no data table gate
2. **A specific mission key** that when CompleteMission() returns true, enables global character switching — need to identify WHICH mission
3. **Possibly in MissionInfo or QuestInfo blob data** — a "grants permanent character switching" flag on a specific quest

The `PlayingMission` conditions in the triggers give us the quest names where temporary switching works. The permanent unlock likely fires when a specific post-chapter-9 mission completes. Cross-referencing which missions complete around chapter 9 with the condition corpus could narrow it down.

## Save Transplant Attempt — FAILED (Type Index Mismatch)

Attempted to copy Damian (5495B) and Oongka (5703B) MercenarySaveData entries from slot108 into slot100. **Game crashed on load.**

Root cause: **Every type index differs between saves.**
- slot100: 71 types, `MercenarySaveData` = index 38
- slot108: 99 types, `MercenarySaveData` = index 56
- 28 types in slot108 don't exist in slot100 at all (e.g. `ItemDyeSaveData`, `SkillLearnElementSaveData`, `GamePlayVariableSaveData`)

The sentinel-based type_index fixup only catches indices adjacent to `0xFFFFFFFFFFFFFFFF` markers. Type indices embedded elsewhere in the data remain wrong.

A raw byte transplant between saves with different schemas is NOT viable. Options:
1. Build templates from scratch using target save's schema ← **THIS WORKED**
2. Add missing types to target save's schema (PARC header surgery)
3. Build a proper schema-aware PARC serializer that maps types by name, not index

## SOLUTION FOUND — Working Early Character Unlock

**Date: 2026-04-26 — CONFIRMED WORKING IN-GAME**

### What It Takes (Two Parts)

**Part 1: PAZ Overlay (group 0062) — Static Game Data**

Overlay with NONE compression via `PackGroupBuilder`, installed to game root `CrimsonDesert/0062/`:

| File | Change |
|------|--------|
| `mercenaryinfo.pabgb` | `is_controllable=1` + `is_playable=1` for Damian (0x0086-0x0087) and Oongka (0x00D8-0x00D9) |
| `mercenaryinfo.pabgh` | Unchanged companion index |
| `conditioninfo.pabgb` | Conditions 4294959693/4294959694: `CompleteMission` replaced with duplicate `CheckCharacterKey` (same 20B size) |
| `conditioninfo.pabgh` | Unchanged companion index |

**Part 2: Save Edit — Minimal MercenarySaveData Insertion**

Insert **155-byte minimal** MercenarySaveData entries for Damian and Oongka into the save's `MercenaryClanSaveData._mercenaryDataList`. Uses the same technique as mount unlocking.

Key insight: **use the simple mount template (155B)** — NOT the full 5500B entries from a late-game save. The full entries reference types that don't exist in early saves. The minimal template only uses types common to all saves, and the game populates the rest (equipment, skills, etc.) on first switch.

### Minimal Character Template (155 bytes)

Based on the simple mount base template from the save editor. Only fields:
- `_characterKey` (u32) — set to 4 (Damian) or 6 (Oongka)
- `_mercenaryNo` (u64) — unique ID (160 for Damian, 522 for Oongka)
- `_levelData` — basic level structure with 3 sub-entries
- `_isMainMercenary` (u8) — 0
- `_isInitialize` (u8) — 1
- `_occupationState` (u8) — 1

No equipment, no skills, no dye, no buffs. The game creates those when you first switch to the character.

```
Damian (155B):
0600050100300800260000ffffffffffffffff
5a0305000000000004000000a0000000000000
0001001c1a0000ffffffffffffffff7c030500
00000000010000280000ffffffffffffffff92
0305000000000004000000010000280000ffff
ffffffffffffac03050000000000040000000100
00280000ffffffffffffffffc6030500000000
000400000052000000010101010001010180000000

Oongka (155B):
0600050100300800260000ffffffffffffffff
5a03050000000000060000000a020000000000
0001001c1a0000ffffffffffffffff7c030500
00000000010000280000ffffffffffffffff92
0305000000000004000000010000280000ffff
ffffffffffffac03050000000000040000000100
00280000ffffffffffffffffc6030500000000
000400000052000000010101010001010180000000
```

### Insertion Procedure

```python
# 1. Type index fixup from reference entry in SAME save
ref_elem = merc_list_field.list_elements[-1]
ref_mbc = struct.unpack_from('<H', ref_raw, 0)[0]
ref_main_ti = struct.unpack_from('<H', ref_raw, 2 + ref_mbc)[0]
struct.pack_into('<H', template, 2 + mbc, ref_main_ti)

# 2. Fix nested type indices (sentinel-based scan)
for pos where template[pos:pos+8] == 0xFF*8 and pos >= 3:
    copy ref_nested[i] to template[pos-3]

# 3. Fix PO offsets within template
for pos where template[pos:pos+8] == 0xFF*8:
    template[pos+8:pos+12] = insert_position + pos + 8 + 4

# 4. Insert at end of _mercenaryDataList
raw[insert_pos:insert_pos] = template

# 5. Fix trailing sizes, list count, external POs
pi._fixup_trailing_sizes(...)
increment list count by 1 per entry
pi._fixup_external(...)
```

### Why This Works

1. **mercenaryinfo overlay** makes Damian/Oongka visible in the F1 character wheel
2. **conditioninfo overlay** removes the mission completion requirement
3. **Save insertion** creates the MercenarySaveData entries the game needs to track these characters
4. **Minimal templates** use only types present in ALL saves (MercenarySaveData + basic sub-types) — no schema mismatch
5. **The game auto-populates** equipment, skills, and other data when you first switch to the character

### Why Previous Attempts Failed

| Attempt | Why It Failed |
|---------|---------------|
| mercenaryinfo overlay alone | Save had no MercenarySaveData entries for Damian/Oongka |
| conditioninfo overlay alone | F1 wheel hidden (is_playable=0), no save entries |
| Both overlays together | Save entries still missing |
| Full 5500B save transplant | Type index mismatch — slot108 has 99 types, slot100 has 71, indices all different |
| Minimal 155B insertion + overlays | **WORKS** — same types as existing save entries |

### Files

- `mod_early_character_unlock.py` — conditioninfo patcher + overlay builder
- `parse_gameplaytriggerinfo.py` — decoded GamePlayTriggerInfo parser (644 entries)
- `output/early_character_unlock/` — built overlay files + templates
- `howtoapplymodoverlay.md` — overlay installation reference
- `MERCENARY_SAVE_FIELDS.md` — IDA-decoded MercenarySaveData field map

## Mod Script

`mod_early_character_unlock.py` — builds patched conditioninfo, outputs to `output/early_character_unlock/`.
Mercenaryinfo patching done inline (4 byte flips at known offsets).

## Tools Used

| Tool | Purpose |
|------|---------|
| `parse_conditioninfo.py` | conditioninfo round-trip parser (8934 entries) |
| Ship-It `crimson-rs 1.0.4.x` | mercenaryinfo struct definition, 122 table parsers |
| `crimson_rs.PackGroupBuilder` | PAZ overlay packing (NONE compression) |
| `crimson_rs.extract_file` | Extract vanilla pabgb from game archives |
| `conditioninfo_104_mapped.json` | Decoded condition corpus |

## Key Reference Files

- `tools/Ship-It/crimson-rs-1.0.4.x/src/tables/mercenary_info/info.rs` — MercenaryInfo struct
- `tools/Ship-It/crimson-rs-1.0.4.x/src/binary/variants/condition_data.rs` — 405 ConditionData variants
- `tools/pabgb_toolkit/decoded_tables/conditioninfo_104_mapped.json` — All 8934 conditions decoded
- `tools/pabgb_toolkit/decoded_tables/conditioninfo_104_bytecode_corpus.json` — 229 expression functions
- `howtoapplymodoverlay.md` — Canonical overlay installation procedure
- `tools/Ship-It/supported_tables.txt` — All 122 pabgb tables Ship-It supports
