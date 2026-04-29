# MercenarySaveData / MercenaryClanSaveData — Field Map from IDA

Date: 2026-04-26

## MercenaryClanSaveData (Parent Container)

Type name string at `0x144b67758`. Registration at `sub_140165AA0`.

Fields:
- `_mercenaryDataList` — List of MercenarySaveData entries (the main roster)
- `_hyosiMercenarySaveList` — Separate Hyosi mercenary list

Related types:
- `MercenaryClanHyosiElementSaveData`
- `CallMercenarySpawnDurationSaveData`
- `MercenaryOccupationState`

## MercenarySaveData (Per-Mercenary Entry)

Type name string at `0x144b672e0`. Registration at `sub_1401658C0`.
Big reader/serializer: `sub_141467E90` (16K, references all field strings).

### Fields with confirmed runtime offsets (from IDA binder functions)

| Runtime Offset | Field | Type | Binder Function | Notes |
|:-:|---|---|---|---|
| 56 (a1[14]) | `_ownedCharacterKey` | u32 | `sub_141461C00` | Character key: 1=Kliff, 4=Damian, 6=Oongka |
| 236 | `_isMainMercenary` | u8 | `sub_1414666D0` | Active/main character flag |
| 237 | `_isInitialize` | u8 | `sub_1414668F0` | Whether entry is initialized |
| 238 | `_isDead` | u8 | `sub_141466B20` | Dead state |
| 239 | `_isBlockedAbility` | u8 | `sub_141466D50` | Ability blocked flag |
| 240 | `_isHyosiMercenary` | u8 | `sub_141466F80` | Hyosi flag |

### Fields from string table (offsets not yet confirmed via binders)

Found in the string block at `0x144b672e0`–`0x144b675d0`:

- `_mercenaryNo` — Mercenary number/index
- `_buffSaveKey` / `BuffRemainTime` / `SkillAndLevel` / `_remainTime` — Buff data
- `_prevFeedFromCampStrawTime` / `_nextFeedFromCampStrawTime` — Camp feeding
- `_workStartTime` / `_workCompleteTime` / `_onlyWorkStartTime` / `_onlyWorkCompleteTime` — Work timers
- `_workPlaceFactionNodeKey` — Assigned work location
- `_deadTime` — Time of death
- `_mercenaryName` — Custom name
- `_lastBreedingTime` — Breeding timer
- `_lastPaidTime` — Pay timer
- `_totalDistance` / `_movedDistance` — Movement tracking
- `_lastSummoned` — Last summon time
- `_moveVelocity` — Movement speed
- `_spawnYaw` / `_spawnPosition` / `_spawnFieldInfoKey` — Spawn location
- `_occupationState` (`MercenaryOccupationState`) — Current occupation
- `_customizationSaveData` — Appearance data
- `_isBlockedAbility` — Ability lock

### Notable ABSENCE

**There is NO `_isPlayable` or `_isUnlocked` field in MercenarySaveData.**

The `_isPlayable` string (`0x144b06b91`) is in the **MercenaryInfo** pabgb context (static game data), NOT in the save data.

This means character availability is likely determined by:
1. Whether a MercenarySaveData entry EXISTS in `_mercenaryDataList` for that character key
2. The `_isMainMercenary` flag (who you're currently playing as)
3. Some external check (quest state, GamePlayTrigger, etc.)

## GamePlayTriggerInfo (Blob Table)

Only ONE field found: `_gamePlayTriggerInfoKey` (u32, PARC field hash).

Registration functions at `sub_140A62150` and `sub_140A62260` both bind the same field name. This means GamePlayTriggerInfo entries in pabgb have essentially: `key + stringKey + isBlocked + _gamePlayTriggerInfoKey` and possibly more undecoded fields in the blob.

The 12 `GamePlayTrigger_PlayableCharacter_*` entries likely contain a `_gamePlayTriggerInfoKey` that references... something. The value of this key for each trigger entry would tell us what they point to.

## Next Steps

1. **Check if Damian/Oongka entries EXIST in _mercenaryDataList** on the Chapter 1 save vs the post-Chapter-9 save. If they're missing from Ch1, the game won't show them regardless of mercenaryinfo.pabgb flags.

2. **Decompile sub_141467E90** (16K MercenarySaveData reader) to get the FULL PARC field list and their types — this would let us build a proper parser for the mercenary section in save files.

3. **Parse GamePlayTriggerInfo entries** from the pabgb to read `_gamePlayTriggerInfoKey` values for the PlayableCharacter triggers. These keys might reference conditions, variables, or other tables that control the unlock.
