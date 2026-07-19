# Dev Cycle 002: Nebula Class Ship Implementation

## Purpose

This plan turns the approved direction in `doc/nebula_design.md` into the first implementation cycle for the Nebula-class destroyer.

The design document remains the source of truth for ship identity, combat role, visual direction, baseline stats, weapon layout, two fighter bays, system direction, and campaign intent. This document is only the work plan for the implementation pass.

## Cycle Goal

Create a playable first version of the Nebula class inside the existing `Toranaga/` mod folder. The ship should load in Starsector, appear in refit, deploy in combat, use shields without passive flux failure, operate its two fighter bays, and serve as the foundation for later tuning.

## Scope

Included in this cycle:

- Add the Nebula hull definition.
- Add or stage the Nebula ship sprite.
- Add the default `nebula_elite` variant.
- Add two fighter bays.
- Add the initial weapon slot layout.
- Add baseline campaign and combat stats from `doc/nebula_design.md`.
- Add description text.
- Update existing CSV files under `Toranaga/data`.
- Bump the mod version in `Toranaga/mod_info.json`.
- Use existing vanilla weapons, wings, hullmods, and ship systems for the first playable pass.
- Validate JSON, CSV shape, asset references, weapon IDs, wing IDs, and slot references.

Deferred unless required for the ship to function:

- Custom Java hullmods.
- Custom Java ship-system implementation.
- Custom fighter wings.
- Campaign start or quest integration.
- Final balance.
- Final art polish.

## Source Design Commitments

The first implementation pass should preserve these decisions from `doc/nebula_design.md`:

- Hull size is `DESTROYER`.
- The ship is intentionally overpowered relative to vanilla destroyers.
- It is an aggressive direct-combat escort, not a dedicated carrier.
- It has exactly 2 fighter bays.
- It visually follows `tahlan_tress.png`.
- It shares a clear family resemblance with the Toranaga.
- It emphasizes shields, mobility, flux performance, and offensive initiative.
- It does not inherit the Toranaga's exploration-focused hullmods.

## Implementation Steps

### 1. Baseline Reference Check

Tasks:

- Re-read `doc/nebula_design.md`.
- Inspect `tahlan_tress.ship`.
- Inspect Tress variants for bay, missile, and fighter conventions.
- Compare vanilla destroyer and cruiser stats for sanity.
- Confirm current RC8 weapon, wing, hullmod, and ship-system IDs before choosing loadout.

Deliverable:

- Implementation notes in the final cycle summary.

### 2. Asset Preparation

Tasks:

- Create `Toranaga/graphics/ships/nebula.png`.
- Use the Tress sprite as the visual basis.
- Prefer an exact copy of `tahlan_tress.png` for the first pass unless explicitly changed before implementation.
- Preserve the reference dimensions: 188x134.

Deliverable:

- `Toranaga/graphics/ships/nebula.png`

Acceptance criteria:

- File exists at the expected path.
- Hull definition references it correctly.
- Sprite dimensions match the hull file.

### 3. Hull Definition

Tasks:

- Create `Toranaga/data/hulls/nebula.ship`.
- Define destroyer hull size, sprite, bounds, center, shield, engines, weapon slots, and two launch bays.
- Use Tress geometry as the layout reference.
- Upgrade weapon slots to match Nebula's direct-combat identity.
- Keep exactly two `LAUNCH_BAY` slots.

Deliverable:

- `Toranaga/data/hulls/nebula.ship`

Acceptance criteria:

- JSON parses successfully.
- Hull ID is `nebula`.
- Hull size is `DESTROYER`.
- Sprite path is `graphics/ships/nebula.png`.
- Ship has exactly 2 launch bays.
- Shield settings use sane RC8 values, especially shield upkeep as a multiplier such as `0.05`.

### 4. Ship Data

Tasks:

- Add the Nebula row to `Toranaga/data/hulls/ship_data.csv`.
- Use baseline values from `doc/nebula_design.md`.
- Select a vanilla first-pass system, likely `highenergyfocus` or `maneuveringjets`.
- Avoid the Toranaga shield-upkeep mistake by using RC8-style upkeep values.
- Do not add exploration-focused logistics hullmods.

Deliverable:

- Updated `Toranaga/data/hulls/ship_data.csv`

