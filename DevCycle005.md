# Dev Cycle 005: Ronald Martin and Brian Stokes Mitchell Implementation

## Purpose

This plan turns the approved directions in `doc/ronaldmartin_design.md` and `doc/brianstokesmitchell_design.md` into the first playable implementation cycle for two new Toranaga-program ships:

- Ronald Martin-class exploration cruiser.
- Brian Stokes Mitchell-class assault destroyer.

The design documents remain the source of truth for identity, combat role, visual direction, baseline statistics, weapon geometry, and campaign intent. This document defines the implementation work, validation requirements, and completion gate.

## Cycle Goal

Create the basic hull and a complete elite variant for each class inside the existing `Toranaga/` mod folder.

At the end of the cycle, both ships must:

- Load successfully in Starsector `0.98a-RC8`.
- Appear correctly in refit.
- Deploy and function in combat.
- Use only available assets and verified game IDs.
- Preserve the geometry of their Gensoukyou reference hulls.
- Have a fully equipped elite variant suitable for simulator testing.
- Remain mechanically distinct from each other and from the existing Toranaga family.
- Ship with an increased mod version in `Toranaga/mod_info.json`.

In this plan, “basic ship” means the reusable hull specification, ship-data row, sprite, and description. “Elite version” means the fully fitted player-facing `.variant` built from that hull. Separate unconfigured `standard` variants are not required.

## Scope

Included in this cycle:

- Create the Ronald Martin basic hull.
- Create the `ronaldmartin_elite` variant.
- Create the Brian Stokes Mitchell basic hull.
- Create the `brianstokesmitchell_elite` variant.
- Copy and stage both reference sprites.
- Preserve reference bounds, centers, shields, engine slots, and weapon coordinates.
- Add first-pass combat and campaign statistics.
- Add descriptions for both ships.
- Update shared hull and string CSV files.
- Use verified vanilla weapons, hullmods, and ship systems for the first playable pass.
- Replace all Gensoukyou-specific styles, hullmods, weapons, and other dependencies.
- Validate IDs, JSON, CSV shape, assets, slots, loadouts, systems, hullmods, and built-ins.
- Increase the mod version in `Toranaga/mod_info.json` from `0.5.0` to `0.6.0`.

Deferred unless required for a functional first pass:

- Custom Java ship systems.
- Custom Java hullmods.
- Custom weapons or weapon effects.
- Custom acquisition missions or campaign events.
- Final balance.
- Final sprite recoloring or art polish.
- New fighter wings or drones.

## Naming Decision

Use the following IDs during this cycle:

| Content | ID |
| --- | --- |
| Ronald Martin hull | `ronaldmartin` |
| Ronald Martin elite variant | `ronaldmartin_elite` |
| Brian Stokes Mitchell hull | `brianstokesmitchell` |
| Brian Stokes Mitchell elite variant | `brianstokesmitchell_elite` |

`doc/ronaldmartin_design.md` provisionally recommends `ronaldmartin_expedition`. This cycle standardizes the player-facing fitted version as `ronaldmartin_elite` to match `toranaga_elite`, `diann_elite`, `raychen_elite`, `hahn_elite`, and the requested elite-version scope. Do not create both Ronald Martin variant IDs in this pass.

Before implementation, search core game data, inspiration data, and the current mod for all four IDs and their intended file paths. If any deployable hull ID collides, stop and adopt a `trng_`-prefixed ID consistently across the hull, variants, CSV rows, descriptions, and references.

## Source Design Commitments

### Ronald Martin

- Hull size is `CRUISER`.
- It is an autonomous exploration platform with exceptional defensive combat performance.
- Its defining strength is campaign reach, survey/salvage capability, sensors, shield endurance, and sustained fire—not Toranaga-level heavy weapon count.
- It uses the FM Miracle sprite and exact source geometry for the first pass.
- It has one large energy turret, four medium energy mounts, and five small energy turrets.
- It has zero fighter bays.
- It should use `highenergyfocus` for the first pass unless ID verification or testing establishes a better vanilla system.
- It should not retain `FantasyBasicMod`, the `FM` ship style, or any Gensoukyou dependency.

