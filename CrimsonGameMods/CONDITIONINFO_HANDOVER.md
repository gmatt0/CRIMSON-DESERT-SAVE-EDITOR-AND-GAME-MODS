# ConditionInfo Handover

Date: 2026-04-25

## Status

`conditioninfo.pabgb/.pabgh` now has **100% structural roundtrip**.

That means:

- Entries parse cleanly.
- Entries serialize back byte-for-byte.
- Full `.pabgb` serializes back byte-for-byte.
- Full `.pabgh` serializes back byte-for-byte.
- The compiled `_gameCondition` bytecode is preserved exactly.

That does **not** mean semantic bytecode decode is finished. `compiled_condition_hex` is still an opaque compiled condition blob. We can safely preserve or copy it, but we cannot yet compile arbitrary expression text into new bytecode.

## Current Layout

Mac binary reflection confirms `ConditionInfo` fields:

```text
_key
_stringKey
_isBlocked
_gameCondition
_originalString
_parserType
```

Current parser maps this as:

```text
u32 _key
u32 _stringKey_len
bytes _stringKey
u8 nul
bytes compiled_condition_hex    # contains _isBlocked/_gameCondition, not semantically decoded yet
u32 _originalString_len
bytes _originalString
u8 _parserType
```

Important correction: `_expression` belongs to `GameConditionInfo`, not `ConditionInfo`.

## Verified Roundtrip

Roundtrip command:

```powershell
python C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\parse_conditioninfo.py `
  "C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\live_extract\conditioninfo.pabgb" `
  "C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\live_extract\conditioninfo.pabgh" `
  --roundtrip
```

Result:

```json
{
  "ok": true,
  "entry_count": 8934,
  "pabgb_size": 786534,
  "pabgh_size": 71474,
  "count_size": 2,
  "key_size": 4
}
```

Verified datasets:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\1.0.4 PABGB_PABGH\conditioninfo.pabgb
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\1.0.4 PABGB_PABGH\pabgh\conditioninfo.pabgh

C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\live_extract\conditioninfo.pabgb
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\live_extract\conditioninfo.pabgh

C:\Users\Coding\CrimsonDesertModding\extractedpaz\gamedata_dump\conditioninfo.pabgb
C:\Users\Coding\CrimsonDesertModding\extractedpaz\gamedata_dump\conditioninfo.pabgh
```

SHA-256 prefixes from verified files:

```text
Current/live 1.0.4 conditioninfo.pabgb: 1a9bfc68b72adb7b
Current/live 1.0.4 conditioninfo.pabgh: c3037ffb545541ea
Old extractedpaz conditioninfo.pabgb: 387eebd457fc9864
Old extractedpaz conditioninfo.pabgh: 9622ba750855f7a3
```

## Live Game Folder

Installed game folder supplied by user:

```text
C:\Program Files (x86)\Steam\steamapps\common\Crimson Desert
```

Live extraction was done with `crimson_rs.extract_file()` from group `0008` and internal PAZ path:

```text
gamedata/binary__/client/bin/conditioninfo.pabgb
gamedata/binary__/client/bin/conditioninfo.pabgh
```

Live extracted files:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\live_extract\conditioninfo.pabgb
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\live_extract\conditioninfo.pabgh
```

The live extraction is byte-identical to the local `1.0.4 PABGB_PABGH` copy.

## Main Code Files

Parser and structural serializer:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\parse_conditioninfo.py
```

Bytecode corpus analyzer:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\conditioninfo_bytecode_analyzer.py
```

Universal parser used for PABGH boundaries:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\universal_pabgb_parser.py
```

Schema/report:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\conditioninfo_schema.json
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\decoded_tables\conditioninfo_report.json
```

## Generated Data Artifacts

Current 1.0.4 mapped entries:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\decoded_tables\conditioninfo_104_mapped.json
```

Current 1.0.4 enriched with old map links:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\decoded_tables\conditioninfo_104_enriched_from_old_map.json
```

Current 1.0.4 bytecode corpus:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\decoded_tables\conditioninfo_104_bytecode_corpus.json
```

Old extractedpaz mapped entries:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\decoded_tables\conditioninfo_old_extractedpaz_mapped.json
```

Old vs 1.0.4 diff:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\decoded_tables\conditioninfo_old_vs_104_diff.json
```

Old bytecode corpus:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\decoded_tables\conditioninfo_old_bytecode_corpus.json
```

Mac condition symbol catalog:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\decoded_tables\conditioninfo_mac_condition_symbols.json
```