Acceptance criteria:

- CSV row has the correct number of fields.
- Nebula values parse into the intended columns.
- `shield upkeep` is a small multiplier, not a large flat number.
- Fighter bays column is `2`.

### 5. Default Variant

Tasks:

- Create `Toranaga/data/variants/nebula_elite.variant`.
- Fit vanilla RC8 weapons compatible with Nebula slots.
- Fit two wings.
- Prioritize vents over capacitors.
- Choose weapons that support sustained shield use rather than immediately overloading the ship.

Deliverable:

- `Toranaga/data/variants/nebula_elite.variant`

Acceptance criteria:

- Variant references hull ID `nebula`.
- Variant has exactly two wing entries.
- Every weapon slot reference exists on `nebula.ship`.
- Every weapon ID exists in RC8 `weapon_data.csv`.
- Every wing ID exists in RC8 `wing_data.csv`.

### 6. Description and Metadata

Tasks:

- Add Nebula description text to `Toranaga/data/strings/descriptions.csv`.
- Use the tone from `doc/nebula_design.md`: technical, prestigious, and connected to the Toranaga program.

Deliverable:

- Updated `Toranaga/data/strings/descriptions.csv`

Acceptance criteria:

- Description ID is `nebula`.
- Description type is `SHIP`.
- Text does not frame the Nebula as a dedicated carrier.
- CSV formatting remains valid.

### 7. Validation

Tasks:

- Parse all touched JSON files.
- Validate CSV field counts.
- Confirm referenced sprite exists.
- Confirm sprite dimensions match hull file.
- Confirm hull has exactly two launch bays.
- Confirm variant has exactly two wings.
- Confirm all variant weapon slots exist on the hull.
- Confirm all variant weapon IDs exist in RC8 core data.
- Confirm all variant wing IDs exist in RC8 core data.
- Search for common bad IDs from prior cycle, especially `burstpd`.

Deliverable:

- Validation summary in the final response.

Acceptance criteria:

- No malformed JSON.
- No malformed CSV rows.
- No missing sprite reference.
- No missing weapon, wing, or slot references.

### 8. Version Bump

Tasks:

- Update `Toranaga/mod_info.json`.
- Increment the mod `version` from the current value to the next patch version for the Nebula implementation.
- Keep `gameVersion` set to the current Starsector RC8 value unless the installed game version changes.

Deliverable:

- Updated `Toranaga/mod_info.json`

Acceptance criteria:

- Mod version changes as part of the implementation cycle.
- `gameVersion` remains compatible with Starsector `0.98a-RC8`.
- JSON parses successfully after the edit.
## First-Pass Tuning Targets

Use these as implementation defaults unless testing or schema constraints require adjustment:

- Ordnance points: 220
- Hull: 8,500
- Armor: 850
- Flux capacity: 22,000
- Flux dissipation: 1,900
- Fighter bays: 2
- Speed: 130
- Shield: omni, 360 arc, 0.05 upkeep, 0.40 efficiency
- Cargo: 120
- Fuel: 180
- Fuel/ly: 2
- Max burn: 11

## Risk Notes

- The Nebula's proposed weapon density may be too high for the Tress sprite and may need visual slot reduction.
- A destroyer with two large mounts, two bays, and very high flux stats may need later tuning after simulator testing.
- Vanilla weapon IDs must be verified against RC8 before finalizing the variant.
- Shield upkeep must remain a small multiplier, not a flat flux number.
- The default loadout should avoid high-flux traps like stacking plasma, heavy blasters, and burst PD all together.

## Phase 2: Weapon Slot Alignment

The initial Nebula implementation was promising, but in-game testing showed that several weapon mounts do not line up with the actual Tress-based sprite. Some mounts appear to float outside the hull, and the ship likely has too many visible weapons for the source art.

Phase 2 should correct the Nebula's visible weapon layout by matching the inspirational Tress ship's weapon count and physical placement.

### Phase 2 Goal

Revise the Nebula hull and default variant so the ship uses the same number of visible weapon mounts as the Tress reference, placed at the same locations on the sprite.

The weapon types may differ from Tress. The weapon count and placement should match Tress.

### Reference Layout

Use `inspiration/scalartech-solutions-0.9.3b/data/hulls/tahlan_tress.ship` as the placement source.

