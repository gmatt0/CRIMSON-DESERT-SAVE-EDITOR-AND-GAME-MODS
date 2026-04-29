# CrimsonGameMods v1.1.3 Changelog

**Date**: 2026-04-25 22:24 CDT
**Branch**: StandAloneSaveEditor

---

## ShadowfeindX Fork Cherry-Picks

Reviewed fork at `ShadowfeindX/CRIMSON-DESERT-SAVE-EDITOR-AND-GAME-MODS`. Cherry-picked additive features, rejected regressions. Full review at `FORK_REVIEW_ShadowfeindX.md`.

- **Buff-to-item index** (`iteminfo_index.py`) — new `buff_to_items` dict mapping buff IDs to items, with `log.info` instead of debug prints
- **find_similar() expanded** — `"passives"` and `"buffs"` modes for finding items sharing a specific passive or buff
- **Context menu: "Show items with this passive/buff"** — right-click passive or buff row in stats table
- **Context menu: "With same passives / With same buffs"** — in Find Similar submenu on item table
- **Context menu: "Dump item info to disk"** — export single item's full JSON
- **Max Stacks preset** — one-click button + `_ITEM_PRESETS["max_stacks"]` entry
- **`_safely_replace_buff_item()`** — safe dict replacement helper
- **Import ITEMINFO** — load dumped item JSON back into editor with validation
- **DEV Ring preset buttons** — collapsible grid (Immunity, STR/HP, DEF/HP, MP/Stam, Speed, All DEV, Elemental, Jump Boots), replaces dead combo-box code
- **`_eb_apply_preset` fix** — `preset.get('gimmick_info', 'unchanged')` prevents KeyError on presets without gimmick
- **`_eb_god_mode(skip=True)`** — eliminates double-confirmation when called from God Mode preset button
- **Duplicate socket row removed** — stale copy in presets section deleted, canonical copy in Sockets group retained
- **`_eb_status` → `_buff_status_label`** — 6 cross-tab calls migrated to bottom-bar label (preset apply, effect catalog, gimmick, drop enchant, sockets) so feedback is visible when fired from Presets tab

## Collapsible UI Bars

- **`_make_collapsible()`** — reusable instance method with gold accent `▾`/`▸` toggle, persists open/closed state to config
- **Notice bar** — collapsible (config key: `buffs_show_notice`)
- **Actions bar** — collapsible (config key: `buffs_show_actions`)
- **Search bar** — collapsible (config key: `buffs_show_search`)
- **DEV Ring Presets** — collapsible (config key: `buffs_show_dev_presets`)
- **Game path bar** — `▲`/`▼` button replaces cryptic "X", state saved to `show_gamepath_bar` config, restored on startup
- **View > Show / Hide Panels > Game Path Bar** — menu toggle synced with button

## Stacker Tab Navigation Fix

- `_goto_stacker_legacy_export()` — replaced fragile parent-walking code with `navigate_requested.emit("stacker")` signal
- `_on_tab_navigate_requested()` in `main_window.py` — added `"stacker"` selector that finds `_stacker_tab` by reference and switches `_mods_tabs` directly
- Tab now actually switches visually

## Universal Proficiency + Kliff Gun Fix Streamline

- **`_stage_kliff_gun_fix()`** — standalone method that extracts characterinfo.pabgb, applies 2-field copy (Damian upper action chart + Oongka gameplay data to Kliff), stages as `_staged_charinfo_files`
- **Integrated into UP v2** — after tribe_gender + equipslotinfo, prompts "Apply Kliff Gun Fix now?"
- **Integrated into Enable Everything** — same prompt after UP v2 step
- **Apply to Game** — bundles staged charinfo files into overlay alongside iteminfo and skill files
- **Export as Mod / CDUMM Export** — also bundles staged charinfo
- **Restore** — clears `_staged_charinfo_files`, confirmation dialog shows Kliff Gun Fix status

## Abyss Gear Unlock

