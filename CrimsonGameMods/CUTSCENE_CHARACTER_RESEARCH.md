# Cutscene Character Assignment — Research Notes

Date: 2026-04-28

## Goal

Figure out what controls which character (Kliff/Damian/Oongka) appears in cutscenes
and minigames (armwrestling, etc.). If we can swap the character, we can make a
"Play as X" mod where you play the entire game as Damian or Oongka instead of Kliff.

## What We Know Works

- Quest `start_player_list` controls quest ACCESS (who can start the quest)
- We patched all 72 restricted quests to `[1, 4, 6]` — all 3 characters can enter
- **Result:** Quest starts fine as non-Kliff BUT cutscenes still spawn Kliff and
  lock camera to him. The active player character stays in the scene without camera.

## F1 Character Wheel — HARDCODED

Exhaustive search of all 121 pabgb tables. The F1 wheel character list (keys 1, 4, 6)
is NOT defined in any pabgb table. It is hardcoded in the game binary.

### Tables searched and ruled out

| Table | What it actually controls |
|-------|--------------------------|
| `reserveslot.pabgb` | Item/mount/skill radial menus. No character slot type. |
| `mercenaryinfo.pabgb` | Summon limits and playable/controllable per TYPE (not per character) |
| `conditioninfo.pabgb` | Per-character conditions (CheckCharacterKey). Referenced but not the wheel definition. |
| `charactergroupinfo.pabgb` | NPC spawn groups (patrols, factions, citizens). 484 entries. |
| `gameeventhandler.pabgb` | UI events (tutorials, cosmetics). No wheel control. |
| `sublevelinfo.pabgb` | Stat progression (HP, skill points, contribution). Uses condition keys for gating. |
| `gameplaytrigger.pabgb` | 12 regional PlayableCharacter triggers (temporary, during specific quests) |
| `gameplayvariableinfo.pabgb` | Construction/building projects. No character variables. |
| `multichangeinfo.pabgb` | Equipment visual changes per enchant level. 17,209 entries. |
| `sequencerspawninfo.pabgb` | Environmental spawns (birds, animals, faction NPCs). |
| `globalstagesequencerinfo.pabgb` | Global sequencers (loading screens, minigames, etc.) |

### Evidence for hardcoded

- Yahn (key=2) was set up identical to Kliff: MercenarySaveData in save,
  conditioninfo CheckCharacterKey(Yahn), characterinfo _spawnActorType=1,
  mercenaryinfo type 1 is_playable=1. Game loads fine, no crash, but Yahn
  does NOT appear in the F1 wheel.
- No pabgb table contains "CharacterWheel", "CharacterSlot", "CharacterSelect"
  or any equivalent entry name.
- String scan of "Playable" only found gameplaytrigger (regional triggers) and
  fieldlevelnametableinfo (label).

## Cutscene Character Assignment — WHERE IT LIVES

### stageinfo.pabgb — `_sequencerDesc` (polymorphic, in blob tail)

StageInfo is 25MB with 50,463 entries. The typed prefix covers 6 fields
(key, string_key, is_blocked, name, stage_desc, complete_log). The blob tail
has 50+ fields including:

- `_sequencerDesc` — SequencerStageChartDesc family, polymorphic, stride 232B.
  This is the FIRST field in the blob tail and likely defines which characters
  appear in each stage's cutscene/sequence.
- `_startPlayerList` — who can play this stage (CArray<u32> of character keys)
- `_forbiddenCharacterList` — who is blocked from this stage

Only 74 out of 50,463 stages have character key arrays (from heuristic scan):
- `[Kliff]`: 89 hits
- `[Damiane]`: 29 hits
- `[Kliff, Damiane]`: 10 hits
- `[Oongka]`: 8 hits
- `[Dragon/Blackstar]`: 3 hits

### globalstagesequencerinfo.pabgb — Transition animations

71 entries defining system-level sequencers:
- `FocusCharacterChange` → `cd_change_character_00` (F1 wheel transition animation)
- `Loading` entries with character-specific loading screens:
  - `cd_common_abyssoneloading_01` (Kliff, default)
  - `cd_common_abyssoneloading_01_damian`
  - `cd_common_abyssoneloading_01_oongka`
- Minigames: Fishing, Rodeo, MilkingCow, SlapFight
- Skills: PlayerBehaviorStage_Skill_* (sword, shield, bow learning animations)

### The cutscene character is likely determined by:

1. **stageinfo._sequencerDesc** — polymorphic blob defining the cutscene
   sequence, which references character keys for who to spawn/focus
2. **The `.road` files** — sequencer road files in the PAZ archives that
   define cutscene timelines. These reference character assets by name.
3. **characterinfo._spawnActorType** — type 1 (player) vs type 4 (companion)
   affects how the game treats the character in sequences

## What We Need To Decode

To make a "Play as X" mod, we need to understand `_sequencerDesc` in stageinfo.
This polymorphic field defines each cutscene's character cast. If we can:

1. Parse `_sequencerDesc` to find character key references
2. Swap Kliff (key=1) with Damian (key=4) or Oongka (key=6)
3. Rebuild stageinfo as an overlay

...then every cutscene would use the chosen character instead of Kliff.

### Difficulty

- `_sequencerDesc` is a polymorphic SequencerStageChartDesc family
- dmm-parser doesn't decode it (marked as blob)
- IDA decompile function is `sub_141D8C6D0` (deeply nested)
- StageInfo is 25MB — any overlay would be large

### Alternative approach

