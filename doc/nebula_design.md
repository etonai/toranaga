# Nebula-Class Destroyer

## Implementation Design Document

Status: Draft for review before implementation.

Source brief: `doc/nebula.md`

Visual inspiration: `inspiration/scalartech-solutions-0.9.3b/graphics/tahlan/ships/tahlan_tress.png`

Reference hull: `inspiration/scalartech-solutions-0.9.3b/data/hulls/tahlan_tress.ship`

---

## Design Goal

The Nebula is a Domain-era elite destroyer from the same strategic development lineage as the Toranaga. It should feel like the smaller, faster, more aggressive escort counterpart to the Toranaga-class autonomous cruiser.

The ship is intentionally stronger than vanilla destroyers. Its purpose is not fair destroyer balance; its purpose is to answer what a no-compromise Domain destroyer would look like if built with Toranaga-adjacent reactor, shield, mobility, and fire-control technology.

## Visual Direction

The Nebula should look like the Tahlan Tress reference.

Key visual cues to preserve:

- Compact destroyer-scale hull with a wide, fast silhouette.
- Clean central body with swept lateral structures.
- Two prominent outer engine or nacelle assemblies.
- Forward-facing weapon posture.
- High-tech paneling and smooth surfaces.
- Clear visual relationship to the Toranaga's Filament-derived shape language.
- Two visible support-bay regions integrated into the hull.

Changes for Nebula identity:

- Domain prototype identity should be cleaner and more purposeful.
- The ship should read as an aggressive superiority destroyer rather than a light carrier.
- The two bays should support combat tempo, not define the whole ship.
- Weapon hardpoints should feel integrated into a compact strike platform.

Recommended sprite strategy:

- Use `tahlan_tress.png` as the visual basis.
- Preserve the 188x134 proportions for the first implementation pass.
- If custom art is later produced, keep the same silhouette and engine geometry.

## Ship Class

Recommended hull size: `DESTROYER`

The Nebula must remain meaningfully smaller than the Toranaga. It should outperform many cruisers through speed, shields, and firepower, but it should not visually or mechanically become a cruiser.

Recommended combat role tags:

- Elite destroyer
- Fleet superiority escort
- Interceptor
- Strike destroyer
- Prototype

## Core Combat Identity

The Nebula wins by taking initiative. It should close quickly, pressure hard, reposition before the enemy can answer, and use its shields to stay aggressive.

Combat feel:

- Extremely agile.
- Fast enough to dictate destroyer and cruiser engagements.
- Shield-first defensive profile.
- High flux reserves and dissipation.
- Strong burst and sustained pressure.
- Enough point defense to survive while attacking.
- Punished by reckless overextension, not by ordinary destroyer limitations.

## Proposed Baseline Stats

These are first-pass implementation targets and should be adjusted after in-game testing.

| Stat | Proposed Value | Intent |
| --- | ---: | --- |
| Hull size | Destroyer | Keeps the ship distinct from Toranaga. |
| Ordnance points | 220 | Allows elite loadouts without cruiser classification. |
| Hull | 8,500 | Very high for a destroyer, but not the primary defense. |
| Armor | 850 | Enough to forgive mistakes without becoming armor-tanked. |
| Flux capacity | 22,000 | Large reserve for shield and weapon pressure. |
| Flux dissipation | 1,900 | Sustains aggressive destroyer combat. |
| Fighter bays | 2 | Preserves the Tress-derived two-bay identity. |
| Max speed | 130 | Fast enough to hunt cruisers and disengage. |
| Acceleration | 170 | Frigate-like responsiveness. |
| Deceleration | 140 | Supports precise strike passes. |
| Turn rate | 75 | Very high destroyer agility. |
| Turn acceleration | 150 | Snappy handling and shield control. |
| Shield type | Omni | Primary defense. |
| Shield arc | 360 | Prototype-grade full coverage. |
| Shield upkeep | 0.05 | Extremely low upkeep multiplier. |
| Shield efficiency | 0.40 | Exceptional shield performance. |
| Supplies/month | 10 | Combat ship, not exploration-optimized. |
| Supplies/recovery | 14 | Costly but manageable. |
| Fuel/ly | 2 | Standard combat logistics. |
| Max burn | 11 | Keeps pace with fast fleets and Toranaga-led task forces. |
| Cargo | 120 | Minimal utility storage. |
| Fuel | 180 | Normal destroyer reserve. |
| Crew minimum | 60 | Advanced automation, but not autonomous like Toranaga. |
| Crew maximum | 180 | Room for combat operations and fighter support. |

## Weapon Layout

The Nebula should echo the Toranaga's flexible, high-tech weapon philosophy at destroyer scale while respecting the Tress sprite.

Recommended slots:

- 2 large energy or synergy forward mounts.
- 2 medium missile or synergy hardpoints on the lateral forward structures.
- 2 medium energy or hybrid turrets near the centerline.
- 6 small energy turrets for point defense and close-range pressure.

The source brief suggests:

- 2 large weapon mounts.
- 2 medium weapon mounts.
- 6 small weapon mounts.

Implementation may use 2 additional medium mounts if the sprite supports it cleanly, but the first pass should not become visually overcrowded.