### Brian Stokes Mitchell

- Hull size is `DESTROYER`.
- It is a dedicated breakthrough and cruiser-hunter combatant with no exploration role.
- It uses the FM Witch sprite and exact source geometry for the first pass.
- It has two medium missile hardpoints, four small energy turrets, and one hidden built-in large axial weapon.
- It has zero fighter bays.
- It should use `fastmissileracks` for the first pass.
- The source `FM_Masterspark` must not be copied as a dependency.
- Its first-pass axial weapon should be a verified vanilla large energy weapon, with `tachyonlance` as the preferred test choice.
- It should not retain `FantasyBasicMod`, `high_scatter_amp`, the `FM` ship style, or any Gensoukyou dependency.

## Reference Data

### Ronald Martin / FM Miracle

Reference files:

- Sprite: `inspiration/Gensoukyou/graphics/ships/FM_Miracle.png`
- Hull: `inspiration/Gensoukyou/data/hulls/FM_Miracle.ship`
- Variant: `inspiration/Gensoukyou/data/variants/FM_Miracle_Standard.variant`
- Variant: `inspiration/Gensoukyou/data/variants/FM_Miracle_Elite.variant`
- Variant: `inspiration/Gensoukyou/data/variants/FM_Miracle_Attack.variant`
- Variant: `inspiration/Gensoukyou/data/variants/FM_Miracle_Support.variant`

Geometry:

- Width: `166`
- Height: `274`
- Center: `[83, 129.5]`
- Collision radius: `153.5`
- Shield center: `[0, 0]`
- Shield radius: `149.5`
- Bounds: copy exactly from `FM_Miracle.ship`.
- Engine slots: copy all twelve, using vanilla `HIGH_TECH` style.
- Weapon slots: preserve all ten source coordinates, mounts, and arcs.

### Brian Stokes Mitchell / FM Witch

Reference files:

- Sprite: `inspiration/Gensoukyou/graphics/ships/FM_Witch.png`
- Hull: `inspiration/Gensoukyou/data/hulls/FM_Witch.ship`
- Variant: `inspiration/Gensoukyou/data/variants/FM_Witch_Standard.variant`
- Variant: `inspiration/Gensoukyou/data/variants/FM_Witch_Support.variant`

Geometry:

- Width: `130`
- Height: `190`
- Center: `[65, 93]`
- Collision radius: `93`
- Shield center: `[0, 0]`
- Shield radius: `90.5`
- Bounds: copy exactly from `FM_Witch.ship`.
- Engine slots: copy all ten, using vanilla `HIGH_TECH` style.
- Weapon slots: preserve all seven source coordinates, mounts, and arcs.

## Implementation Steps

### 1. Baseline Inspection and Collision Audit

Tasks:

- Re-read both implementation design documents.
- Inspect both source hull files and all listed source variants.
- Inspect current Toranaga hull, variant, ship-data, and description conventions.
- Search core, inspiration, and current mod data for the proposed hull and variant IDs.
- Verify current RC8 IDs for all proposed weapons, systems, hullmods, and built-ins.
- Record the current mod version before making implementation changes.

Acceptance criteria:

- No unresolved hull, variant, description, or file-path collision.
- No Gensoukyou-only ID is selected for the implementation.
- The starting mod version is confirmed as `0.5.0`.

### 2. Sprite Assets

Tasks:

- Copy `FM_Miracle.png` to `Toranaga/graphics/ships/ronaldmartin.png`.
- Copy `FM_Witch.png` to `Toranaga/graphics/ships/brianstokesmitchell.png`.
- Do not resize, pad, rotate, recolor, or recompress either first-pass asset.

Deliverables:

- `Toranaga/graphics/ships/ronaldmartin.png`
- `Toranaga/graphics/ships/brianstokesmitchell.png`

Acceptance criteria:

- Ronald Martin sprite is `166x274` and byte-identical to `FM_Miracle.png`.
- Brian Stokes Mitchell sprite is `130x190` and byte-identical to `FM_Witch.png`.
- Both files exist at the paths referenced by their hull files.

### 3. Ronald Martin Basic Hull

Tasks:

- Create `Toranaga/data/hulls/ronaldmartin.ship`.
- Set hull ID to `ronaldmartin` and hull size to `CRUISER`.
- Copy Miracle center, bounds, shield, engine, and slot geometry exactly.
- Change the ship and engine styling to available Toranaga/vanilla high-tech values.
- Define one large energy turret, four medium energy mounts, and five small energy turrets using the design document's slot plan.
- Use zero launch bays.
- Add verified exploration built-ins supported by the current game/mod.
- Do not reference `FantasyBasicMod` or another Gensoukyou ID.

Deliverable:

- `Toranaga/data/hulls/ronaldmartin.ship`

Acceptance criteria:

- JSON parses successfully.
- Geometry matches `FM_Miracle.ship`.
- Hull contains ten combat slots and zero launch bays.
- All built-in hullmod IDs exist.
- No unavailable style or dependency remains.

### 4. Brian Stokes Mitchell Basic Hull

Tasks:

- Create `Toranaga/data/hulls/brianstokesmitchell.ship`.
- Set hull ID to `brianstokesmitchell` and hull size to `DESTROYER`.
- Copy Witch center, bounds, shield, engine, and slot geometry exactly.
- Change the ship and engine styling to available Toranaga/vanilla high-tech values.
- Preserve two medium missile hardpoints and four small energy turrets.
- Preserve `WS0007` as a hidden built-in large axial weapon slot.
- Bind a verified vanilla large energy weapon to `WS0007`; prefer `tachyonlance` for the first test pass.
- Use zero launch bays.
- Do not reference `FantasyBasicMod`, `high_scatter_amp`, or `FM_Masterspark`.

Deliverable:

- `Toranaga/data/hulls/brianstokesmitchell.ship`

Acceptance criteria:

- JSON parses successfully.
- Geometry matches `FM_Witch.ship`.
- Hull contains seven combat slots and zero launch bays.
- `WS0007` is hidden, built-in, and assigned a verified weapon.
- No unavailable style, weapon, or hullmod dependency remains.

### 5. Shared Ship Data

Tasks:

- Add both hull rows to `Toranaga/data/hulls/ship_data.csv`.
- Apply the first-pass tuning targets from this document.
- Use `highenergyfocus` for Ronald Martin.
- Use `fastmissileracks` for Brian Stokes Mitchell.
- Keep fighter bays at `0` for both ships.
- Preserve each class's distinct campaign logistics.

Deliverable:

- Updated `Toranaga/data/hulls/ship_data.csv`

Acceptance criteria:

- Both rows have the same field count as the header.
- Values occupy the intended columns.
- Shield upkeep values are small multipliers, not flat flux numbers.
- Ronald Martin has exploration-cruiser cargo, fuel, and endurance.
- Brian Stokes Mitchell has combat-destroyer logistics with no exploration advantage.

### 6. Ronald Martin Elite Variant

Tasks:

- Create `Toranaga/data/variants/ronaldmartin_elite.variant`.
- Reference hull ID `ronaldmartin` and variant ID `ronaldmartin_elite`.
- Fit verified vanilla energy weapons across all ten slots.
- Favor sustained, AI-reliable pressure rather than an all-burst self-overload fit.
- Use the small mounts primarily for complete point-defense coverage.
- Prioritize vents before capacitors.
- Add combat hullmods that complement range, shields, flux, and weapon control.
- Use no wings.

Deliverable:

- `Toranaga/data/variants/ronaldmartin_elite.variant`

