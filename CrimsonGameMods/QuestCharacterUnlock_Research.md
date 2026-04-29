# Quest Character Unlock — Research Notes

Date: 2026-04-28

## Summary

We patched `questinfo.pabgb` field `start_player_list` to allow all 3 characters
on all 72 character-restricted quests. The mod WORKS — quests no longer kick you
out or force a character swap. However, cutscenes still spawn the original character
(e.g. Kliff) and the camera follows them instead of the active player character.

**Conclusion:** `start_player_list` controls quest ACCESS, not cutscene casting.
Cutscene character assignments are likely in StageInfo's `_sequencerDesc` or a
separate sequencer pabgb.

## Quest Data Structure (from dmm-parser quest_info/info.rs)

35 fields total. Parser: Python reimplementation of the Rust struct, verified
905/905 entries parse clean with 0 failures.

### Typed Fields (1-28, fully parseable)

| # | Field | Type | Notes |
|---|-------|------|-------|
| 1 | key | u32 | QuestKey |
| 2 | string_key | CString | e.g. "Quest_Intro" |
| 3 | is_blocked | u8 | |
| 4 | quest_type | u8 | 1=?, 2=standard |
| 5 | quest_category | u8 | 0=side, 12=region, 13=main story |
| 6 | name | LocalizableString | display name |
| 7 | desc | LocalizableString | description |
| 8 | quest_group_info | u16 | QuestGroupKey |
| 9 | faction_info | u32 | FactionKey hash |
| 10 | faction_state_data | FactionStateData | CArray\<u8\> + u32 + u32 + u8 |
| 11 | branch_data | BranchData | 18B fixed: quest_key + cond_key + u8 + u8 + u32 + u32 |
| 12 | **start_player_list** | CArray\<u32\> | **CharacterKey list — controls who can play** |
| 13 | branch_data_list | CArray\<BranchData\> | condition-gated quest branches |
| 14 | executor_quest_list | CArray\<u32\> | QuestKey hashes |
| 15 | gauge_list | CArray\<u32\> | QuestGaugeKey |
| 16 | mission_list | CArray\<u32\> | MissionKey hashes |
| 17 | stage_list | CArray\<u32\> | StageKey hashes |
| 18 | start_mission | u32 | MissionKey |
| 19 | start_stage | u32 | StageKey |
| 20 | stage_icon_path | u32 | StringInfoKey |
| 21 | stage_text_icon_path | u32 | StringInfoKey |
| 22 | stage_image_path | u32 | StringInfoKey |
| 23 | playable_mission_count | u32 | |
| 24 | playable_stage_count | u32 | |
| 25 | test_tag | CString | |
| 26 | game_start_stage | u32 | StageKey |
| 27 | game_start_sub_timeline | CString | |
| 28 | memo | CString | |

### Blob + Trailing Fields (29-35)

| # | Field | Type | Notes |
|---|-------|------|-------|
| 29 | quest_dialog_filter_data_list | blob | Polymorphic CArray, captured as raw bytes |
| 30 | dialog_must_mission_info_list | CArray\<u32\> | MissionKey list |
| 31 | npc_dialog_must_condition | u32 | ConditionKey |
| 32 | is_save | u8 | |
| 33 | is_continuous_mission | u8 | |
| 34 | is_repeatable | u8 | |
| 35 | debug_color | u32 | |

## start_player_list Analysis (905 quests)

### Distribution

| List Contents | Count | Meaning |
|---------------|-------|---------|
| Empty `[]` | 833 | No character restriction (side content, shops, schedules, etc.) |
| `[1]` Kliff only | 65 | Story boss fights, camp tutorials, faction quests |
| `[4]` Damiane only | 3 | PistolShot minigame, AnamorphicSword, BloodCoronation_WitchDukeAndDream |
| `[6]` Oongka only | 1 | Quest_Chase_TraitorDwayne |
| `[1, 6]` Kliff+Oongka | 2 | Armwrestling, Handwrestling |
| `[1, 4]` Kliff+Damiane | 1 | Duel_MainWeapon |

### Category 13 = Main Story (39 of 72 restricted quests)

All main story/boss quests use category 13 and have explicit character restrictions.
Examples:
- `Quest_Intro` (10001) → `[Kliff]`
- `Quest_Epilogue_Ending` (1000358) → `[Kliff]`
- `Quest_Chase_TraitorDwayne` (1000009) → `[Oongka]`
- `Quest_BloodCoronation_WitchDukeAndDream` (1000180) → `[Damiane]`
- `Quest_GreyWolf_Camp` (11006000) → `[Kliff]`

### Empty List Quests (833)

These are NOT main story. Breakdown:
- 207 system/functional quests (group 9999) — `Func_LevelSequencerSpawn`, etc.
- 58 sequencer/cutscene quests (group 8600)
- 38+ shop quests (group 8000+)
- Challenges, schedules, side content, faction nodes

`Func_CD_MainStroy` (key=1000792) has an EMPTY list — it's a meta-quest controller,
not a playable quest.

## Quest_Intro Structure