Instead of decoding the full polymorphic struct, we could:
1. Heuristically scan each stage entry's blob for character key u32 values
2. Swap `01 00 00 00` (Kliff) with `04 00 00 00` (Damian) at those positions
3. This is RISKY — u32 value 1 appears everywhere as counts, flags, etc.
4. Would need careful filtering (only swap at positions that are actually
   character key references)

## Tables Referenced Per Character (String Name Scan)

Files containing ALL THREE character name strings:

| File | Kliff | Damian | Oongka | Purpose |
|------|-------|--------|--------|---------|
| aidialogstringinfo | 20 | 21 | 21 | Dialog strings |
| characterinfo | 6 | 2 | 4 | Character definitions |
| conditioninfo | 52 | 15 | 41 | Condition expressions |
| dialogvoiceinfo | 2 | 1 | 1 | Voice acting config |
| dropsetinfo | 9 | 11 | 11 | Loot tables |
| gameadviceinfo | 2 | 3 | 3 | Tutorial advice |
| gameeventhandler | 3 | 3 | 3 | UI events (glasses, backpack, tutorials) |
| gimmickinfo | 17 | 19 | 6 | Gimmick/interactive objects |
| itemgroupinfo | 77 | 1 | 26 | Item groups |
| iteminfo | 20 | 27 | 29 | Items (weapons, armor) |
| knowledgeinfo | 8 | 98 | 112 | Knowledge entries |
| missioninfo | 7 | 5 | 12 | Mission definitions |
| multichangeinfo | 123 | 333 | 283 | Equipment visual changes |
| skill | 5 | 88 | 99 | Skill definitions |
| skilltreegroupinfo | 5 | 4 | 4 | Skill tree groups |
| skilltreeinfo | 8 | 6 | 6 | Skill trees |
| stageinfo | 4 | 13 | 16 | Stage definitions |
| stringinfo | 29 | 194 | 190 | Localized strings |
| sublevelinfo | 1 | 1 | 1 | Stat progression |
| uimaptextureinfo | 1 | 1 | 1 | Map UI textures |

## Condition Key Cross-References

Damian condition (0xFFFFE24D = 4294959693) and Oongka condition
(0xFFFFE24E = 4294959694) appear in only 2 pabgb files:
- `conditioninfo.pabgb` — where they're defined
- `sublevelinfo.pabgb` — SkillPoint_Damian/SkillPoint_Oongka entries

Kliff condition (0xFFFFF714 = 4294967060) appears in:
- conditioninfo, questinfo (6), missioninfo (3), npcinfo (3),
  aieventtableinfo (3), characterinfo (1), itemuseinfo (1),
  knowledgeinfo (2), uimaptextureinfo (1)

## gameeventhandler Character Entries

| Key | Name | Type | What it does |
|-----|------|------|-------------|
| 17997 | Control_Oongka_Rocket_BackPack | 106 | Oongka's jetpack/rocket backpack control |
| 18009 | Information_Advice_Play_Oongka | 15 | Tutorial popup when first playing Oongka |
| 18010 | Information_Advice_Play_Damian | 12 | Tutorial popup when first playing Damian |
| 18102 | Control_Kliff_Glasses | 106 | Kliff's glasses cosmetic control |
| 18103 | Control_Kliff_Mask | 106 | Kliff's mask cosmetic control |
| 18133 | Information_Advice_Play_Oongka_Guide | 89 | Oongka play guide |
| 18136 | Information_Advice_Play_Damian_Guide | 89 | Damian play guide |
| 18137 | Information_Advice_Play_Damian_Out | 12 | Damian leave/dismiss event |
| 18167 | Control_Kliff_Glasses_Window | 0 | Kliff glasses window UI |

## Next Steps for "Play as X" Mod

The key question is: **can we swap which character appears in cutscenes?**

Approach 1 — Decode stageinfo._sequencerDesc:
- Hard. Polymorphic family, 232B stride, deeply nested.
- Would give full control over cutscene character casting.

Approach 2 — Binary swap in stageinfo blob:
- Scan stage entry blobs for character key patterns.
- Find entries where key=1 (Kliff) is referenced as a character (not count/flag).
- Need a reliable way to distinguish character keys from other u32=1 values.
- The _startPlayerList and _forbiddenCharacterList positions we already found
  (via heuristic scan) could serve as anchor points.

Approach 3 — Character key swap at characterinfo level:
- Swap Kliff's characterKey with Damian's in characterinfo.
- The game would treat "Kliff" as "Damian" everywhere.
- Risk: equipment, skills, tribe hashes all differ.

Approach 4 — Save-level character swap:
- In the save file, swap the _characterKey in MercenarySaveData.
- Make the "Kliff" entry actually be Damian's character key.
- The game spawns Damian's model where Kliff would be.
- Risk: save corruption if the game expects specific data per key.

## Files

| File | Purpose |
|------|---------|
| `mod_quest_char_unlock.py` | Quest start_player_list patcher (overlay 0063) |
| `mod_early_character_unlock.py` | Condition + mercenary overlay (overlay 0062) |
| `_setup_yahn_like_kliff.py` | Test: set up Yahn as playable (proved F1 wheel is hardcoded) |
| `QuestCharacterUnlock_Research.md` | Quest system research |
| `CharacterStartingGearHowtoChange.md` | Starting gear analysis |
| `MERCENARY_INSERTION_GUIDE.md` | Save-level character insertion |
| `Character unlock Gates.md` | Original character unlock research |