Design note: the original Tress slot map has two small energy turrets, two medium missile hardpoints, two hidden launch bays, and decorative engine weapons. The Nebula should preserve the broad layout idea while upgrading it into a direct-combat destroyer.

## Fighter Bays

Recommended baseline: 2 bays.

The Tress reference is a two-bay light carrier, and the Nebula should keep that visible lineage. Unlike a carrier, however, the Nebula should use its bays to extend its attack and defense envelope while remaining a direct-combat destroyer.

Design intent:

- Bays support the ship's aggression.
- Wings should not be the main source of damage.
- Fighter choices should help the Nebula pursue, screen, or finish targets.
- The ship should still feel dangerous if its fighters are temporarily depleted.

Preferred loadout direction:

- 2 standard fighter bays for player flexibility.
- Default variant should use fast interceptors, elite fighters, or precision strike craft.
- Avoid slow bomber-only defaults unless testing shows the ship needs more anti-capital punch.

## Ship System

Recommended system name: `Reactor Overdrive`

Role: offensive mobility and pressure.

Proposed behavior:

- Increases speed, acceleration, and turn rate.
- Improves energy weapon flux efficiency or rate of fire.
- Slightly improves shield efficiency while active.
- Encourages attack runs rather than passive defense.

Possible first-pass implementation:

- Use an existing vanilla ship system if it approximates the feel.
- `highenergyfocus` is acceptable for an early offensive test pass.
- `maneuveringjets` is acceptable if mobility proves more important.
- Custom Java should be deferred until the base hull is stable in-game.

## Built-In Hullmods

The Nebula should share some high-tech integration with the Toranaga, but it should not carry the Toranaga's exploration package.

Recommended built-ins:

- `advancedoptics`
- `turretgyros`
- `stabilizedshieldemitter` if supported safely as a built-in
- `hardened_subsystems` if peak-time testing demands it

Avoid built-ins:

- `surveying_equipment`
- `efficiency_overhaul`
- `solar_shielding`

The Nebula is a combat escort, not an expedition platform.

## Variants

Initial implementation should include one complete player-facing variant.

### `nebula_elite`

Purpose: default elite strike escort.

Suggested fit:

- Large energy weapons selected for pressure without self-overloading.
- Medium missile/synergy mounts for anti-shield pressure or finishing.
- Small energy mounts mostly point defense.
- Two fast wings that keep up with the ship's attack tempo.
- Vents prioritized over capacitors until shield behavior is confirmed.

Additional variants can come later:

- `nebula_interceptor`
- `nebula_strike`
- `nebula_screen`
- `nebula_testbed`

## Campaign Integration

Minimum campaign implementation:

- Add hull definition.
- Add ship sprite.
- Add ship variant.
- Add ship data row.
- Add description text.

Preferred campaign identity:

- Rare prototype or limited-production escort.
- Strong association with Toranaga program.
- Not common market stock.
- Potential reward, start companion, or special fleet escort in later content.

## Description Text Direction

Tone: concise, technical, and prestigious.

The description should present the Nebula as the Domain's answer to the problem of escorting a strategic flagship that could outrun and outfight ordinary support vessels. It should emphasize that the ship was too expensive and complex for mass deployment before the Collapse.

Avoid making it sound like a carrier. The two bays are part of its integrated combat system, not its defining strategic role.

## Asset Plan

Required assets:

- `Toranaga/graphics/ships/nebula.png`

Optional future assets:

- Engine glow overlays.
- Custom hullmod icon.
- Custom system icon.
- Small decorative engine or bay sprites if a later implementation needs them.

Sprite strategy:

- Use the Tress image as the direct visual reference.
- For first implementation, the Nebula may use an exact or minimally adjusted copy of `tahlan_tress.png` if visual fidelity is the priority.
- Preserve Starsector top-down readability.
- Align weapon slots to visible Tress hardpoints and bay structures.

Reference dimensions:

- Width: 188
- Height: 134
- Center: approximately `[94, 66.5]`

## File Plan

Expected implementation files may include:

- `Toranaga/data/hulls/nebula.ship`
- `Toranaga/data/variants/nebula_elite.variant`
- `Toranaga/data/hulls/ship_data.csv`
- `Toranaga/data/strings/descriptions.csv`
- `Toranaga/graphics/ships/nebula.png`

Custom code is not expected for the first pass.

## Testing Plan

After implementation:

- Confirm the mod loads without JSON, CSV, weapon, wing, or hullmod ID errors.
- Confirm the sprite displays at correct scale and orientation.
- Confirm weapon slots align with visible hardpoints.
- Confirm the two fighter bays work.
- Confirm shields raise without excessive passive flux.
- Confirm mobility feels destroyer-fast, not cruiser-heavy.
- Test against vanilla destroyers and cruisers.
- Test alongside Toranaga to confirm shared family feel.

## Open Review Questions

- Should the Nebula use an exact Tress sprite copy, as Toranaga now uses an exact Filament copy?
- Should the default loadout lean more toward energy pressure or missile strike?
- Should the two bays use interceptors, fighters, or strike craft by default?
- Should the ship system be mobility-first or weapon-output-first?
- Should the Nebula be available independently, or only as part of Toranaga-related content?

## Review Gate

Implementation should not begin until this document is reviewed and approved.
