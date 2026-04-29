# CrimsonCLI Integration Guide for Mod Managers

Ship `CrimsonCLI.exe` (11MB) alongside your mod manager. It handles all iteminfo parsing, Field JSON v3 application, and legacy mod conversion without requiring Python or crimson-rs Rust bindings.

## Setup

Place `CrimsonCLI.exe` in your app's resources or tools directory:

```
YourModManager/
├── your_app.exe
├── tools/
│   └── CrimsonCLI.exe      ← 11MB, no dependencies
└── mods/
    └── my_mod.field.json
```

## Tauri/Rust Integration

```rust
use std::process::Command;
use std::path::Path;

const CLI: &str = "tools/CrimsonCLI.exe";

/// Apply a Field JSON v3 mod to the game.
/// Returns Ok(stdout) on success, Err(stderr) on failure.
fn apply_field_json(
    game_dir: &str,
    mod_path: &str,
    overlay: &str,
) -> Result<String, String> {
    let output = Command::new(CLI)
        .args(["apply-field-json", mod_path, "--game", game_dir, "--overlay", overlay])
        .output()
        .map_err(|e| format!("Failed to run CrimsonCLI: {}", e))?;

    if output.status.success() {
        Ok(String::from_utf8_lossy(&output.stdout).to_string())
    } else {
        Err(String::from_utf8_lossy(&output.stderr).to_string())
    }
}

/// Apply multiple mods at once (last-writer-wins on conflicts).
fn apply_multiple(
    game_dir: &str,
    mod_paths: &[&str],
    overlay: &str,
) -> Result<String, String> {
    let mut args: Vec<&str> = vec!["apply-field-json"];
    args.extend(mod_paths);
    args.extend(["--game", game_dir, "--overlay", overlay]);

    let output = Command::new(CLI)
        .args(&args)
        .output()
        .map_err(|e| format!("Failed to run CrimsonCLI: {}", e))?;

    if output.status.success() {
        Ok(String::from_utf8_lossy(&output.stdout).to_string())
    } else {
        Err(String::from_utf8_lossy(&output.stderr).to_string())
    }
}

/// Convert a legacy byte-offset mod to Field JSON v3.
fn convert_legacy(
    legacy_path: &str,
    output_path: &str,
) -> Result<String, String> {
    let output = Command::new(CLI)
        .args(["convert-legacy", legacy_path, "--output", output_path])
        .output()
        .map_err(|e| format!("Failed to run CrimsonCLI: {}", e))?;

    if output.status.success() {
        Ok(String::from_utf8_lossy(&output.stdout).to_string())
    } else {
        Err(String::from_utf8_lossy(&output.stderr).to_string())
    }
}

/// Remove an overlay from the game.
fn remove_overlay(game_dir: &str, overlay: &str) -> Result<String, String> {
    let output = Command::new(CLI)
        .args(["remove-overlay", "--game", game_dir, "--overlay", overlay])
        .output()
        .map_err(|e| format!("Failed to run CrimsonCLI: {}", e))?;

    if output.status.success() {
        Ok(String::from_utf8_lossy(&output.stdout).to_string())
    } else {
        Err(String::from_utf8_lossy(&output.stderr).to_string())
    }
}

/// Verify game data integrity.
fn verify_roundtrip(game_dir: &str) -> bool {
    Command::new(CLI)
        .args(["roundtrip", "--game", game_dir])
        .status()
        .map(|s| s.success())
        .unwrap_or(false)
}

/// Get mod info as text.
fn mod_info(mod_path: &str) -> Result<String, String> {
    let output = Command::new(CLI)
        .args(["info", mod_path])
        .output()
        .map_err(|e| format!("Failed to run CrimsonCLI: {}", e))?;

    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}
```

## Mount Pipeline Integration

For a mod manager's mount/apply workflow:

```rust
/// Mount all enabled mods in order.
fn mount_mods(game_dir: &str, enabled_mods: &[ModFile]) -> Result<(), String> {
    // Step 1: Convert any legacy mods to Field JSON v3
    let mut field_json_paths: Vec<String> = Vec::new();

    for m in enabled_mods {
        if m.format == 3 {
            // Already Field JSON v3
            field_json_paths.push(m.path.clone());
        } else if m.format == 2 {
            // Legacy byte-offset mod — convert first
            let converted = format!("{}.field.json", m.path);
            convert_legacy(&m.path, &converted)?;
            field_json_paths.push(converted);
        }
    }

    // Step 2: Apply all Field JSON v3 mods in one call
    let refs: Vec<&str> = field_json_paths.iter().map(|s| s.as_str()).collect();
    let result = apply_multiple(game_dir, &refs, "0058")?;
    println!("{}", result);

    Ok(())
}

/// Unmount — remove the overlay.
fn unmount(game_dir: &str) -> Result<(), String> {
    remove_overlay(game_dir, "0058")?;
    Ok(())
}
```

## Tauri Command Wrapper

Expose to the frontend via a Tauri command:

```rust
#[tauri::command]
async fn apply_iteminfo_mods(
    game_dir: String,
    mod_paths: Vec<String>,
    overlay: String,
) -> Result<String, String> {
    let refs: Vec<&str> = mod_paths.iter().map(|s| s.as_str()).collect();
    apply_multiple(&game_dir, &refs, &overlay)
}

#[tauri::command]
async fn convert_legacy_mod(
    legacy_path: String,
    output_path: String,
) -> Result<String, String> {
    convert_legacy(&legacy_path, &output_path)
}
```

Frontend (TypeScript):
```typescript
import { invoke } from '@tauri-apps/api/core';

// Apply mods
const result = await invoke('apply_iteminfo_mods', {
  gameDir: 'C:/Program Files/Steam/.../Crimson Desert',
  modPaths: ['mods/god_mode.field.json', 'mods/infinite_stamina.field.json'],
  overlay: '0058',
});

// Convert legacy mod
await invoke('convert_legacy_mod', {
  legacyPath: 'mods/old_mod.json',
  outputPath: 'mods/old_mod.field.json',
});
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Error (details in stdout) |

## Performance

- `roundtrip`: ~2 seconds (parse 6339 items + serialize)
- `apply-field-json`: ~3 seconds (parse + apply + serialize + pack overlay)
- `convert-legacy`: ~4 seconds (baseline match + patch + parse×2 + diff)
- `info`: instant

## Notes

- CrimsonCLI.exe bundles its own Python runtime + crimson_rs — no external dependencies
- The `game_baselines/` folder is bundled inside the exe for legacy mod conversion
- Multiple mods applied in one call are merged with last-writer-wins semantics
- The overlay number defaults to `0058` — use a different number to avoid conflicts with other tools