```
Quest_Intro (key=10001):
  quest_type: 2, quest_category: 13, quest_group: 1000
  start_player_list: [1] (Kliff)
  branch_data_list: [{quest_key: 1000123 (Quest_IntroHernand), cond_key: 0}]
  executor_quest_list: [1000792 (Func_CD_MainStroy)]
  mission_list: [1000157 (Mission_Intro_Tutorial_I), 1000160 (Mission_Intro_MainBattle)]
  start_mission: 1000157
  stage_list: 16 stages
```

## MissionInfo Structure (from dmm-parser)

Typed prefix only (4 fields), rest is blob tail:

| Field | Type |
|-------|------|
| key | u32 |
| string_key | CString |
| is_blocked | u8 |
| parent_quest | u32 |

Tail blob contains (from IDA Korean error strings):
`_subMissionList`, `_executeStageList`, `_branchMissionList`, `_startPlayerList`,
`_fieldReviveList`, `_giveUpFieldReviveList`, `_triggerVolumeData`, **`_rewardList`**,
**`_resultDataList`**, `_rewardInventoryKey`, `_uiDesc`, ... 50+ more fields.

**Note:** MissionInfo also has `_startPlayerList` in its blob tail. Not parsed yet.

## StageInfo Analysis (50,463 entries, 25MB)

Typed prefix: key, string_key, is_blocked, name, stage_desc, complete_log.
Blob tail contains `_startPlayerList`, `_forbiddenCharacterList`, `_sequencerDesc`,
and 40+ more fields.

### Character Key Scan Results (heuristic — scanned blob for CArray\<u32\> patterns)

Only 74 out of 50,463 stages have character key arrays:

| Combination | Occurrences | Example |
|-------------|-------------|---------|
| `[Kliff]` | 89 | Dragon_Block_Lv1, Goblin_Master_Meet |
| `[Damiane]` | 29 | GreyWolf_Camp_RepairCamp stages |
| `[Kliff, Damiane]` | 10 | GreyWolf_Camp_RepairCamp stages |
| `[Oongka]` | 8 | Dwayne_Boss_Oongka_I |
| `[Dragon/Blackstar]` | 3 | Caliburn_Boss_MusketSiege stages |

### Multi-Array Stages (revealing `_startPlayerList` + `_forbiddenCharacterList`)

GreyWolf_Camp stages consistently have TWO arrays at different offsets:
- `[Kliff, Damiane]` — likely `_startPlayerList`
- `[Damiane]` — likely `_forbiddenCharacterList` or second restriction

`BloodCoronation_Azerian_Dead` has THREE arrays: `[Kliff]`, `[Damiane]`, `[Kliff]`

### Rokade NOT in StageInfo

Rokade (key=1003120) was not found in any stage entry's character key arrays.
Horses are auto-granted at the MercenarySaveData level, not stage-gated.

## Condition Branch Keys (from quest branch_data)

Top conditions referenced by quest branches:
- `0xFFFFE4EE` (4294960366): 6 quests
- `0xFFFFE4EF` (4294960367): 3 quests
- Various others with 1-2 references each

These are conditioninfo keys that gate quest branching decisions.

## The Cutscene Problem

When playing as Damiane/Oongka on a Kliff quest, the quest STARTS fine (no kick,
no force-swap). But cutscenes still spawn the original character and lock the
camera to them. The active player character stays in the scene but without camera
control.

### Where cutscene casting likely lives

- **StageInfo._sequencerDesc** — polymorphic `SequencerStageChartDesc` family,
  stride 232B, the FIRST field in the blob tail. This likely defines which
  characters appear in each stage's cutscene.
- **Sequencer pabgb tables** — group 8600 quests (58 entries with names like
  `cd_seq_05_content_doc_m05_m04_animal_01`) are cutscene sequencers.
- **GlobalStageSequencerInfo** — another sequencer table.

### Next steps to fix cutscenes

1. Decode `_sequencerDesc` in StageInfo (polymorphic, complex)
2. OR find character references in sequencer entries and swap them
3. OR look for a character-substitution system (the game already does this
   for the GreyWolf_Camp stages where both Kliff+Damiane appear)

## Mod Files

| File | Purpose |
|------|---------|
| `mod_quest_char_unlock.py` | Patches start_player_list on all 72 restricted quests → `[1, 4, 6]` |
| `mod_early_character_unlock.py` | Patches mercenaryinfo + conditioninfo for F1 wheel unlock |
| `MERCENARY_INSERTION_GUIDE.md` | Save-level MercenarySaveData insertion |

### mod_quest_char_unlock.py overlay

- Group: `0063`
- Tables: `questinfo.pabgb` + `questinfo.pabgh`
- Compression: NONE (via PackGroupBuilder)
- Changes: 72 entries patched, +564B growth (CArray expansion)
- Install: game root `CrimsonDesert/0063/`
- Revert: `python mod_quest_char_unlock.py --game-dir "..." --revert`

## Binary Format Reference

```
CString     = u32 length + length bytes (NO null terminator)
CArray<T>   = u32 count + count × T
LocalizableString = u8 category + u64 index + CString default
BranchData  = u32 quest_key + u32 cond_key + u8 + u8 + u32 + u32 (18B fixed)
FactionStateData  = CArray<u8> + u32 + u32 + u8
```

Source: `tools/dmm-parser-main/src/tables/quest_info/info.rs` (Rust struct definition,
roundtrip-verified against vanilla questinfo.pabgb).
