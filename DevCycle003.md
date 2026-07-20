# Dev Cycle 003: RayChen Class Frigate Implementation

## Purpose

This plan turns the approved direction in `doc/raychen_design.md` into the first implementation cycle for the RayChen-class frigate.

The design document remains the source of truth for ship identity, combat role, visual direction, baseline stats, weapon layout, system direction, and campaign intent. This document is the work plan for the first playable implementation pass.

## Cycle Goal

Create a playable first version of the RayChen class inside the existing `Toranaga/` mod folder. The ship should load in Starsector, appear in refit, deploy in combat, use shields without passive flux failure, and behave as an elite overpowered frigate based on the Tahlan Skirt reference.

## Scope

Included in this cycle:

- Add the RayChen hull definition.
- Add or stage the RayChen ship sprite.
- Add the default `raychen_elite` variant.
- Add baseline campaign and combat stats from `doc/raychen_design.md`.
- Add description text.
- Update existing CSV files under `Toranaga/data`.
- Bump the mod version in `Toranaga/mod_info.json`.
- Use existing vanilla weapons, hullmods, and ship systems for the first playable pass.
- Validate JSON, CSV shape, asset references, weapon IDs, hullmod IDs, system IDs, and slot references.
- Confirm there is no ID or file-path collision with vanilla Starsector data before implementation.

Deferred unless required for the ship to function:

- Custom Java hullmods.
- Custom Java ship-system implementation.
- Custom weapons.
- Custom wings or drones.
- Campaign start or quest integration.
- Final balance.
- Final art polish.
- Expanding to the full seven-mount concept from `doc/raychen.md`.

## Source Design Commitments

The first implementation pass should preserve these decisions from `doc/raychen_design.md`:

- Hull size is `FRIGATE`.
- The ship is intentionally overpowered relative to vanilla frigates.
- It is a fast elite interceptor and hunter-killer, not a mini cruiser.
- It visually follows `tahlan_skirt.png`.
- It should copy the Skirt sprite exactly for the first implementation.
- It should preserve the Skirt dimensions, center, shield geometry, bounds, and engine slots unless testing proves otherwise.
- It should use `raychen` and `raychen_elite` as the current IDs.
- It should not collide with vanilla Starsector hull IDs, variant IDs, description IDs, or file paths.
- It should not have fighter bays in the first pass.
- It should use four visible forward mounts based on the Skirt hardpoint layout.

## Reference Data

Use these ScalarTech files as implementation references:

- Sprite: `inspiration/scalartech-solutions-0.9.3b/graphics/tahlan/ships/tahlan_skirt.png`
- Hull: `inspiration/scalartech-solutions-0.9.3b/data/hulls/tahlan_skirt.ship`
- Variant: `inspiration/scalartech-solutions-0.9.3b/data/variants/tahlan_skirt_skirmisher.variant`
- Variant: `inspiration/scalartech-solutions-0.9.3b/data/variants/tahlan_skirt_hunter.variant`

Reference Skirt geometry:

- Width: `100`
- Height: `124`
- Center: `[50, 54.5]`
- Collision radius: `97`
- Shield center: `[0, 0]`
- Shield radius: `90.5`
- Bounds: copy from `tahlan_skirt.ship`
- Engine slots: copy from `tahlan_skirt.ship`, adapting engine style to a safe vanilla style if Tahlan custom styles are unavailable.

Reference Skirt visible slot coordinates:

- `WS0001`: `[22.5, 32]`
- `WS0002`: `[22.5, -32]`
- `WS0003`: `[41.5, 7]`
- `WS0004`: `[41.5, -7]`

## Implementation Steps

### 1. Baseline Reference and Collision Check

Tasks:

- Re-read `doc/raychen_design.md`.
- Inspect `tahlan_skirt.ship`.
- Inspect Skirt variants for source loadout conventions.
- Search vanilla/core and current mod data for `raychen`, `raychen_elite`, and `data/hulls/raychen.ship`.
- Confirm no ID collision like the earlier `nebula` problem.
- Confirm current RC8 weapon, hullmod, and ship-system IDs before choosing loadout.

Deliverable:

- Implementation notes in the final cycle summary.

Acceptance criteria:

- No vanilla/core collision for `raychen`.
- No stale or conflicting RayChen files exist before implementation.

### 2. Asset Preparation

Tasks:

- Create `Toranaga/graphics/ships/raychen.png`.
- Copy `tahlan_skirt.png` exactly for the first pass.
- Preserve reference dimensions: `100x124`.

Deliverable:

- `Toranaga/graphics/ships/raychen.png`

