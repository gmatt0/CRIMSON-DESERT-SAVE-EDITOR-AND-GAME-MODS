# CrimsonGameMods — Local vs GitHub Diff

Date: 2026-04-28
Local branch: `StandAloneSaveEditor`
GitHub remote: `gamemods/main` (NattKh/CRIMSON-DESERT-SAVE-EDITOR-AND-GAME-MODS)
Total: 130 files changed, +44,518 / -358,136 lines

## New Files (local only, not on GitHub)

| File | Lines | Purpose |
|------|-------|---------|
| `characterinfo_parser_v2.py` | 1,489 | IDA-derived characterinfo roundtrip parser |
| `CharacterStartingGearHowtoChange.md` | — | Starting gear research doc |
| `QuestCharacterUnlock_Research.md` | — | Quest start_player_list research |
| `MERCENARY_INSERTION_GUIDE.md` | — | MercenarySaveData insertion procedure |
| `Character unlock Gates.md` | — | Character unlock research narrative |
| `mod_quest_char_unlock.py` | — | Quest character unlock mod (overlay 0063) |
| `mod_early_character_unlock.py` | — | Mercenary + condition overlay (overlay 0062) |
| `parse_conditioninfo.py` | — | Conditioninfo roundtrip parser |
| `parse_gameplaytriggerinfo.py` | — | GamePlayTriggerInfo parser (644 entries) |
| `howtoapplymodoverlay.md` | — | PAZ overlay installation reference |
| `_setup_yahn_like_kliff.py` | — | Test: set up Yahn as playable character |
| `_insert_yahn.py` | — | Test: insert Yahn MercenarySaveData |

## Modified Files

| File | Change | Details |
|------|--------|---------|
| `mercenaryinfo_parser.py` | +34 | **Fixed**: added 4 missing fields (combat_targeting_flags, is_playable, parent_mercenary_group_info, hired_skill_info_list). Was causing roundtrip mismatch. |
| `gui/tabs/mercpets.py` | +138 | **Added**: "Set Summon Limit" button + spinbox, exposed `is_playable` checkbox, added to _DIFF_FIELDS for export/import |
| `gui/main_window.py` | +112/-112 | **Unhid** MercPets tab (removed experimental_mode gate), renamed "MercPets (dev)" to "MercPets" |
| `gui/tabs/buffs_v319.py` | +956/-956 | Various changes (large diff) |
| `main.py` | +4/-4 | Minor |
| `armor_catalog.py` | +10/-10 | Minor |
| `updater.py` | +2/-2 | Minor |
| `data/item_names.json` | ~84K | Updated item name database |
| `splash.png` | binary | Updated splash image |

## Deleted Files (were on GitHub, removed locally)

### Large JSON mod files (user-created mods, not source code)
- `enable.field.json` (174,770 lines)
- `everything in one.json` (35,402 lines)
- `enableeverything.json` (35,131 lines)
- `My ItemBuffs Config.json` (8,351 lines)
- `packs/imbue and QoL with damage increase.json` (20,723 lines)
- `skill_inf_stamina_mod.field.json` (2,568 lines)
- `Mount Everywhere.json` (1,523 lines)
- `kliff using damian.json` (111 lines)
- `stamina_mods/*.json` (5 files × 3,706 lines each)
- `lemonheads-UnlimitedDragonFlying-v3.0.json` (67 lines)
- `packs/Mid Slayer.json` (362 lines)
- Various pack modinfo.json files

### Removed source files
- `gui/tabs/mod_loader.py` (1,080 lines) — ModLoader tab
- `gui/tabs/iteminfo_inspector.py` (1,300 lines) — ItemInfo Inspector tab
- `gui/tabs/dmm_webview.py` (329 lines) — DMM WebView tab
- `gui/add_to_save_dialog.py` (389 lines) — Add-to-save dialog
- `launcher.py` (134 lines) — Launcher
- `bundle_unified.py` (196 lines) — Unified bundler
- `universal_pabgb_parser.py` (579 lines) — Universal parser
- `pabgb_parser_local.py` (412 lines) — Local parser
- `actionchart_descriptor.py` (244 lines) — Action chart
- `stringinfo_resolver.py` (94 lines) — String resolver
- `iteminfo_housing_parser.py` (45 lines) — Housing parser
- `tools/pabgb_auto_decoder.py` (766 lines) — Auto decoder
- `crimson_rs/` directory (entire module — __init__, enums, pack_mod, create_pack, validate_game_dir, legacy, .pyd files)

### Removed documentation
- `README.md`, `BUILD_UNIFIED.md`, `MODDING_GUIDE.md`
- `CHANGELOG_v1.0.3.md`, `CHANGELOG_v1.0.4.md`, `CHANGELOG_v1.0.8.md`, `CHANGELOG_v1.0.9.md`
- `FIELD_JSON_V3_SPEC.md`, `STACKER_OUTPUT_FORMATS.md`
- `INTEGRATION_HANDOFF.md`, `INTEGRATION_STATUS.md`
- `ITEMBUFFS_FEATURE_AUDIT.md`, `MOD_COMPATIBILITY_PROBLEM.md`
- `COMPATIBILITY_DISCUSSION.md`, `CRIMSON_RS_DUAL_PARSER_TECHNICAL_DOC.md`
- `HANDOVER_CUSTOM_ITEM_CREATOR.md`, `HANDOVER_NEXT_SESSION.md`, `HANDOVER_SKILLTREE_EDITOR.md`
- `OPTION_D_INTEGRATION_PLAN.md`, `STACKER_ITEMBUFFS_INTEGRATION.md`
- `WHY_NOT_JUST_EXPORT_JSON.md`, `WHY_WE_PIVOTED.md`
- `TODO_CROSS_CHARACTER_EQUIP.md`, `NEXUS_POST_v1.0.1.md`
- `JMM_USERS_GUIDE.md`, `PABGB_DECODE_PROCESS.md`, `SESSION_STATUS_20260423.md`

### Removed binary/build artifacts
- `CrimsonGameMods.exe` (73MB)
- `version.dll` (698KB)
- `crimson_data.db` (32MB)
- `CrimsonGameMods.spec`, `CrimsonCLI.spec`, `build.bat`, `clear_cache.bat`
- `_new_iteminfo.pabgb/pabgh`, `_new_equipslotinfo.pabgb/pabgh`
- `_skill_pabgb.bin`, `_skill_pabgh.bin`
- `game_baselines/` (skill.pabgb/pabgh for 1.0.0.3 and 1.0.0.4)
- `packs/*/files/gamedata/binary__/client/bin/*.pabgb` (multiple)
- `tools/test_lightning_unlock.zip`
- `editor_version_gamemods.json`

### Removed test/trace scripts
- `_test_custom_item.py`, `_test_full_custom_item.py`, `_test_parse.py`
- `_test_stacker_inspector.py`, `_test_swap_store_item.py`
- `_trace2.py`, `_trace3.py`, `_trace_item.py`
- `_analyze_accessory_mod.py`, `_deploy_all.py`, `_find_insertions.py`

## Summary

The local branch is a **cleaned-up fork** of the GitHub main — large JSON mods, binary artifacts, removed tabs (ModLoader, Inspector, DMM WebView), and old documentation have been stripped. New additions are the character unlock/quest system (parsers + mod scripts + research docs) and mercenaryinfo parser fixes.