Tress visible combat weapon slots:

- `WS0001`: small energy turret at `[-5.5, 39]`, arc `233`, angle `81`
- `WS0002`: small energy turret at `[-5.5, -39]`, arc `233`, angle `-81`
- `WS0003`: medium missile hardpoint at `[55.5, 60]`, arc `5`, angle `0`
- `WS0004`: medium missile hardpoint at `[55.5, -60]`, arc `5`, angle `0`

Tress non-combat/decorative slots:

- `WS0005`: large decorative engine slot at `[-43, -82]`, angle `-150`
- `WS0006`: large decorative engine slot at `[-43, 82]`, angle `150`

Tress launch bays:

- `LB 1`: upper hidden launch bay using the Tress coordinates
- `LB 2`: lower hidden launch bay using the Tress coordinates

### Phase 2 Implementation Tasks

- Update `Toranaga/data/hulls/nebula.ship`.
- Remove extra Nebula visible weapon slots that do not exist on the Tress reference.
- Keep exactly four visible combat weapon slots unless a later reviewed design explicitly changes this.
- Place the four visible combat weapon slots at the Tress coordinates listed above.
- Keep exactly two launch bays using Tress launch bay coordinates.
- Keep or restore the two decorative engine slots only if they improve visual fidelity and do not appear in the refit UI as usable weapons.
- Update `Toranaga/data/variants/nebula_elite.variant` so it only references the remaining visible combat slots.
- Choose weapon types that fit the reduced slot count while preserving the Nebula's elite destroyer identity.
- Reconsider OP, flux, and weapon loadout after reducing the mount count.
- Bump `Toranaga/mod_info.json` version after the Phase 2 correction.

### Phase 2 Elite Loadout

Use this four-weapon loadout for the Phase 2 `nebula_elite` variant unless implementation testing shows a hard compatibility issue:

- `WS0001`: `gravitonbeam`
- `WS0002`: `pulselaser`
- `WS0003`: `pulselaser`
- `WS0004`: `phasebeam`

Design intent:

- Keep all four weapons medium-scale or smaller so the loadout fits the Tress sprite.
- Avoid forcing an Autopulse Laser or other large weapon onto a hull position that does not visually support it.
- Preserve the elite variant identity through Graviton Beam shield pressure, two Pulse Lasers for general damage, and Phase Lance burst finishing.
- Recheck flux behavior after implementation, but this loadout should be much safer than the Phase 1 weapon density.
### Phase 2 Acceptance Criteria

- No usable weapon appears to float outside the Nebula sprite.
- Nebula visible combat weapon count matches Tress: 4 visible combat mounts.
- Nebula visible combat weapon coordinates match Tress.
- Nebula still has exactly two fighter bays.
- `nebula_elite.variant` references only existing Nebula weapon slots.
- All weapon IDs exist in RC8 core data.
- All wing IDs exist in RC8 core data.
- JSON and CSV validation pass.
- The mod version is bumped after the fix.
## Phase 3: Sprite Composition and Visual Alignment

After Phase 2, the Nebula uses the correct number of visible combat mounts and the Tress reference coordinates, but in-game testing still suggests a larger visual alignment problem. The shield, weapons, and ship image do not appear to agree visually. The likely issue is not just individual weapon slot placement; it may be that the visible Nebula sprite does not match the full visual composition expected by the original Tress hull.

The Tress reference appears to use its base ship sprite together with decorative built-in visual slots, especially engine/nacelle visuals. If those visuals are not baked into `nebula.png` or recreated safely as non-usable decorative elements, the ship can appear visually offset or incomplete even when the numeric hull center is correct.

### Phase 3 Goal

Make the Nebula's visible sprite, shield, collision feel, and weapon positions agree in-game.

This phase should prioritize what the player sees in combat over blind reuse of source coordinates.

### Phase 3 Diagnostic Tasks

- Compare `Toranaga/graphics/ships/nebula.png` against the full in-game appearance of `tahlan_tress` if available.
- Inspect Tress decorative built-in weapon slots, especially `WS0005` and `WS0006` using `tahlan_filamentengine`.
- Determine whether Tress's apparent sprite shape depends on decorative/scripted weapon visuals that are not present in Nebula.
- Generate or update a slot overlay image showing:
  - sprite bounds
  - hull center/origin
  - shield radius
  - visible weapon slots
  - launch bay locations if helpful