Acceptance criteria:

- File exists at the expected path.
- Hull definition references it correctly.
- Sprite remains byte-identical to the Skirt reference image.

### 3. Hull Definition

Tasks:

- Create `Toranaga/data/hulls/raychen.ship`.
- Define frigate hull size, sprite, bounds, center, shield, engine slots, and four visible weapon slots.
- Use Skirt geometry as the layout reference.
- Use no fighter bays for the first pass.
- Keep weapon slots aligned to the Skirt hardpoints.
- Use safe vanilla-compatible engine style values if the Tahlan engine styles are not available in this mod.

Deliverable:

- `Toranaga/data/hulls/raychen.ship`

Acceptance criteria:

- JSON parses successfully.
- Hull ID is `raychen`.
- Hull size is `FRIGATE`.
- Sprite path is `graphics/ships/raychen.png`.
- Ship has zero launch bays.
- Ship has four visible combat weapon slots.
- Shield settings use sane RC8 values, especially shield upkeep as a small multiplier.

### 4. Ship Data

Tasks:

- Add the RayChen row to `Toranaga/data/hulls/ship_data.csv`.
- Use baseline values from `doc/raychen_design.md`.
- Select a vanilla first-pass system, likely `maneuveringjets` unless testing or ID availability suggests a better fit.
- Do not add exploration-focused logistics hullmods.
- Keep fighter bays column as `0`.

Deliverable:

- Updated `Toranaga/data/hulls/ship_data.csv`

Acceptance criteria:

- CSV row has the correct number of fields.
- RayChen values parse into the intended columns.
- `shield upkeep` is a small multiplier, not a large flat number.
- Fighter bays column is `0`.
- `gameVersion` remains compatible with Starsector `0.98a-RC8`.

### 5. Default Variant

Tasks:

- Create `Toranaga/data/variants/raychen_elite.variant`.
- Fit vanilla RC8 weapons compatible with RayChen slots.
- Use no wings.
- Prioritize vents over capacitors.
- Choose weapons that exploit strong flux stats without turning the ship into a self-overload trap.

Deliverable:

- `Toranaga/data/variants/raychen_elite.variant`

Acceptance criteria:

- Variant references hull ID `raychen`.
- Variant ID is `raychen_elite`.
- Variant has no wing entries.
- Every weapon slot reference exists on `raychen.ship`.
- Every weapon ID exists in RC8 `weapon_data.csv` or verified current game data.

### 6. Description and Metadata

Tasks:

- Add RayChen description text to `Toranaga/data/strings/descriptions.csv`.
- Use the tone from `doc/raychen_design.md`: fast, technical, precise, and prestigious.
- Present the RayChen as the upper limit of frigate performance, not a carrier or mini cruiser.

Deliverable:

- Updated `Toranaga/data/strings/descriptions.csv`

Acceptance criteria:

- Description ID is `raychen`.
- Description type is `SHIP`.
- Text connects the RayChen to the Toranaga and DiAnn program family.
- CSV formatting remains valid.

### 7. Validation

Tasks:

- Parse all touched JSON files.
- Validate CSV field counts.
- Confirm referenced sprite exists.
- Confirm sprite dimensions match hull file.
- Confirm sprite hash matches the Skirt reference.
- Confirm hull has zero launch bays.
- Confirm variant has no wings.
- Confirm all variant weapon slots exist on the hull.
- Confirm all variant weapon IDs exist in available data.
- Search for common bad IDs and stale collision-prone IDs.
- Confirm no deployable `raychen` ID collision with vanilla/core data was found.

Deliverable:

- Validation summary in the final response.

Acceptance criteria:

- No malformed JSON.
- No malformed CSV rows.
- No missing sprite reference.
- No missing weapon or slot references.
- No vanilla ID collision.

### 8. Version Bump

Tasks:

- Update `Toranaga/mod_info.json`.
- Increment the mod `version` from the current value to the next minor or patch version for the RayChen implementation.
- Keep `gameVersion` set to Starsector `0.98a-RC8` unless the installed game version changes.

Deliverable:

- Updated `Toranaga/mod_info.json`

Acceptance criteria:

- Mod version changes as part of implementation.
- `gameVersion` remains `0.98a-RC8`.
- JSON parses successfully after the edit.

## First-Pass Tuning Targets

Use these as implementation defaults unless validation or testing requires adjustment:

