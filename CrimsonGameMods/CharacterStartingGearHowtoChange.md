# Character Starting Gear — How It Works & How to Change It

Date: 2026-04-28

## Where Starting Gear Is Defined

Starting equipment is defined in **`characterinfo.pabgb`**, field `_equipItemInfoList`.
It is NOT a quest reward. The game reads this list when a character first spawns and
grants all items automatically.

Parser: `characterinfo_parser_v2.py` — IDA-derived, roundtrip-verified.

## Starting Loadouts

### Kliff (key=1) — 10 items

| # | ItemKey | Name |
|---|---------|------|
| 0 | 1163042 | Wolf_OneHandSword |
| 1 | 1001147 | Wood_OneHandShield |
| 2 | 230029 | Rusty_Hagwood_OneHandDagger |
| 3 | 1003265 | GreyWolf_OneHandBow |
| 4 | 1163044 | Inytium_Leather_Armor |
| 5 | 1000296 | Inytium_Leather_Cloak |
| 6 | 1163045 | Inytium_Leather_Gloves |
| 7 | 1163046 | Inytium_Leather_Boots |
| 8 | 1001523 | Item_Fist_Kliff |
| 9 | 10026 | Lantern |

### Damian (key=4) — 11 items

| # | ItemKey | Name |
|---|---------|------|
| 0 | 200901 | Demian_OneHandRapier |
| 1 | 1000683 | Damian_OneHandShield |
| 2 | 1001747 | Damian_OneHandPistol |
| 3 | 230905 | Rikisis_OneHandDagger |
| 4 | 1001532 | Damian_Demeniss_Elite_Uniform_Leather_Armor |
| 5 | 1001560 | Damian_Demeniss_Uniform_Leather_Cloak |
| 6 | 1002297 | Damian_Demeniss_Uniform_Leather_Gloves |
| 7 | 1001557 | Damian_Demeniss_Elite_Uniform_Leather_Boots |
| 8 | 240031 | Tynion_Giant_TwoHandGiantBastard |
| 9 | 10026 | Lantern |
| 10 | 1001129 | Daeil_Band |

### Oongka (key=6) — 13 items

| # | ItemKey | Name |
|---|---------|------|
| 0 | 250995 | Rusty_Cigar_TwoHandAxe |
| 1 | 1675016612 | Orc_OneHandCannon |
| 2 | 230917 | Aurio_OneHandDagger |
| 3 | 1163251 | Oongka_Basic_Leather_Armor |
| 4 | 1000678 | Oongka_Basic_Leather_Cloak |
| 5 | 133072 | Langust_Leather_Boots |
| 6 | 1002101 | Oongka_Basic_Leather_Gloves |
| 7 | 1001816 | Greyfur_Necklace |
| 8 | 1000478 | Kliff_Earring |
| 9 | 1003688 | Item_Fist_Oongka |
| 10 | 1000975 | Oongka_Rocket_Helm |
| 11 | 10026 | Lantern |
| 12 | 1001129 | Daeil_Band |

### Shared Items
- **Lantern** (10026) — all three
- **Daeil_Band** (1001129) — Damian + Oongka
- **Kliff_Earring** (1000478) — listed under Oongka (shared accessory)

## Horses / Mounts

Mounts are NOT in `_equipItemInfoList`. They are auto-granted at runtime when the
character's `MercenarySaveData` entry exists in the save file.

| Character | Mount | CharKey | How Granted |
|-----------|-------|---------|-------------|
| Kliff | Rokade (`Riding_Horse_Tiuta_Unique_2050_kliff`) | 1003120 | Always present in save |
| Damian | Damian's Horse | 1001173 | Auto-granted when Damian's MercenarySaveData exists |
| Oongka | Oongka's Horse | 1001172 | Auto-granted when Oongka's MercenarySaveData exists |

Rokade's characterinfo entry:
- `_vehicleInfo: 16960` (is a vehicle)
- `_spawnActorType: 5` (mount, not player)

Player characters have `_vehicleInfo: 0` and `_callVehicleGimmickInfo: 0` — the
mount binding is at the save/runtime level, not in characterinfo.

## Other Relevant Fields in characterinfo

| Field | Kliff | Damian | Oongka |
|-------|-------|--------|--------|
| `_equipInfo` | 1 | 4 | 6 |
| `_mercenaryInfo` | 1 | 2 | 1 |
| `_spawnActorType` | 1 | 4 | 4 |
| `_factionInfo` | 1000000 | 1000000 | 1000000 |
| `_mercenaryDropInfoList` | [700002] | [700003] | [700004] |
| `_skillInfoBySpawnList` | [] | [] | [] |
| `_characterRewardDataList` | [] | [] | [] |

Skills are empty in the starting list — they get populated by the game when the
character levels up or learns abilities.

## How to Modify Starting Gear

### Using characterinfo_parser_v2.py

```python
import characterinfo_parser_v2 as cp
import crimson_rs

game_path = "C:/Program Files (x86)/Steam/steamapps/common/Crimson Desert"
dp = "gamedata/binary__/client/bin"

pabgb = crimson_rs.extract_file(game_path, "0008", dp, "characterinfo.pabgb")
pabgh = crimson_rs.extract_file(game_path, "0008", dp, "characterinfo.pabgh")
entries = cp.parse_all(pabgh, pabgb)

kliff = cp.get_entry_by_key(entries, 1)
```

**IMPORTANT:** The `_equipItemInfoList` is a `read_list_reward_data()` structure
(sub_1410D6CC0). Each element is 64 bytes in the raw data:
- h1 (u32): ItemKey hash — looked up at runtime via sub_141100480
- h2 (u32): secondary hash (always 0 for starting gear)
- 7 × u64: parameters (all `0xF4240` = 1000000 for starting gear, likely defaults)

To change starting gear, you'd need to patch the raw bytes of the entry at the
correct offset. The parser stores `_raw` for byte-perfect roundtrip, so you can
use `cp.set_field_raw(entry, offset, new_bytes)` to patch specific fields.

### Overlay Deployment

Use a PAZ overlay (e.g. group `0065`) with `PackGroupBuilder(NONE, NONE)`:
```python
builder = crimson_rs.PackGroupBuilder(
    group_dir, crimson_rs.Compression.NONE, crimson_rs.Crypto.NONE)
builder.add_file("gamedata/binary__/client/bin", "characterinfo.pabgb", new_pabgb)
builder.add_file("gamedata/binary__/client/bin", "characterinfo.pabgh", new_pabgh)
pamt_bytes = bytes(builder.finish())
```

Install to game root (e.g. `CrimsonDesert/0065/`), NOT `paz/0065/`.

### Caveats

- characterinfo.pabgb is 23MB with 6966 entries — overlay will be large
- The parser reaches ~1500-1700B of each 3700-3900B entry (40-45% parsed)
- Remaining tail (~2200B) is stored as raw bytes for roundtrip safety
- Modifying `_equipItemInfoList` changes entry size → must rebuild pabgh offsets
- Test on a non-critical save first

## Related Files

| File | Purpose |
|------|---------|
| `characterinfo_parser_v2.py` | IDA-derived parser (roundtrip-verified) |
| `mod_early_character_unlock.py` | Mercenary + condition overlay for character unlock |
| `mod_quest_char_unlock.py` | Quest start_player_list patcher |
| `MERCENARY_INSERTION_GUIDE.md` | Save-level character insertion procedure |
| `Character unlock Gates.md` | Full character unlock research |
