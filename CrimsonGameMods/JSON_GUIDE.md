# Better JSON — Crimson Desert Mod Manager v8

## Quick Start

1. Create a `.json` file describing your changes
2. Drop it into the manager (drag & drop) or place it in the `Mods/` folder
3. Activate the mod, click **APPLY MODS**, done

---

## Mod File Structure

Every mod is a JSON file with two sections: **metadata** and **patches**.

```json
{
    "modinfo": {
        "title": "My Awesome Mod",
        "version": "1.0",
        "author": "YourName",
        "description": "What this mod does.",
        "nexus_url": "https://www.nexusmods.com/crimsondesert/mods/123"
    },
    "format": 2,
    "patches": [
        {
            "game_file": "gamedata/skill.pabgb",
            "source_group": "0008",
            "changes": [
                {
                    "entry": "Skill_CrowWing",
                    "rel_offset": 116,
                    "offset": 497051,
                    "original": "f0d8ffff",
                    "patched": "ffffffff",
                    "label": "stamina drain"
                }
            ]
        }
    ]
}
```

---

## Metadata (`modinfo`)

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Mod name shown in the manager |
| `version` | No | Version string (e.g. `"1.0"`) |
| `author` | No | Your name |
| `description` | No | Short description of what the mod does |
| `nexus_url` | No | Link to Nexus Mods page (enables thumbnail fetch) |

---

## Patch Formats

There are three ways to specify where to patch. Pick one based on your needs.

### Format v1 — Absolute Offset

Uses the exact byte position in the file. Simple but **breaks after game updates**.

```json
{
    "patches": [{
        "game_file": "gamedata/skill.pabgb",
        "source_group": "0008",
        "changes": [{
            "offset": 497051,
            "original": "f0d8ffff",
            "patched": "ffffffff",
            "label": "stamina drain"
        }]
    }]
}
```

- `offset` — absolute byte position in the file
- `original` — hex bytes at that position (verified before patching)
- `patched` — hex bytes to write
- `label` — optional description

### Format v2 — Entry-Anchored (Recommended)

References a named entry + relative offset. **Survives game updates** because the manager resolves the entry's position at runtime.

```json
{
    "format": 2,
    "patches": [{
        "game_file": "gamedata/skill.pabgb",
        "source_group": "0008",
        "changes": [{
            "entry": "Skill_CrowWing",
            "rel_offset": 116,
            "original": "f0d8ffff",
            "patched": "ffffffff",
            "label": "stamina drain"
        }]
    }]
}
```

- `format: 2` — must be set at root level
- `entry` — name of the data entry in the .pabgb file
- `rel_offset` — byte offset **within** that entry (not the whole file)

**How it works:** The manager reads the .pabgb/.pabgh schema, finds where `Skill_CrowWing` starts, adds `rel_offset`, and patches there. After a game update, the entry may be at a different file position — but the name and internal structure stay the same.

### Hybrid — Best of Both (Recommended for Sharing)

Include both entry-anchored and absolute offset. The manager tries entry first, falls back to offset.

```json
{
    "format": 2,
    "patches": [{
        "game_file": "gamedata/skill.pabgb",
        "source_group": "0008",
        "changes": [{
            "entry": "Skill_CrowWing",
            "rel_offset": 116,
            "offset": 497051,
            "original": "f0d8ffff",
            "patched": "ffffffff",
            "label": "stamina drain"
        }]
    }]
}
```

**Fallback order:**
1. Try `entry` + `rel_offset` → if `original` matches → patch
2. If entry not found → try `offset` → if `original` matches → patch
3. If neither works → skip with error

---

## Which Format Should I Use?

| Situation | Recommendation |
|-----------|----------------|
| Personal use | Any format works |
| Sharing on Nexus | **Hybrid** — most compatible |
| Needs to survive game patches | **v2** or **Hybrid** |
| Patching non-.pabgb files | **v1** — entry-anchored only works with .pabgb |

**When in doubt, use Hybrid.** It gives the best of both worlds.

---

## Patch Fields Reference

| Field | Used In | Description |
|-------|---------|-------------|
| `game_file` | All | Relative path to the game file (e.g. `"gamedata/skill.pabgb"`) |
| `source_group` | All | Group ID within the PAZ archive (e.g. `"0008"`) |
| `offset` | v1, Hybrid | Absolute byte position in the file |
| `entry` | v2, Hybrid | Entry name in the .pabgb file |
| `rel_offset` | v2, Hybrid | Byte offset within the entry |
| `original` | All | Expected hex bytes at the target position (safety check) |
| `patched` | All | New hex bytes to write |
| `label` | All (optional) | Human-readable description of the change |

---