- Compare the overlay to an in-game screenshot before changing data.

### Phase 3 Implementation Options

Option A: Bake Missing Visuals Into Sprite

- Compose a new `Toranaga/graphics/ships/nebula.png` that includes the visual pieces needed to match the Tress in-game silhouette.
- Keep the final PNG dimensions at 188x134 unless testing proves a larger canvas is needed.
- Recalculate `center`, `shieldCenter`, `shieldRadius`, bounds, and weapon slots after baking the sprite.

Option B: Add Safe Decorative Slots

- Add non-usable decorative slots equivalent to Tress's visual-only engine/nacelle slots.
- Only use this option if the needed decorative assets can be included without custom Java dependencies or missing weapon spec errors.
- Decorative slots must not appear as player-usable weapon mounts.

Option C: Hand-Align Current Sprite

- Keep the current exact Tress base sprite.
- Adjust `center`, `shieldCenter`, `shieldRadius`, and the four visible weapon slot locations based on the actual sprite appearance in-game.
- Use this if the base sprite is visually complete enough and only needs practical alignment.

### Phase 3 Acceptance Criteria

- The Nebula appears centered inside its shield during combat.
- Shields visually cover the ship without excessive empty offset to one side.
- The four visible weapons appear mounted on the hull, not floating outside it.
- Fighter bay behavior remains intact with exactly two bays.
- The Nebula sprite remains visually consistent with the Tress inspiration.
- JSON and CSV validation pass.
- All weapon, wing, and optional decorative IDs exist in RC8 or are supplied by the mod.
- The mod version is bumped after the visual-alignment fix.


### Phase 3 Alignment Attempt Log

This log tracks each Nebula visual-alignment attempt so future changes can build from observed evidence instead of repeating the same correction.

| Version | Change Tried | Evidence / Reasoning | Observed Result | Current Interpretation |
| --- | --- | --- | --- | --- |
| `0.2.2` | Changed hull `center` from `[94, 66.5]` to `[125, 95]` and reduced `shieldRadius` from `125.5` to `112`. | First combat screenshot made the ship appear low/right inside the shield, suggesting the rendered sprite might be offset from the combat origin. | User reported the ship was still incorrectly offset. The later grid screenshot showed weapon and bay markers still visibly above the hull. | Manual center correction was not the right primary fix, or Starsector's visible marker issue was dominated by slot locations rather than sprite origin. |
| `0.2.3` | Reverted to original Tress source geometry: `center: [94, 66.5]`, `shieldCenter: [0, 0]`, `shieldRadius: 125.5`. | The copied Nebula sprite is byte-for-byte identical to `tahlan_tress.png`, and the original `tahlan_tress.ship` uses those exact geometry values. | User reported it did not look like there was any change. | The deployed data path was verified, so the lack of visible improvement implies that the grid problem is probably not fixed by hull center/shield values alone. |
| `0.2.4` | Shifted the four visible combat mounts and both launch-bay exit paths aft by `50` units. Kept the sprite, center, shield center, and shield radius at Tress source values. | In the grid screenshot, weapon/bay markers appeared ahead of the visible hull. Since center changes did not produce an obvious correction, the next test targeted the slot coordinate system directly. | User reported this was much closer. The grid screenshot showed the markers moved substantially toward the hull, confirming Starsector is consuming the edited `.ship` slot coordinates. The hardpoint squares still appeared slightly too far forward. | Continue tuning the slot coordinates aft in smaller increments rather than changing sprite center or shield geometry. |
| `0.2.5` | Shifted the same four visible combat mounts and both launch-bay exit paths aft by another `25` units, for a total aft shift of `75` units from the original Tress coordinates. | The `0.2.4` screenshot confirmed the direction was correct but not quite enough. A smaller second pass tested whether continuing in the same direction would finish the alignment. | User reported this made the alignment worse and made the ship appear larger relative to the markers. No sprite scale fields were changed, so this was treated as an overshoot/visual-context problem rather than an intentional scaling change. | Back off from the 75-unit shift. Try an intermediate total shift and avoid changing sprite center, dimensions, shield geometry, or image scale. |
| `0.2.6` | Set the four visible combat mounts and both launch-bay exit paths to a total aft shift of `60` units from the original Tress coordinates. This backed off `15` units from the overshot `0.2.5` pass while remaining `10` units aft of the closer `0.2.4` pass. | The `0.2.4` result was much closer and `0.2.5` was worse, so this tested a conservative intermediate value. | User was unsure it improved anything and expressed fatigue with repeated screenshot/deploy iterations. | Stop blind shared-offset tuning. The process is too slow and may still require many iterations. Build or use a visual ship-slot editor/calibration workflow before making more coordinate changes. |