- Ordnance points: 95
- Hull: 3,800
- Armor: 450
- Flux capacity: 10,000
- Flux dissipation: 950
- Fighter bays: 0
- Speed: 190
- Acceleration: 260
- Deceleration: 240
- Turn rate: 125
- Turn acceleration: 220
- Shield: omni, 360 arc, 0.03 upkeep, 0.35 efficiency
- Cargo: 35
- Fuel: 60
- Fuel/ly: 1
- Max burn: 12
- Crew: 12 minimum, 40 maximum
- Supplies/recovery: 8
- Supplies/month: 6
- CR to deploy: 12
- Peak CR seconds: 300

## First-Pass Weapon Direction

The source brief asks for a very powerful frigate, but the Skirt sprite only clearly supports four visible hardpoints. The first pass should preserve four mounts and make them strong instead of adding floating slots.

Recommended slot structure:

- `WS0001`: medium energy hardpoint at `[22.5, 32]`
- `WS0002`: medium energy hardpoint at `[22.5, -32]`
- `WS0003`: small energy hardpoint at `[41.5, 7]`
- `WS0004`: small energy hardpoint at `[41.5, -7]`

Possible elite loadout direction:

- `WS0001`: Pulse Laser or Heavy Blaster
- `WS0002`: Pulse Laser or Heavy Blaster
- `WS0003`: Ion Cannon or Tactical Laser
- `WS0004`: Ion Cannon or Tactical Laser

Final weapon IDs should be verified against available RC8 data during implementation.

## Risk Notes

- A frigate with this speed, shield efficiency, and flux dissipation may be dramatically stronger than intended even for an overpowered prototype.
- Four upgraded mounts may already be enough; adding the full seven-mount concept would likely require custom art or a visual slot editor.
- Shield upkeep must remain a small multiplier, not a flat flux value.
- Vanilla weapon IDs must be verified against RC8 before finalizing the variant.
- The Skirt source uses Tahlan custom weapons, systems, engine styles, hullmods, and a built-in wing that should not be copied blindly.
- The DiAnn/Nebula collision showed that ID uniqueness must be checked before implementation, not after symptoms appear in-game.

## Out of Scope for Dev Cycle 003

- Final balance.
- Final art.
- Custom campaign start.
- Custom ship system code.
- Custom hullmod code.
- Custom weapons.
- Custom wings or drones.
- Unique quest or recovery integration.
- Visual expansion to seven weapon mounts.

## Completion Definition

Dev Cycle 003 is complete when the repo contains a coherent first-pass RayChen implementation with:

- A RayChen hull file.
- A RayChen ship data row.
- A default `raychen_elite` variant.
- A RayChen sprite path and asset.
- Zero fighter bays.
- Description text.
- A bumped mod version in `Toranaga/mod_info.json`.
- Validation results confirming structure, asset references, slot references, and RC8 ID compatibility.

The result does not need to be final-balanced, but it should be ready for an in-game load, refit, and simulator test pass.

## Implementation Result

Status: Implemented in mod version `0.4.0`.

The first playable RayChen implementation was added under the existing `Toranaga/` mod folder.

Implemented files:

- `Toranaga/data/hulls/raychen.ship`
- `Toranaga/data/variants/raychen_elite.variant`
- `Toranaga/graphics/ships/raychen.png`
- Updated `Toranaga/data/hulls/ship_data.csv`
- Updated `Toranaga/data/strings/descriptions.csv`
- Updated `Toranaga/mod_info.json`

Implementation choices:

- Hull ID: `raychen`
- Elite variant ID: `raychen_elite`
- Hull size: `FRIGATE`
- Ship system: `maneuveringjets`
- Fighter bays: `0`
- Sprite: exact copy of `tahlan_skirt.png`
- Geometry: Skirt dimensions, center, shield, bounds, and slot coordinates preserved
- Engine styles: changed from Tahlan custom styles to vanilla `HIGH_TECH`
- Built-in hullmods: `advancedoptics`, `turretgyros`
- Elite variant hullmods: `hardenedshieldemitter`, `stabilizedshieldemitter`, `unstable_injector`

Elite loadout:

- `WS0001`: Pulse Laser (`pulselaser`)
- `WS0002`: Pulse Laser (`pulselaser`)
- `WS0003`: Ion Cannon (`ioncannon`)
- `WS0004`: Ion Cannon (`ioncannon`)

Validation notes:

- `raychen.ship` and `raychen_elite.variant` parse as JSON.
- The RayChen sprite is `100x124` and byte-identical to the Skirt reference sprite.
- The hull has four visible combat slots and zero launch bays.
- The elite variant has zero wings and references only existing RayChen slots.
- RC8 core data contains the chosen weapons, hullmods, and `maneuveringjets` system.
- No RC8 core `raychen` or `raychen_elite` collision was found.