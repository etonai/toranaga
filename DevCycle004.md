# Dev Cycle 004: Hahn Class Frigate Implementation

## Purpose

This plan turns the approved direction in `doc/hahn_design.md` into the first implementation cycle for the Hahn-class frigate.

The design document remains the source of truth for ship identity, combat role, visual direction, baseline stats, weapon layout, system direction, and campaign intent. This document is the work plan for the first playable implementation pass.

## Cycle Goal

Create a playable first version of the Hahn class inside the existing `Toranaga/` mod folder. The ship should load in Starsector, appear in refit, deploy in combat, use shields without passive flux failure, and behave as an elite overpowered frigate based on the Tahlan Curl reference — distinct in feel from its sibling, the RayChen.

## Scope

Included in this cycle:

- Add the Hahn hull definition.
- Add or stage the Hahn ship sprite.
- Add the default `hahn_elite` variant.
- Add baseline campaign and combat stats from `doc/hahn_design.md`.
- Add description text.
- Update existing CSV files under `Toranaga/data`.
- Bump the mod version in `Toranaga/mod_info.json`.
- Use existing vanilla weapons, hullmods, and ship systems for the first playable pass.
- Validate JSON, CSV shape, asset references, weapon IDs, hullmod IDs, system IDs, and slot references.
- Confirm there is no ID or file-path collision with vanilla Starsector data, or with the existing RayChen/DiAnn/Toranaga content, before implementation.

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

The first implementation pass should preserve these decisions from `doc/hahn_design.md`:

- Hull size is `FRIGATE`.
- The ship is intentionally overpowered relative to vanilla frigates.
- It is a fast elite interceptor and hunter-killer, not a mini cruiser.
- It shares the RayChen's design philosophy and mission but is a distinct sibling built from a different source hull, not a reskin.
- It visually follows `tahlan_curl.png`.
- It should copy the Curl sprite exactly for the first implementation.
- It should preserve the Curl dimensions, center, off-center shield geometry, bounds, and all six engine slots unless testing proves otherwise.
- It should use `hahn` and `hahn_elite` as the current IDs.
- It should not collide with vanilla Starsector hull IDs, variant IDs, description IDs, or file paths, nor with existing Toranaga mod content (`raychen`, `raychen_elite`, `diann`, `toranaga`, etc.).
- It should not have fighter bays in the first pass.
- It should use all five visible mounts from the Curl hardpoint/turret layout (two missile hardpoints, one fixed energy hardpoint, two energy turrets), giving it a missile-opener/turret-brawler identity distinct from the RayChen's all-fixed-forward energy layout.

## Reference Data

Use these ScalarTech files as implementation references:

- Sprite: `inspiration/scalartech-solutions-0.9.3b/graphics/tahlan/ships/tahlan_curl.png`
- Hull: `inspiration/scalartech-solutions-0.9.3b/data/hulls/tahlan_curl.ship`
- Variant: `inspiration/scalartech-solutions-0.9.3b/data/variants/tahlan_curl_combat.variant`
- Variant: `inspiration/scalartech-solutions-0.9.3b/data/variants/tahlan_curl_escort.variant`
- Variant: `inspiration/scalartech-solutions-0.9.3b/data/variants/tahlan_curl_standard.variant`

Reference Curl geometry:

- Width: `108`
- Height: `105`
- Center: `[54, 60]`
- Collision radius: `80`
- Shield center: `[-3.5, 0]` (off-center — preserve rather than correct to `[0, 0]`)
- Shield radius: `71.5`
- Bounds: copy from `tahlan_curl.ship`
- Engine slots: copy all six from `tahlan_curl.ship`, adapting engine style to a safe vanilla style if Tahlan custom styles are unavailable (matches the RayChen precedent of swapping to vanilla `HIGH_TECH`).

Reference Curl visible slot coordinates:

- `WS0001`: small missile hardpoint at `[34, 19]`, arc 5°
- `WS0002`: small missile hardpoint at `[34, -19]`, arc 5°
- `WS0003`: small energy hardpoint at `[39, 0]`, arc 5°
- `WS0004`: small energy turret at `[10, 17]`, arc 180°
- `WS0005`: small energy turret at `[10, -17]`, arc 180°

## Implementation Steps

### 1. Baseline Reference and Collision Check

