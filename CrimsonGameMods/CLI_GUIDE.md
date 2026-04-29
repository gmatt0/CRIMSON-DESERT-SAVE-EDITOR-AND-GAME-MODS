# CrimsonGameMods CLI Guide

Command-line interface for applying, converting, and managing Crimson Desert mods without the GUI. Designed for mod managers (DMM, JMM, CDUMM) and automation scripts.

## Setup

```bash
# From source
python cli.py <command> [options]

# From built exe
CrimsonGameMods.exe --cli <command> [options]
```

Requires: game path must point to a valid Crimson Desert installation with `0008/0.paz` and `meta/0.papgt`.

---

## Commands

### `info`

Show details about one or more mod files. Works with both Field JSON v3 and legacy formats.

```bash
python cli.py info MOD.json
python cli.py info MOD1.json MOD2.field.json MOD3.json
```

Output:
```
my_mod.field.json:
  Format: Field JSON v3
  Target: iteminfo.pabgb
  Title: God Mode Preset
  Intents: 42
  Unique entries: 12
  Unique fields: 8
```

---

### `roundtrip`

Verify that the parser can read and re-write the game's vanilla iteminfo without any data loss. Use this to confirm crimson_rs is working correctly for your game version.

```bash
python cli.py roundtrip --game "C:/path/to/Crimson Desert"
```

Output:
```
Vanilla: 5,358,049 bytes
Parsed: 6339 items
Serialized: 5,358,049 bytes
Roundtrip: PASS
```

---

### `extract-vanilla`

Extract the unmodified iteminfo.pabgb from the game's PAZ archives. Useful for creating baselines or inspecting vanilla data.

```bash
python cli.py extract-vanilla --game "C:/path/to/game" --output vanilla.pabgb
python cli.py extract-vanilla --game "C:/path/to/game" --output vanilla.pabgb --pabgh vanilla.pabgh
```

---

### `apply-field-json`

Apply one or more Field JSON v3 mods to the game. This is the primary command for mod managers.

**Apply directly to game (creates overlay):**
```bash
python cli.py apply-field-json mod.field.json --game "C:/path/to/game"
python cli.py apply-field-json mod.field.json --game "C:/path/to/game" --overlay 0058
```

**Apply multiple mods (last-writer-wins on conflicts):**
```bash
python cli.py apply-field-json mod1.field.json mod2.field.json --game "C:/path/to/game"
```

**Write raw pabgb instead of overlay (for mod managers that handle packing):**
```bash
python cli.py apply-field-json mod.field.json --game "C:/path/to/game" --output patched.pabgb
```

**Verbose mode (shows skipped intents):**
```bash
python cli.py apply-field-json mod.field.json --game "C:/path/to/game" -v
```

What happens:
1. Extracts vanilla iteminfo from game
2. Parses into item dicts
3. Applies each intent by navigating the field path and setting the value
4. Serializes all items back to bytes
5. Packs into overlay (or writes raw file with `--output`)
6. Updates PAPGT so the game loads the overlay

---

### `convert-legacy`

Convert a legacy byte-offset JSON mod (Format 2) to Field JSON v3. Automatically detects which game version the mod targets by matching byte patterns against baselines in `game_baselines/`.

```bash
python cli.py convert-legacy old_mod.json
python cli.py convert-legacy old_mod.json --output new_mod.field.json
```

What happens:
1. Scans `game_baselines/` for the best-matching baseline (1.0.0.3 or 1.0.0.4)
2. Applies byte patches to the matched baseline (reverse-offset-sorted for inserts)
3. Parses both vanilla and patched with the appropriate parser (current or legacy)
4. Diffs the parsed dicts to produce field-name intents
5. Writes the Field JSON v3 file

Supports: replace patches, insert patches, hex string offsets, entry-anchored offsets.

---

### `export-field-json`

Merge multiple Field JSON v3 mods and export the combined result as a single Field JSON v3 file.

```bash
python cli.py export-field-json mod1.field.json mod2.field.json --game "C:/path/to/game" --output merged.field.json
```

---

### `remove-overlay`

Remove a mod overlay from the game directory and update the PAPGT metadata.

```bash
python cli.py remove-overlay --game "C:/path/to/game" --overlay 0058
```

---

## Field JSON v3 Format

The mod format used by all CLI commands. Uses field names instead of byte offsets — mods survive game updates.

```json
{
  "modinfo": {
    "title": "My Mod",
    "version": "1.0",
    "author": "AuthorName"
  },
  "format": 3,
  "target": "iteminfo.pabgb",
  "intents": [
    {
      "entry": "Oath_Of_Darkness",
      "key": 391518535,
      "field": "cooltime",
      "op": "set",
      "new": 1
    }
  ]
}
```

Field paths use dot notation for nested fields and brackets for array indices:
- `cooltime` — top-level scalar
- `drop_default_data.use_socket` — nested field
- `equip_passive_skill_list` — replace entire array
- `enchant_data_list[0].equip_buffs` — indexed array element

See `FIELD_JSON_V3_SPEC.md` for the complete specification.

---

## Integration with Mod Managers

Mod managers can call the CLI as a subprocess:

```javascript
// JavaScript/TypeScript (Tauri, Electron)
const { Command } = require('@tauri-apps/plugin-shell');
const result = await Command.create('CrimsonGameMods.exe', [
  '--cli', 'apply-field-json', 'mod.field.json',
  '--game', gamePath, '--overlay', '0058'
]).execute();
```

```python
# Python
import subprocess
result = subprocess.run([
    'CrimsonGameMods.exe', '--cli', 'apply-field-json', 'mod.field.json',
    '--game', game_path, '--overlay', '0058'
], capture_output=True, text=True)
```

```csharp
// C#
var process = Process.Start("CrimsonGameMods.exe",
    "--cli apply-field-json mod.field.json --game \"" + gamePath + "\"");
process.WaitForExit();
```

Exit codes: `0` = success, `1` = error (details in stderr).

---

## Overlay Numbers

Each tab uses a unique overlay number to avoid conflicts:

| Overlay | Owner |
|---------|-------|
| 0036 | DropSets |
| 0037 | SpawnEdit |
| 0039 | FieldEdit |
| 0058 | ItemBuffs (default) |
| 0061 | BagSpace |
| 0062 | Stacker |
| 0064 | SkillTree |
| 0065 | MercPets |

When calling `apply-field-json`, use `--overlay` to specify which slot. Default is `0058`.
