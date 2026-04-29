# Session Handover — 2026-04-24 / 2026-04-25

## What Was Done

### v1.1.0 Release
- Updated crimson_rs to 1.0.4.1 (Potter's latest + our UTF-8 fix)
- Field JSON v3 as only export format (legacy exports removed)
- Skill Editor tab with stamina presets (10%/25%/50%/75%/Infinite)
- skillinfo_parser.py — 100% roundtrip skill.pabgb parser
- Export/Import Field JSON on MercPets, DropSets, BagSpace tabs
- Multi-version baseline support in Stacker (1.0.0.3 + 1.0.0.4)
- Overlay spinners on all tabs
- Favorites system, drop enchant selector, socket display (ported from community dev)
- Mod Manager tab, Stores tab, shared state audit disabled

### v1.1.1 Release
- Fixed ALL presets (5 Sockets, Max Refine, No Cooldown, Max Charges, Great Thief)
- Root cause: preset definitions were missing from `_ITEM_PRESETS` dict, and `drop_default_data` handling was missing from `_eb_apply_preset`
- Fixed crimson_rs UTF-8 crash (PR #2 to potter420/crimson-rs)
- Re-enabled Great Thief after UTF-8 fix
- Added "Export as Mod Folder" button to ItemBuffs
- Added "Changelog / Releases" menu item
- Fixed splash version (was baked in PNG, now dynamic)
- Fixed stale overlay detection (auto-fallback to vanilla when overlay is from old game version)
- Fixed PAPGT creation from scratch (needs `unknown0: 1610` header fields)

### CrimsonCLI
- Built standalone CLI exe (11.4MB) — `cli.py` + `cli_core.py` + `CrimsonCLI.spec`
- Commands: apply-field-json, apply-field-json-raw, convert-legacy, export-field-json, extract-vanilla, roundtrip, remove-overlay, info
- All 7 commands tested and working
- No GUI dependencies — can be used by mod managers as subprocess

### crimson-rs Native JSON Bindings (PR #3)
- Added `json_traits.rs` with ToJsonValue/WriteJsonValue for all types
- Macro generates `to_json_dict` / `write_from_json_dict` alongside PyO3 methods
- `parse_iteminfo_to_json` + `serialize_iteminfo_from_json` + `parse_iteminfo_tracked_rust`
- Compiles but native Rust path doesn't roundtrip correctly yet — CLI bridge is the working path

### DMM Integration Attempt
- Built his source, fixed crimson-rs path, added cli_bridge.rs
- Field JSON v3 mods detected but "0 mod(s) applied" — his mount pipeline doesn't reach v3 code path
- Added debug logging but binary wasn't being rebuilt properly
- **Conclusion**: CrimsonCLI.exe subprocess is the viable integration path, not native Rust

### PABGB Toolkit
- `tools/pabgb_toolkit/` — standalone shareable package
- `pabgb_pipeline.py` — unified pipeline (Mac RTTI + auto-decoder + IDA + parser gen)
- `pabgb_auto_decoder.py` — entropy scoring, RTTI integration, anchor constraints, parser stub gen
- `ida_dump_everything.py` — overnight IDA dump script (incremental, resumable)
- `ida_dump_v2.py` — lightweight single-class dumper
- Ran pipeline against all 114 pabgb tables, extracted RTTI for 20+ classes
- Dumped all 121 pabgb/pabgh files for 1.0.4 to `1.0.4 PABGB_PABGH/`

### Skill Editor Bulk Mods
- Zero Cooldown — works, tested in-game ✓
- Free Skills — works, tested in-game ✓
- Unlock All — re-enabled (was disabled, Max Level 30 was the actual crasher)
- Max Level 30 — REMOVED, caused game crash (changes size on raw-fallback entries)
- CrowWing->Rocket swap — no visible effect (_skillGroupKey swap doesn't change behavior)
- Permanent Buffs — added for testing (_buffSustainFlag=1 on all skills)
- Skill body swap test — full entry body swap between same-size skills

## What's In Progress

### ReserveSlot Editor (F1/F2 Action Wheel) — NEXT SESSION
- `reserveslot.pabgb` fully decoded: 27 entries, 19 RTTI fields
- Key discovery: `_enableVehicleList` contains u16 hashes that filter which mounts show in the wheel
- Vehicle category hashes mapped: Horse=0x4240, Wolf=0x4246, Dragon=0x4258, ATAG=0x425C, etc.
- VehicleSlot has 9 allowed categories, VehicleSlot_Dragon has 1, VehicleSlot_Mechanic has 2
- Binary layout fully mapped (see memory/project_reserveslot_decoded.md)
- **TODO**: Build reserveslot_parser.py, new tab, "Add All Mounts Everywhere" button

### IDA Overnight Dump
- `ida_dump_everything.py` script ready to run
- Dumps: functions, strings, Korean field names, imports, types, decompiled pseudocode
- Incremental/resumable — skips completed steps on re-run
- Output: `tools/ida_field_maps/full_dump/`

### Stacker skill.pabgb Support
- Plan written at `.claude/plans/wondrous-noodling-stallman.md`
- skillinfo_parser.py ready, needs integration into Stacker's merge pipeline
- Requires: classify skill-targeting mods, separate merge path, skill serialization

### BuffLevelData Full Decode
- 38 unique subclass vtables identified
- Common base fields decoded (18 fields)
- 1761/1952 entries fully decoded, 191 raw fallback
- Subclass tails stored as raw bytes — need IDA decompilation of 38 vtable[10] functions

## Key Files Modified
```
gui/tabs/buffs_v319.py      — presets fix, export mod folder, favorites, drop enchant
gui/tabs/skill_tree.py      — skill editor, stamina presets, bulk mods, skill swap
gui/tabs/stacker.py         — multi-baseline, field json fixes, hex offset parsing
gui/tabs/world.py           — overlay spinners, field json export/import
gui/tabs/bagspace.py        — overlay spinner, field json
gui/tabs/mercpets.py        — field json export/import
gui/main_window.py          — disabled tabs, changelog link, stale overlay fix
updater.py                  — version 1.1.1
skillinfo_parser.py         — NEW, 100% roundtrip skill.pabgb parser
cli.py                      — NEW, standalone CLI
cli_core.py                 — NEW, CLI core functions (no GUI imports)
CrimsonCLI.spec             — NEW, PyInstaller spec for CLI exe
paz_patcher.py              — unchanged
crimson_rs/crimson_rs.pyd   — updated with UTF-8 fix
```

## Releases
- v1.1.0: https://github.com/NattKh/CRIMSON-DESERT-SAVE-EDITOR-AND-GAME-MODS/releases/tag/gamemods-v1.1.0
- v1.1.1: https://github.com/NattKh/CRIMSON-DESERT-SAVE-EDITOR-AND-GAME-MODS/releases/tag/gamemods-v1.1.1

## PRs to potter420/crimson-rs
- PR #2 (UTF-8 fix): https://github.com/potter420/crimson-rs/pull/2
- PR #3 (native JSON): https://github.com/potter420/crimson-rs/pull/3

## Known Issues
- Max Level 30 crashes game (size change on raw-fallback entries)
- _skillGroupKey swap doesn't change skill behavior (skills resolved by key, not groupKey)
- DMM v3 integration needs more investigation — mount pipeline doesn't reach v3 code
- Stale overlays from old game versions cause 0/N items parsed (fixed with auto-detection)
- PAPGT created from scratch needs header fields (unknown0=1610)
