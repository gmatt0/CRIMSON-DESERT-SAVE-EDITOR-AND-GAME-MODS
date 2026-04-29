# Future Features TODO

## Stacker as Central Deploy Hub (Consolidation)

**Context**: Discussion between NattKh and ShadowfeindX (2026-04-25).

Currently each tab owns its own overlay group and deploy path:
- ItemBuffs → 0058/ (iteminfo + skill + charinfo)
- FieldEdit → 0039/ (fieldinfo + vehicleinfo + characterinfo + wantedinfo + etc.)
- Stores → 0060/ (storeinfo)
- Equipslotinfo → 0059/

**Goal**: Route ALL import/export through Stacker Tool. Build a central mod manifest that every tab pushes to. Stacker becomes the single deploy point with a checklist UI:
- [ ] Universal Proficiency
- [ ] Kliff Gun Fix
- [ ] Infinity Durability
- [ ] Max Stacks
- [ ] Custom Buffs (from ItemBuffs config)
- [ ] Custom Field Edits
- etc.

Users tick checkmarks, Stacker pulls from each tab's staged data, builds a unified overlay (or split overlays where required like equipslotinfo), and deploys.

**Why**: Eliminates confusion about which tab applies what, prevents overlay conflicts, gives one place to see everything that will be deployed.

**Scope**: Multi-session architecture change. Every tab currently manages its own `Apply to Game` and `Export`. Consolidating means:
1. Define a central `StagedMod` manifest (what files, what overlay group, what source tab)
2. Each tab pushes to the manifest instead of deploying directly
3. Stacker reads the manifest, shows the checklist, builds the overlay
4. Legacy `Apply to Game` buttons become "Stage for Stacker" or are removed

**Prerequisite**: Stacker already has "Pull ItemBuffs Edit" — extend this pattern to all tabs.