Tasks:

- Re-read `doc/hahn_design.md`.
- Inspect `tahlan_curl.ship`.
- Inspect Curl variants for source loadout conventions.
- Search vanilla/core and current mod data for `hahn`, `hahn_elite`, and `data/hulls/hahn.ship`.
- Confirm no ID collision like the earlier `nebula` problem, and no collision with the existing `raychen`/`raychen_elite` content.
- Confirm current RC8 weapon, hullmod, and ship-system IDs before choosing loadout.

Deliverable:

- Implementation notes in the final cycle summary.

Acceptance criteria:

- No vanilla/core or existing-mod collision for `hahn`.
- No stale or conflicting Hahn files exist before implementation.

### 2. Asset Preparation

Tasks:

- Create `Toranaga/graphics/ships/hahn.png`.
- Copy `tahlan_curl.png` exactly for the first pass.
- Preserve reference dimensions: `108x105`.

Deliverable:

- `Toranaga/graphics/ships/hahn.png`

Acceptance criteria:

- File exists at the expected path.
- Hull definition references it correctly.
- Sprite remains byte-identical to the Curl reference image.

### 3. Hull Definition

Tasks:

- Create `Toranaga/data/hulls/hahn.ship`.
- Define frigate hull size, sprite, bounds, center, shield, all six engine slots, and all five visible weapon slots.
- Use Curl geometry as the layout reference, including the off-center shield.
- Use no fighter bays for the first pass.
- Keep weapon slots aligned to the Curl hardpoints and turrets, including correct mount types and arcs.
- Use safe vanilla-compatible engine style values if the Tahlan engine styles are not available in this mod.

Deliverable:

- `Toranaga/data/hulls/hahn.ship`

Acceptance criteria:

- JSON parses successfully.
- Hull ID is `hahn`.
- Hull size is `FRIGATE`.
- Sprite path is `graphics/ships/hahn.png`.
- Ship has zero launch bays.
- Ship has five visible combat weapon slots: two missile, three energy (one hardpoint, two turrets).
- Shield settings use sane RC8 values, especially shield upkeep as a small multiplier.

### 4. Ship Data

Tasks:

- Add the Hahn row to `Toranaga/data/hulls/ship_data.csv`.
- Use baseline values from `doc/hahn_design.md`.
- Select a vanilla first-pass system, likely `maneuveringjets` unless testing or ID availability suggests a better fit.
- Do not add exploration-focused logistics hullmods.
- Keep fighter bays column as `0`.

Deliverable:

- Updated `Toranaga/data/hulls/ship_data.csv`

Acceptance criteria:

- CSV row has the correct number of fields.
- Hahn values parse into the intended columns.
- `shield upkeep` is a small multiplier, not a large flat number.
- Fighter bays column is `0`.
- `gameVersion` remains compatible with Starsector `0.98a-RC8`.

### 5. Default Variant

Tasks:

- Create `Toranaga/data/variants/hahn_elite.variant`.
- Fit vanilla RC8 weapons compatible with Hahn slots: light strike missiles on `WS0001`/`WS0002`, an energy weapon on `WS0003`, and tracking-friendly energy weapons on the `WS0004`/`WS0005` turrets.
- Use no wings.
- Prioritize vents over capacitors.
- Choose weapons that exploit strong flux stats without turning the ship into a self-overload trap.

Deliverable:

- `Toranaga/data/variants/hahn_elite.variant`

Acceptance criteria:

- Variant references hull ID `hahn`.
- Variant ID is `hahn_elite`.
- Variant has no wing entries.
- Every weapon slot reference exists on `hahn.ship`.
- Every weapon ID exists in RC8 `weapon_data.csv` or verified current game data.

### 6. Description and Metadata

Tasks:

- Add Hahn description text to `Toranaga/data/strings/descriptions.csv`.
- Use the tone from `doc/hahn_design.md`: fast, technical, precise, and prestigious.
- Present the Hahn as a parallel line of development to the RayChen within the same program, not a reskin, upgrade, or carrier.

Deliverable:

- Updated `Toranaga/data/strings/descriptions.csv`

Acceptance criteria:

- Description ID is `hahn`.
- Description type is `SHIP`.
- Text connects the Hahn to the Toranaga, DiAnn, and RayChen program family.
- CSV formatting remains valid.