Open diagnostic questions:

- Does the refit/simulator UI show the expected deployed mod version after restart?
- When using future calibration output, do weapon/bay markers land on the intended hull features in one deploy/test pass?
- Are the blue circular markers in the screenshot fighter/bay indicators, weapon indicators, or both?
- Does Starsector require a full application restart, not just reloading a save or refit screen, before hull-spec coordinate changes appear?
- Is the screenshot from the Nebula hull specifically, not a stale variant or another ship using the same sprite?

### Phase 3 Process Decision

The repeated deploy-and-screenshot loop is no longer an efficient way to align the Nebula. Versions `0.2.4`, `0.2.5`, and `0.2.6` proved that `.ship` slot coordinates are being consumed by Starsector, but they also showed that shared numeric offsets are a poor tool for final placement. Even when the direction is correct, the user has to restart/test/screenshot repeatedly, and different markers may need independent tuning.

Before making further Nebula alignment changes, switch to a visual workflow:

- Preferred: use a Starsector ship editor capable of loading `nebula.png` and editing/exporting `.ship` weapon and bay coordinates directly.
- Fallback: create a local utility under `utilities/` that renders `nebula.png`, the `.ship` center, shield, weapon slots, bay points, and grid into an overlay image, then use that overlay to choose coordinates before deploying.
- Baseline recommendation: treat `0.2.4` as the best observed alignment so far, `0.2.5` as an overshoot, and `0.2.6` as inconclusive. Do not continue adding shared offsets without a visual editor/overlay.
### Phase 3 Notes

The measured PNG alpha bounds place the current Nebula sprite close to `center: [94, 66.5]`, so the raw image is not obviously off-center by bounding-box math. The in-game problem may come from a mismatch between the Tress base sprite and the full Tress visual composition. Phase 3 should verify that before making another broad numerical adjustment.
## Out of Scope for Dev Cycle 002

- Custom Nebula ship system Java.
- Custom Nebula hullmod Java.
- Custom wings or weapons.
- Campaign start integration.
- Special recovery content.
- Final balance pass.
- Final custom art beyond the Tress-based first-pass sprite.

## Completion Definition

Dev Cycle 002 is complete when the repo contains a coherent first-pass Nebula implementation with:

- A Nebula hull file.
- A Nebula ship data row.
- A default `nebula_elite` variant.
- A Nebula sprite path and asset.
- Exactly two fighter bays.
- Description text.
- A bumped mod version in `Toranaga/mod_info.json`.
- Validation results confirming structure and RC8 ID compatibility.

The result does not need to be final-balanced, but it should be ready for an in-game load, refit, and simulator test pass.

### Phase 3 Implementation Result

Status: Implemented in mod version `0.2.2`.

The first Phase 3 pass keeps `nebula.png` as an exact copy of the Tress reference sprite and applies a conservative in-game alignment correction instead of redrawing the ship. The Nebula hull center is adjusted from `[94, 66.5]` to `[125, 95]` so the visible sprite moves up and left relative to the combat origin, matching the screenshot symptom where the ship rendered low and right inside its shield. The shield radius is tightened from `125.5` to `112` while leaving `shieldCenter` at `[0, 0]`.

Phase 2 combat-slot and bay constraints remain unchanged: four visible combat mounts, two fighter bays, and the elite loadout of Graviton Beam, Pulse Laser, Pulse Laser, and Phase Lance.
### Phase 3 Correction Result

Status: Implemented in mod version `0.2.3`.

