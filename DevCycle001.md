# Dev Cycle 001: Toranaga Class Ship Implementation

## Purpose

This plan turns the approved direction in `doc/toranaga_design.md` into the first implementation cycle for the Toranaga-class autonomous cruiser.

The design document remains the source of truth for ship identity, combat role, visual direction, baseline stats, weapon layout, two fighter bays, hullmods, and campaign intent. This document is only the work plan for the first development pass.

## Cycle Goal

Create a playable first version of the Toranaga class under the dedicated `Toranaga/` directory that can be loaded by Starsector, viewed in refit, deployed in combat, and used as the foundation for later tuning.

## Scope

Included in this cycle:

- Inspect the current mod structure and required Starsector data conventions.
- Add the Toranaga hull definition.
- Add or prepare the Toranaga ship sprite.
- Add the default `toranaga_elite` variant.
- Add two fighter bays.
- Add the initial weapon slot layout.
- Add baseline campaign and combat stats from `doc/toranaga_design.md`.
- Add descriptions and required CSV entries.
- Use existing hullmods and systems where possible for the first playable pass.
- Verify that the mod data is structurally coherent.

Deferred unless required for the ship to function:

- Custom Java hullmod implementation.
- Custom Java ship-system implementation.
- Custom fighter wing creation.
- Special campaign-start integration.
- Exploration event or unique recovery content.
- Final sprite polish.
- Balance tuning beyond obvious load or data errors.

## Source Design Commitments

The first implementation pass should preserve these decisions from `doc/toranaga_design.md`:

- Hull size is `CRUISER`.
- The ship is intentionally overpowered.
- It is a direct-combat autonomous flagship, not a dedicated carrier.
- It has exactly 2 fighter bays in the baseline implementation.
- It uses a high-tech, Filament-inspired silhouette without copying the Filament ship directly.
- It emphasizes shields, flux, mobility, and precision firepower.
- It has broad energy/hybrid/synergy weapon flexibility.
- It includes integrated exploration and efficiency hullmods where supported by vanilla data.

## Implementation Steps

### 1. Repository Survey

Tasks:

- Inspect top-level mod files.
- Identify existing `data`, `graphics`, `jars`, and CSV structure.
- Determine whether this repo already contains a valid Starsector mod skeleton.
- Keep the workspace root separate from the deployable Starsector mod root.
- Identify package naming conventions if Java is present.

Deliverable:

- A short implementation note in the final cycle summary describing the discovered structure.

### 2. Asset Preparation

Tasks:

- Locate the reference Filament sprite.
- Create or stage `Toranaga/graphics/ships/toranaga.png`.
- Keep the first-pass asset readable in Starsector even if it is not final art.
- Preserve approximate 300x380 proportions unless the mod structure suggests another scale.

Deliverable:

- `Toranaga/graphics/ships/toranaga.png`

Acceptance criteria:

- File exists at the expected path.
- Hull definition references it correctly.
- Sprite dimensions and center values are coherent.

### 3. Hull Definition

Tasks:

- Create `Toranaga/data/hulls/toranaga.ship`.
- Define cruiser hull size, sprite, bounds, center, shield, engines, weapon slots, and two launch bays.
- Use the design stats as first-pass targets.
- Avoid copying the Filament slot map directly.

Deliverable:

- `Toranaga/data/hulls/toranaga.ship`

Acceptance criteria:

- JSON parses successfully.
- The ship has two launch bay slots.
- Weapon slots match the design layout.
- Shield and collision radius fit the sprite.

### 4. Ship Data

Tasks:

- Add the Toranaga row to `Toranaga/data/hulls/ship_data.csv`.
- Use baseline values from `doc/toranaga_design.md`.
- Select an available ship system for the first pass if the custom `Gravitic Command Matrix` is deferred.
- Add built-in hullmods supported by existing game IDs.

Deliverable:

- Updated `Toranaga/data/hulls/ship_data.csv`

Acceptance criteria:

- CSV row has the correct number of columns.
- IDs match the hull and variant files.
- Built-in hullmods use valid IDs where possible.

### 5. Default Variant

Tasks:

- Create `Toranaga/data/variants/toranaga_elite.variant`.
- Fit weapons compatible with the selected slot types.
- Fit two wings.
- Add vents, capacitors, and hullmods consistent with the flagship role.

Deliverable:

- `Toranaga/data/variants/toranaga_elite.variant`

Acceptance criteria:

- Variant references `toranaga`.
- Variant has two wing entries.
- Weapon groups are coherent and do not reference missing slots.

### 6. Description and Metadata

Tasks:

- Add description text using the tone from `doc/toranaga_design.md`.
- Add any required codex, tag, or variant metadata supported by the mod skeleton.

Deliverable:

- Updated description or string data file, likely `Toranaga/data/strings/descriptions.csv`.

Acceptance criteria:

- Description references the Toranaga as a late-Domain autonomous strategic cruiser.
- Text is mythic but technical.
- CSV formatting is valid.

### 7. Validation

Tasks:

- Run local file validation where possible.
- Parse JSON files.
- Check CSV row shape.
- Confirm referenced files exist.
- If a build task exists, run the relevant non-destructive build or data check.

Deliverable:

- Validation summary.

Acceptance criteria:

- No obvious missing file references.
- JSON parses cleanly.
- CSV structure appears consistent.
- Any unable-to-run validation is explicitly noted.

## First-Pass Tuning Targets

Use these as implementation defaults unless the actual mod skeleton requires adjustment:

- Ordnance points: 360
- Hull: 18,000
- Armor: 1,500
- Flux capacity: 38,000
- Flux dissipation: 2,200
- Speed: 95
- Shield: omni, 360 arc, 0.45 efficiency
- Fighter bays: 2
- Cargo: 900
- Fuel: 1,800
- Max burn: 10

## Risks

- The repository may not yet contain a complete Starsector mod skeleton.
- Some hullmod or ship-system IDs may differ by Starsector version.
- A generated or placeholder sprite may need later art replacement.
- CSV schemas may require inspection before safe editing.
- Custom Java features may need a separate cycle if there is no current build setup.

## Out of Scope for Dev Cycle 001

- Final balance.
- Final art.
- Custom campaign start.
- Custom ship system code.
- Custom hullmod code.
- Custom wing or weapon code.
- Unique quest or recovery integration.

## Completion Definition

Dev Cycle 001 is complete when the repo contains a coherent first-pass Toranaga implementation with:

- A hull file.
- A ship data row.
- A default variant.
- A ship sprite path.
- Two fighter bays.
- Description text.
- Basic validation results.

The result does not need to be final-balanced, but it should be ready for the next cycle of in-game testing and refinement.