Acceptance criteria:

- Variant JSON parses successfully.
- Every assigned slot exists on the Ronald Martin hull.
- Every weapon and hullmod ID is verified for RC8.
- Variant has zero wings.
- The loadout can sustain fire without immediately overloading its own reactor.

### 7. Brian Stokes Mitchell Elite Variant

Tasks:

- Create `Toranaga/data/variants/brianstokesmitchell_elite.variant`.
- Reference hull ID `brianstokesmitchell` and variant ID `brianstokesmitchell_elite`.
- Fit verified medium missiles that set up or exploit the axial weapon.
- Fit the four small energy turrets for continuous pressure and point defense.
- Do not redundantly assign the built-in axial slot in the variant if the hull owns it.
- Prioritize vents before capacitors.
- Add combat hullmods focused on missile reliability, shields, and flux performance.
- Use no wings.

Deliverable:

- `Toranaga/data/variants/brianstokesmitchell_elite.variant`

Acceptance criteria:

- Variant JSON parses successfully.
- Every assigned slot exists on the Brian Stokes Mitchell hull.
- Every weapon and hullmod ID is verified for RC8.
- Variant has zero wings.
- The loadout demonstrates the missile-opening/axial-finisher combat loop.

### 8. Descriptions and Metadata

Tasks:

- Add a `SHIP` description for `ronaldmartin` to `Toranaga/data/strings/descriptions.csv`.
- Add a `SHIP` description for `brianstokesmitchell` to the same file.
- Present Ronald Martin as an integrated autonomous exploration cruiser, not a warship with survey equipment attached.
- Present Brian Stokes Mitchell as a pure combat prototype, not a carrier, explorer, or small cruiser.
- Preserve valid CSV quoting and field counts.

Deliverable:

- Updated `Toranaga/data/strings/descriptions.csv`

Acceptance criteria:

- Both description IDs exactly match their hull IDs.
- Both descriptions use type `SHIP`.
- CSV remains valid.
- Each description clearly distinguishes its ship from the other family members.

### 9. Version Increase

Tasks:

- Update `Toranaga/mod_info.json` during this implementation cycle.
- Increase `version` from `0.5.0` to `0.6.0`.
- Keep `gameVersion` at `0.98a-RC8` unless the target game version changes before implementation.
- Update the mod description only if necessary to accurately reflect its expanded ship roster.

Deliverable:

- Updated `Toranaga/mod_info.json`

Acceptance criteria:

- The mod version is higher than the pre-cycle version.
- The expected completed-cycle version is `0.6.0`.
- `gameVersion` remains correct.
- JSON parses successfully.
- The version increase is not omitted even if all ship files validate without it.

### 10. Structural Validation

Tasks:

- Parse every touched `.ship`, `.variant`, and `.json` file.
- Validate field counts for every touched CSV row.
- Confirm both sprites exist, have the expected dimensions, and match their references by hash.
- Validate all hull-to-sprite references.
- Validate all variant-to-hull references.
- Validate every equipped slot against its hull.
- Validate every weapon, hullmod, built-in, and ship-system ID against available RC8 or mod data.
- Confirm both ships have zero launch bays and both elite variants have zero wings.
- Search touched files for `FM_`, `FantasyBasicMod`, `high_scatter_amp`, and unavailable custom styles.
- Confirm the final `mod_info.json` version is `0.6.0`.

Acceptance criteria:

- No malformed JSON.
- No malformed CSV rows.
- No missing asset, hull, weapon, system, or hullmod references.
- No retained Gensoukyou dependency.
- No hull or variant ID collision.
- Correct final version is present.

### 11. In-Game Test Pass

Tasks:

- Confirm the launcher displays Toranaga version `0.6.0`.
- Add each elite variant through the console or an available test method.
- Open both ships in refit.
- Deploy each ship in the simulator.
- Verify sprite placement, shield coverage, weapon alignment, engine glows, and system activation.
- Test AI control as well as player control.
- Test Ronald Martin's cargo, fuel, burn speed, supply use, survey behavior, and recovery behavior in campaign.
- Test Brian Stokes Mitchell against destroyers and cruisers to verify its attack cycle.
- Compare both ships against existing family hulls for role separation.

Acceptance criteria:

- Both elite variants can be spawned, refitted, and deployed.
- No visible floating or misaligned weapon slots.
- No shield geometry or passive-upkeep failure.
- No missing sprites or effects.
- Systems activate and affect the intended weapons.
- Both ships are intentionally powerful but retain their stated identities.

## First-Pass Tuning Targets

### Ronald Martin

- Ordnance points: 300
- Hull: 16,000
- Armor: 1,400
- Flux capacity: 34,000
- Flux dissipation: 2,600
- Fighter bays: 0
- Speed: 85
- Acceleration: 85
- Deceleration: 75
- Turn rate: 48
- Turn acceleration: 80
- Shield: omni, 360 arc, 0.05 upkeep, 0.40 efficiency
- Cargo: 1,200
- Fuel: 2,400
- Fuel/ly: 2
- Max burn: 10
- Crew: 140 minimum, 600 maximum
- Supplies/recovery: 24
- Supplies/month: 10
- CR recovery/day: 5%
- CR to deploy: 18%
- Peak CR seconds: 720
- System: `highenergyfocus`

### Brian Stokes Mitchell

- Ordnance points: 235
- Hull: 9,500
- Armor: 1,000
- Flux capacity: 24,000
- Flux dissipation: 2,100
- Fighter bays: 0
- Speed: 135
- Acceleration: 180
- Deceleration: 155
- Turn rate: 82
- Turn acceleration: 165
- Mass: 700
- Shield: omni, 360 arc, 0.04 upkeep, 0.35 efficiency
- Cargo: 90
- Fuel: 160
- Fuel/ly: 2
- Max burn: 11
- Crew: 55 minimum, 170 maximum
- Supplies/recovery: 16
- Supplies/month: 11
- CR recovery/day: 4%
- CR to deploy: 20%
- Peak CR seconds: 420
- System: `fastmissileracks`

## First-Pass Weapon Direction

### Ronald Martin Elite

- Preserve all ten Miracle mounts.
- One large energy turret as the primary sustained battery.
- Two forward medium energy hardpoints for focused pressure.
- Two medium energy turrets for broad coverage.
- Five small energy turrets primarily for point defense.
- Verify final weapon IDs and flux behavior before committing the loadout.

### Brian Stokes Mitchell Elite

- Preserve all seven Witch slots.
- Two medium missile hardpoints as the configurable assault batteries.
- One hidden built-in large energy weapon; prefer verified `tachyonlance` for the first pass.
- Four small energy turrets for point defense and continuous pressure.
- Verify missile ammunition behavior with `fastmissileracks`.

## Risk Notes

- Both ships are intentionally overpowered; testing should focus first on function and identity, then on relative family balance.
- Ronald Martin's combined cargo, fuel, survey, salvage, sensor, shield, and combat strengths may invalidate support ships if bonuses stack too broadly.
- A custom Ronald Martin exploration hullmod is deferred; use only verified built-ins in the basic pass rather than inventing an unimplemented ID.
- Brian Stokes Mitchell's built-in large weapon, missile reload system, and exceptional reactor can compound into excessive burst damage.
- A hidden built-in weapon must be owned by the hull and should not be treated as an ordinary visible variant slot.
- The Gensoukyou hulls use unavailable custom content that must not be copied blindly.
- The unusual Witch lateral engine slots must be visually checked in-game.
- Shield upkeep values must remain small multipliers.
- The previous Nebula collision demonstrates that ID uniqueness must be checked before any deployable hull is added.
- `ronaldmartin_elite` intentionally differs from the provisional `ronaldmartin_expedition` ID in the design document; all implementation references must use the cycle decision consistently.
- The version increase is a required deliverable, not an optional cleanup step.