The grid screenshot showed the first manual center adjustment still left weapon and bay markers visually separated from the ship. After comparing Nebula against the original `tahlan_tress.ship`, the manual offset was reversed. Because `nebula.png` is an exact copy of `tahlan_tress.png`, Nebula now uses the Tress source geometry again: `center: [94, 66.5]`, `shieldCenter: [0, 0]`, and `shieldRadius: 125.5`.

The Phase 2 mount count remains unchanged: four visible combat mounts and two fighter bays. The custom elite loadout remains Graviton Beam, Pulse Laser, Pulse Laser, and Phase Lance.
### Phase 3 Slot Alignment Result

Status: Implemented in mod version `0.2.4`.

The grid screenshot after `0.2.3` showed that restoring the Tress hull center did not visibly improve the problem. That indicates the main issue is not the sprite center but the usable slot and launch-bay coordinates relative to the adapted Nebula visual. The four visible combat mounts and both launch-bay exit paths were shifted aft by `50` Starsector units, leaving the sprite, hull center, shield center, and shield radius at the original Tress source values.

This pass keeps the same four-weapon elite loadout and two fighter bays, but intentionally breaks from the exact Tress slot coordinates so the visible markers sit on the Nebula hull in Starsector's grid view.
### Phase 3 Second Slot Alignment Result

Status: Implemented in mod version `0.2.5`.

The `0.2.4` grid screenshot showed the aft slot shift was the correct direction and that Starsector is using the edited Nebula `.ship` coordinates. The markers were much closer to the hull, but the visible hardpoint squares still appeared too far forward. This pass shifts the same four combat mounts and both launch-bay exit paths aft by another `25` units, for a total aft shift of `75` units from the original Tress coordinates.

The ship sprite, hull center, shield center, shield radius, four-weapon elite loadout, and two-bay layout are otherwise unchanged.
### Phase 3 Intermediate Slot Alignment Result

Status: Implemented in mod version `0.2.6`.

The `0.2.5` screenshot showed that a total `75`-unit aft slot shift was worse than `0.2.4`. This pass backs off to a total `60`-unit aft shift from the original Tress coordinates: `10` units farther aft than the closer `0.2.4` result, but `15` units forward from the overshot `0.2.5` result.

No sprite scale, sprite dimensions, hull center, shield center, or shield radius were changed in this pass. If the ship still appears scaled differently in-game, that should be treated as a refit-view/camera perception issue or a separate hull-display setting, not a direct sprite-scale edit from this cycle.
## Phase 4: DiAnn Rename and Hull ID Collision Fix

Fable's analysis in `doc/Fable_nebula_placement.md` identified the real root cause of the Phase 3 placement failure: the modded hull ID and file path `nebula` collided with Starsector's vanilla Nebula civilian transport. The vanilla ship also uses `data/hulls/nebula.ship` and hull ID `nebula`, which explains the impossible mixed symptoms from the screenshots: the Tress-based sprite appeared, but vanilla small ballistic slot markers and vanilla-centered geometry bled into the in-game refit display.

This means the Phase 3 visual tuning attempts were working against a contaminated hull spec. The correct fix is not further coordinate tuning; it is to give the ship a unique mod-prefixed identity and restore the original Tress geometry.

### Phase 4 Goal

Rename the former Nebula-class ship to the DiAnn class, remove all deployable `nebula` hull/variant/description collisions, and restore exact Tress placement data under a unique namespaced ID.

### Phase 4 Implementation

- Rename `Toranaga/data/hulls/nebula.ship` to `Toranaga/data/hulls/trng_diann.ship`.
- Set the hull spec to player-facing `hullName: "DiAnn"` and internal `hullId: "trng_diann"`.
- Rename `Toranaga/data/variants/nebula_elite.variant` to `Toranaga/data/variants/trng_diann_elite.variant`.
- Set the elite variant to `hullId: "trng_diann"` and `variantId: "trng_diann_elite"`.
- Rename the sprite from `Toranaga/graphics/ships/nebula.png` to `Toranaga/graphics/ships/trng_diann.png` and update `spriteName` accordingly.
- Change the `ship_data.csv` row from `Nebula,nebula,...` to `DiAnn,trng_diann,...`.
- Change the description row ID from `nebula` to `trng_diann` and update the display text to DiAnn-class language.
- Restore exact Tress geometry and slot locations:
  - `center: [94, 66.5]`
  - `shieldCenter: [0, 0]`
  - `shieldRadius: 125.5`
  - `WS0001: [-5.5, 39]`
  - `WS0002: [-5.5, -39]`
  - `WS0003: [55.5, 60]`
  - `WS0004: [55.5, -60]`
  - `LB 1: [30, 48.5, 19.5, 42.5, 9.5, 33.5]`
  - `LB 2: [8, -32.5, 15.5, -39, 26.5, -45.5]`