- **`_eb_unlock_all_abyss_gear()`** — sets `equipable_hash = 0` on all AbyssGear items (192 restricted, 293 total)
- **Field-name based** — survives game updates, auto-catches new abyss items
- **"Unlock All Abyss Gear" button** in Global Mods > Apply to All Items
- **Wired into Enable Everything** — step 3b between sockets and UP v2
- **Stacker detection** — `abyss_unlocked` / `abyss_total` in pull summary
- **Credit**: OhmesmileTH (Nexus Mods) for discovering `_equipableHash = 0` technique. Re-implemented as field-name mod that stacks with everything.

## 100% Socket Coverage

- **`_socketable_force_target()` simplified** — returns `True` for ANY equippable item with `drop_default_data` + `equip_type_info`, regardless of category
- **3051/3051 equippable items** covered (was 647 extend + 304 force = 951, now all 3051)
- **Covers**: daggers (Goblin King's Treasure Dagger 12900), masks (Kliff_Mask 1000806), glasses (Master Du's Circlet 1000479), pirate hats (1000771), health devices (1001236), all armor, all weapons
- **Lantern + Bracer** added to `_FORCE_SOCKET_CATEGORIES`
- **Daeil_Band** (Axiom Bracelets) added to `_FORCE_SOCKET_STRING_KEYS`

## SkillTree Legacy JSON Export Fix

- **Root cause**: `rel_offset` and `offset` were computed from byte 0 of `serialize_entry()` output (includes key + name_len + name + null terminator). Standard PABGB convention (CrimsonWings/DMM/JMM) measures from after key + name_len + name (null is body byte 0, not header).
- **Fix**: diff loop starts at `hdr_size = 4 + 4 + name_len`, `rel_offset = byte_pos - hdr_size`
- **Verified**: all 277 CrimsonWings reference offsets match exactly
- **Button re-enabled**: `_btn_skill_export_legacy` added to layout (was created but never `addWidget`'d)

## `_is_admin()` → `_can_write_game_dir()` Fix

- **Root cause**: `ctypes.windll.shell32.IsUserAnAdmin()` returned `False` even when user had write access to game directory (Steam doesn't require admin). Apply to Game silently returned after showing warning.
- **Fix**: replaced all 5 `_is_admin()` gates with `_can_write_game_dir()` which tests actual write access via temp file
- **Affects**: Apply to Game, Restore Original, Reset Vanilla PAPGT, Blackberry Test, Max Stacks legacy

## PAPGT Surgical Restore

- **Root cause**: `.vanilla` PAPGT backup was taken after other tools (DMM, FieldEdit, SkillTree) had written entries. Restoring from it reintroduced references to deleted directories, crashing the game.
- **Fix**: "Restore Original" now surgically removes only ItemBuffs entries from current PAPGT, then prunes any entries pointing to missing directories
- **"Reset to Vanilla PAPGT"** also prunes dead references after restoring from backup
- **Restore summary** — shows which folders were removed and what features they contained (iteminfo, Kliff Gun Fix, equipslotinfo, etc.)

## Item Creator Improvements

- **"Stage Item" button** — pushes custom item into `_buff_rust_items` in memory, no deployment. User clicks Apply to Game to deploy alongside all other edits. Replaces old "Apply to Game (New Item)" which clobbered existing overlays.
- **"Deliver via Money Bag" button** — stages iteminfo into memory + deploys dropsetinfo overlay (0036) with donor key replacing coins in dropset 400002 (Copper Money Bag) at 100% rate. User opens copper pouch in-game to receive item. No save editing required.
- **"Swap to Vendor" removed** — did not work reliably
- **Export as Single-Item Mod** — unchanged

## AbyssGearUnlocker.field.json Fix

- **Root cause**: Stacker conversion captured vanilla restriction hash values as the `"new"` value instead of 0. Every intent was a no-op.
- **Fixed**: regenerated with all 189 intents correctly setting `equipable_hash` to 0

## Misc

- `editor_version_gamemods.json` bumped to v1.1.3
- `TODO_FUTURE_FEATURES.md` — Stacker as Central Deploy Hub consolidation plan documented
- `FORK_REVIEW_ShadowfeindX.md` — full regression report for fork author
- Unused `import ctypes` removed from buffs_v319.py