## Out of Scope for Dev Cycle 005

- Final balance.
- Final custom art or recoloring.
- Custom Ronald Martin research hullmod code.
- Custom Brian Stokes Mitchell axial weapon.
- Custom ship-system code.
- Custom campaign starts, quests, markets, or recovery events.
- New fighter wings or drones.
- Additional standard, support, attack, or test variants.
- Changes to existing Toranaga-family hull balance unless needed to fix a shared data error.

## Completion Definition

Dev Cycle 005 is complete when the repository contains:

- `Toranaga/data/hulls/ronaldmartin.ship`
- `Toranaga/data/variants/ronaldmartin_elite.variant`
- `Toranaga/graphics/ships/ronaldmartin.png`
- A Ronald Martin row in `ship_data.csv`.
- A Ronald Martin ship description.
- `Toranaga/data/hulls/brianstokesmitchell.ship`
- `Toranaga/data/variants/brianstokesmitchell_elite.variant`
- `Toranaga/graphics/ships/brianstokesmitchell.png`
- A Brian Stokes Mitchell row in `ship_data.csv`.
- A Brian Stokes Mitchell ship description.
- No retained Gensoukyou-only dependencies.
- Validation results confirming geometry, assets, IDs, loadouts, and CSV/JSON structure.
- A successful basic refit and simulator pass for both elite variants.
- An increased mod version of `0.6.0` in `Toranaga/mod_info.json`.

The cycle does not require final balance or custom code. It does require two coherent basic ships, two functional elite variants, and the version increase.

## Implementation Result

Status: Implemented in mod version `0.6.0`.

Implemented basic ships:

- `Toranaga/data/hulls/ronaldmartin.ship`
- `Toranaga/data/hulls/brianstokesmitchell.ship`
- `Toranaga/graphics/ships/ronaldmartin.png`
- `Toranaga/graphics/ships/brianstokesmitchell.png`

Implemented elite variants:

- `Toranaga/data/variants/ronaldmartin_elite.variant`
- `Toranaga/data/variants/brianstokesmitchell_elite.variant`

Updated shared files:

- `Toranaga/data/hulls/ship_data.csv`
- `Toranaga/data/strings/descriptions.csv`
- `Toranaga/mod_info.json`

Implementation choices:

- Ronald Martin uses `highenergyfocus`, ten energy mounts, zero bays, and the exploration built-ins specified by the design.
- Ronald Martin Elite uses a Tachyon Lance, paired Pulse Lasers, paired Graviton Beams, and five Burst PD Lasers.
- Brian Stokes Mitchell uses `fastmissileracks`, twin medium missile hardpoints, four small energy turrets, zero bays, and a built-in Tachyon Lance in hidden slot `WS0007`.
- Brian Stokes Mitchell Elite uses paired Sabot SRM Pods, two Burst PD Lasers, and two Ion Cannons.
- Both source sprites are exact byte copies and both hulls preserve their complete reference geometry.
- All Gensoukyou-only styles, hullmods, and weapons were removed.
- The mod version was increased from `0.5.0` to `0.6.0`.

Validation result:

- All new hull, variant, and metadata JSON parses successfully.
- Both CSV files parse and contain the new IDs.
- Sprite dimensions and SHA-256 hashes match their reference assets.
- Bounds, engine slots, weapon slots, centers, and shield geometry match the reference hulls.
- All weapons, hullmods, built-ins, and systems resolve against Starsector `0.98a-RC8` core data.
- Both hulls have zero launch bays and both elite variants have zero wings.
- No retained `FM_`, `FantasyBasicMod`, `high_scatter_amp`, or `FM_Masterspark` dependency remains.

Remaining manual work:

- Launch Starsector and perform the refit, simulator, AI, visual alignment, and campaign behavior tests described above.