- Bump the mod version to `0.3.0`, because this is a behavior-level collision fix rather than another placement tweak.

### Phase 4 Acceptance Criteria

- No deployable mod file uses `data/hulls/nebula.ship`, `data/variants/nebula_elite.variant`, or `graphics/ships/nebula.png`.
- No deployable Toranaga data file references `hullId: "nebula"`, `variantId: "nebula_elite"`, or description ID `nebula`.
- The DiAnn sprite remains byte-identical to the Tress reference image.
- The DiAnn hull uses exact Tress center, shield radius, weapon slot coordinates, and launch-bay coordinates.
- The elite variant still uses the approved loadout: Graviton Beam, Pulse Laser, Pulse Laser, and Phase Lance.
- The mod deploys as version `0.3.0`.
- In-game refit should show exactly the DiAnn's four intended weapon mounts and two bays, with no vanilla small ballistic Nebula ghost slots.

### Phase 4 Result

Status: Implemented in mod version `0.3.0`.

The former Nebula is now the DiAnn class with internal ID `trng_diann`. The old `nebula` hull ID was removed from deployable mod data to avoid colliding with Starsector's vanilla Nebula civilian transport. The previous Phase 3 coordinate offsets were reverted to exact Tress values, since Fable's analysis showed the geometry itself was not the original problem.
## Phase 5: DiAnn ID Simplification and Elite Slot Remap

After the Phase 4 collision fix proved the DiAnn placement was much better, the current direction is to keep the ship name simple and remove the `trng_` prefix from the DiAnn hull and elite variant. The important collision to avoid was the vanilla `nebula` ID; `diann` is unique enough for this mod's current scope and is easier to use in console/testing.

### Phase 5 Goal

Use plain DiAnn IDs and adjust the elite variant's weapon placement so the Phase Lance occupies slot 2 while slots 3 and 4 are Pulse Lasers.

### Phase 5 Implementation

- Rename `Toranaga/data/hulls/trng_diann.ship` to `Toranaga/data/hulls/diann.ship`.
- Rename `Toranaga/data/variants/trng_diann_elite.variant` to `Toranaga/data/variants/diann_elite.variant`.
- Rename `Toranaga/graphics/ships/trng_diann.png` to `Toranaga/graphics/ships/diann.png`.
- Change hull ID from `trng_diann` to `diann`.
- Change variant ID from `trng_diann_elite` to `diann_elite`.
- Change the sprite path to `graphics/ships/diann.png`.
- Change `ship_data.csv` and `descriptions.csv` IDs from `trng_diann` to `diann`.
- Keep the exact Tress geometry restored in Phase 4.
- Update the elite loadout to:
  - `WS0001`: Graviton Beam (`gravitonbeam`)
  - `WS0002`: Phase Lance (`phasebeam`)
  - `WS0003`: Pulse Laser (`pulselaser`)
  - `WS0004`: Pulse Laser (`pulselaser`)
- Bump the mod version to `0.3.1`.

### Phase 5 Acceptance Criteria

- The deployable mod uses `diann` and `diann_elite` as the current IDs.
- No deployable file path or live data field uses `trng_diann` or `trng_diann_elite`.
- The old vanilla-colliding `nebula` ID remains absent from deployable DiAnn data.
- The elite variant has Phase Lance in slot 2 and Pulse Lasers in slots 3 and 4.
- The DiAnn sprite remains byte-identical to the Tress reference image.
- The mod deploys as version `0.3.1`.

### Phase 5 Result

Status: Implemented in mod version `0.3.1`.

The DiAnn now uses plain IDs: `diann` for the hull and `diann_elite` for the elite variant. The elite weapon mapping was updated so `WS0002` carries the Phase Lance and both `WS0003` and `WS0004` carry Pulse Lasers. The `trng_` prefix is no longer used by the current deployable DiAnn files or data.