Roundtrip rebuilt files:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\roundtrip\conditioninfo_104_rebuilt.pabgb
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\roundtrip\conditioninfo_104_rebuilt.pabgh
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\roundtrip\conditioninfo_live_rebuilt.pabgb
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\roundtrip\conditioninfo_live_rebuilt.pabgh
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\roundtrip\conditioninfo_old_rebuilt.pabgb
C:\Users\Coding\CrimsonDesertModding\CrimsonGameMods\tools\pabgb_toolkit\roundtrip\conditioninfo_old_rebuilt.pabgh
```

## External Resources

Old complete game map:

```text
C:\Users\Coding\CrimsonDesertModding\ResearchFolder\game_map_complete_v3.json
```

This has `8801` old condition keys and useful condition links:

```text
condition_refs_skills
condition_refs_items
condition_refs_knowledge
condition_refs_knowledge_groups
condition_refs_regions
condition_refs_characters
condition_refs_quest
condition_refs_mission
condition_checks_knowledge
condition_checks_quest
condition_checks_faction
condition_requires_quest
condition_requires_mission
```

Mac binary:

```text
C:\Users\Coding\Downloads\CrimsonDesert_Steam-2026-04-23
```

Extracted from it:

- `421` condition-related symbols
- `408` `ConditionData_*` symbols

Old failed JSON dump:

```text
C:\Users\Coding\CrimsonDesertModding\CrimsonSaveEditorGUI\pabgb_full_dump\conditioninfo.json
```

Do not trust this as a schema. It has `8803` rows, but every row has:

```text
_parsed_bytes = 2
_stringKey = "<parse_stopped at +2>"
```

It is a failed parse, not a useful decode.

CdModCreator inspected here:

```text
C:\Users\Coding\CrimsonDesertModding\ResearchFolder\Perfect Mod Loader\CdModCreator
```

Useful for entry-anchored patching concepts, not semantic `ConditionInfo` decoding. Its `PabgbParser.cs` builds entry maps, but does not decode `_gameCondition` bytecode.

## Current 1.0.4 Counts

```text
conditioninfo entries: 8934
pabgb size: 786534
pabgh size: 71474
pabgh count prefix: u16
pabgh key size: 4
```

Parser type distribution:

```text
0: 3007
2: 4445
4: 1479
5: 3
```

Bytecode corpus:

```text
Detected expression functions: 229
```

Top functions include:

```text
CompleteSubMission
StageKey
CompleteMission
KnowledgeKey
CheckKnowledge
QuestDialogKey
CompleteQuest
ItemKey
CheckCharacterKey
MissionKey
CheckHaveItem
```

## Known Tiny Reusable Conditions

Potential force-pass / force-fail candidates, still needs in-game validation:

```text
CheckNone()
compiled_condition_hex = 030200000100
parserType = 0

!CheckNone()
compiled_condition_hex = 02030200010000
parserType = 0

!CheckNone()
compiled_condition_hex = 02040001000000
parserType = 4
```

These can be used as existing known-good compiled blobs for experimental condition replacement.

## What Can Be Added To CrimsonGameMods Now

Safe features:

1. Condition browser/search.
2. Condition dependency viewer using old map links and expression text.
3. Old vs 1.0.4 condition diff viewer.
4. Whole-condition replacement using another existing compiled blob.
5. Patch exporter that rewrites `.pabgb/.pabgh` with structural roundtrip.

Experimental features:

1. Force pass / force fail by replacing compiled blob with known tiny conditions.
2. Simple key/hash argument swaps for validated one-function patterns, e.g.:
   - `CompleteQuest(...)`
   - `CompleteMission(...)`
   - `CheckKnowledge(...)`
   - `CheckHaveItem(...)`

Not safe yet:

1. Arbitrary text expression editing.
2. Compiling new `_originalString` text into bytecode.
3. Claiming full semantic `_gameCondition` AST decode.

## Next Technical Steps

1. Build a small `conditioninfo_editor.py` that can:
   - load `.pabgb/.pabgh`
   - replace one condition with another
   - optionally apply force-pass/force-fail presets
   - save byte-identical structure

2. Add pattern validators for simple functions:
   - ensure compiled byte length and opcode prefix match known corpus patterns
   - only patch key/hash bytes when pattern is unambiguous

3. Decode bytecode node grammar:
   - group by simple expressions in `conditioninfo_104_bytecode_corpus.json`
   - map opcode bytes to `ConditionData_*` symbols from Mac binary
   - produce `decode_game_condition(bytes) -> AST`
   - prove `AST -> bytes` is byte-identical

4. Only after AST roundtrip works, attempt a text compiler:
   - `_originalString -> AST -> compiled bytes`