### 7. Validation

Tasks:

- Parse all touched JSON files.
- Validate CSV field counts.
- Confirm referenced sprite exists.
- Confirm sprite dimensions match hull file.
- Confirm sprite hash matches the Curl reference.
- Confirm hull has zero launch bays.
- Confirm variant has no wings.
- Confirm all variant weapon slots exist on the hull.
- Confirm all variant weapon IDs exist in available data.
- Search for common bad IDs and stale collision-prone IDs.
- Confirm no `hahn` ID collision with vanilla/core data or existing Toranaga mod content was found.

Deliverable:

- Validation summary in the final response.

Acceptance criteria:

- No malformed JSON.
- No malformed CSV rows.
- No missing sprite reference.
- No missing weapon or slot references.
- No vanilla or in-mod ID collision.

### 8. Version Bump

Tasks:

- Update `Toranaga/mod_info.json`.
- Increment the mod `version` from `0.4.0` to `0.5.0` for the Hahn implementation.
- Keep `gameVersion` set to Starsector `0.98a-RC8` unless the installed game version changes.

Deliverable:

- Updated `Toranaga/mod_info.json`

Acceptance criteria:

- Mod version changes from `0.4.0` to `0.5.0` as part of implementation.
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
- Speed: 185
- Acceleration: 255
- Deceleration: 235
- Turn rate: 130
- Turn acceleration: 220
- Shield: omni, 360 arc, 0.03 upkeep, 0.35 efficiency, off-center per Curl geometry
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

The source brief asks for a very powerful frigate, but the Curl sprite only clearly supports five visible mounts. The first pass should preserve all five and make them strong instead of adding floating slots.

Recommended slot structure:

- `WS0001`: small missile hardpoint at `[34, 19]`
- `WS0002`: small missile hardpoint at `[34, -19]`
- `WS0003`: medium energy hardpoint at `[39, 0]`
- `WS0004`: small energy turret at `[10, 17]`, 180° arc
- `WS0005`: small energy turret at `[10, -17]`, 180° arc

Possible elite loadout direction:

- `WS0001`: Harpoon MRM or Sabot Pod
- `WS0002`: Harpoon MRM or Sabot Pod
- `WS0003`: Pulse Laser or Heavy Blaster
- `WS0004`: Tactical Laser or Ion Cannon
- `WS0005`: Tactical Laser or Ion Cannon

Final weapon IDs should be verified against available RC8 data during implementation.

## Risk Notes

- A frigate with this speed, shield efficiency, and flux dissipation may be dramatically stronger than intended even for an overpowered prototype, same as the RayChen precedent.
- Five upgraded mounts may already be enough; adding the full seven-mount concept would likely require custom art or a visual slot editor.
- Shield upkeep must remain a small multiplier, not a flat flux value.
- Vanilla weapon IDs must be verified against RC8 before finalizing the variant.
- The Curl source uses Tahlan custom weapons, systems, engine styles, and hullmods that should not be copied blindly.
- The off-center shield geometry (`[-3.5, 0]`) is a deliberate identity choice per `doc/hahn_design.md`; do not silently "fix" it to `[0, 0]` during implementation.
- The turret-mounted slots (`WS0004`/`WS0005`) behave differently in the AI and in player control than the RayChen's fixed hardpoints — verify tracking and arc behavior in testing rather than assuming parity.
- The DiAnn/Nebula collision showed that ID uniqueness must be checked before implementation, not after symptoms appear in-game; this now also applies to checking against the RayChen's own IDs.

## Out of Scope for Dev Cycle 004

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

Dev Cycle 004 is complete when the repo contains a coherent first-pass Hahn implementation with:

- A Hahn hull file.
- A Hahn ship data row.
- A default `hahn_elite` variant.
- A Hahn sprite path and asset.
- Zero fighter bays.
- Description text.
- A bumped mod version (`0.4.0` → `0.5.0`) in `Toranaga/mod_info.json`.
- Validation results confirming structure, asset references, slot references, and RC8 ID compatibility.

The result does not need to be final-balanced, but it should be ready for an in-game load, refit, and simulator test pass alongside the RayChen.

## Implementation Result

Status: Not yet implemented. This dev cycle is a plan pending execution.
