# Fork Review: ShadowfeindX/CRIMSON-DESERT-SAVE-EDITOR-AND-GAME-MODS

**Date**: 2026-04-25
**Fork**: https://github.com/ShadowfeindX/CRIMSON-DESERT-SAVE-EDITOR-AND-GAME-MODS
**Base**: Forked from NattKh v1.1.3, latest commit "integrate itembuffs ui changes" (2026-04-25 17:01 UTC)

## What we cherry-picked (merged into our source)

These were genuinely additive and enhance the tool:

1. **Buff-to-item index** (`iteminfo_index.py`) — new `buff_to_items` dict mapping buff IDs to items that carry them, parallel to the existing `passive_to_items`
2. **find_similar() expanded** — new `"passives"` and `"buffs"` modes so users can find all items sharing a specific passive skill or equipment buff
3. **"Show items with this passive/buff"** context menu actions on the stats detail table (right-click a passive or buff row)
4. **"With same passives" / "With same buffs"** in the Find Similar submenu on the item table
5. **Max Stacks preset** — one-click button to set `max_stack_count` to 999999
6. **`_safely_replace_buff_item()`** — safe dict replacement helper used by the new import flow
7. **Dump item info to disk** — right-click context menu action to export a single item's full JSON
8. **Import ITEMINFO** — load a previously dumped item JSON back into the editor with validation
9. **DEV Ring preset buttons** — individual one-click buttons (Immunity, STR/HP, DEF/HP, MP/Stam, Speed, All DEV, Elemental, Jump Boots) in a collapsible group below the main preset grid. Replaces the dead combo-box code that was never wired up. Collapsible so it doesn't clutter the page for casual users.

## Dev feedback → what we fixed based on their response

After sending the initial review, the fork author (ShadowfeindX) clarified several items. We incorporated the valid points:

### Accepted: `_eb_status` → `_buff_status_label` for cross-tab actions

Dev correctly pointed out that `_eb_status` lives on the Advanced/Imbue panel and is NOT visible when preset buttons fire from the Presets tab. We selectively migrated 6 calls to `_buff_status_label` (the global bottom-bar label): effect catalog apply, `_eb_apply_preset`, VFX gimmick, drop enchant level, extend sockets, bulk sockets. The 8 calls that fire from the same panel (`_eb_add_passive`, remove passive, imbue, stat selection) remain on `_eb_status` where they're visible.

### Accepted: Duplicate socket row removal

Dev correctly identified that the socket row was duplicated — once in the presets build section and again in the Sockets group under Advanced. The second instance overwrites `self._eb_socket_count` and `self._eb_socket_valid`, orphaning the first widget. We removed the first (stale) copy; the Sockets group under Advanced is the canonical location.

### Accepted: God Mode `skip=True`

Dev correctly pointed out the double-dialog issue — `apply_godmode()` closure already confirms, then `_eb_god_mode()` confirms again. We added `skip: bool = False` to `_eb_god_mode()` and the `apply_godmode()` closure now passes `skip=True` to all sub-calls (god_mode + all preset calls).

### Accepted: Debug prints → `log.info`

Dev noted log wasn't available in `iteminfo_index.py`. We added `import logging` and replaced the prints with a single `log.info("Index built: %d items, %d passives, %d buffs", ...)`.

## Remaining issues in the fork (NOT merged)

### 1. Indentation bug (~line 8879 in fork)

```python
# Fork has:
    cur["entries"] = [e for e in cur["entries"]  # extra indent
# Should be:
cur["entries"] = [e for e in cur["entries"]
```
This changes the scope of the statement — confirmed as bug by dev.

### 2. Commented-out debug line

```python
# if it.get("key") == 1000578:
#     print(it)
```
Dead debug code — dev confirmed should be deleted.

### 3. Typo in preset description

Fork has `"be default"` instead of `"by default"` in the `max_enchant` preset description.

### 4. `addAction` called twice for export menu items

The fork has patterns like:
```python
act_export_field = export_mod_menu.addAction("Export as Field JSON (v3)")
...
export_mod_menu.addAction(act_export_field)  # DUPLICATE — adds the action twice
```
This would cause the menu item to appear twice.

### 5. Empty stub page

`_build_buff_drop_data_page()` returns an empty QWidget with no content. Wired into action tabs but no functionality — dev confirmed safe to delete.
