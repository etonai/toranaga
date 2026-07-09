# Toranaga-Class Autonomous Cruiser

## Implementation Design Document

Status: Draft for review before implementation.

Source brief: `doc/design.md`

Visual inspiration: `inspiration/scalartech-solutions-0.9.3b/graphics/tahlan/ships/tahlan_filament.png`

---

## Design Goal

The Toranaga is a unique, player-start flagship built around the fantasy of a final Domain prototype: cruiser-sized in classification, capital-grade in battlefield impact, and self-sufficient enough to carry an entire exploration campaign.

The ship should be intentionally overpowered, but not in a dull "more hit points" way. Its strength should come from precision, speed, shield quality, flux reserves, integrated systems, and broad tactical flexibility.

## Visual Direction

The Toranaga should visually echo the Tahlan Filament reference without being a direct copy.

Key visual cues to preserve:

- Tall, narrow high-tech silhouette with a strong central spine.
- Elegant forward point and clean axial symmetry.
- Prominent circular or ring-like central reactor feature.
- Swept lateral structures that imply speed and advanced field geometry.
- Large aft engine cluster with bright high-energy exhaust.
- Smooth, luminous high-tech paneling rather than industrial plating.
- Distinctive red or crimson energy accents against a cool metallic hull.

Changes for Toranaga identity:

- Domain prototype styling should be cleaner and less ornate.
- The silhouette should read as an autonomous strategic cruiser rather than a carrier-capital.
- The central ring should suggest an integrated phase-shield or gravitic core.
- The aft engines should be powerful but disciplined, with fewer decorative protrusions.
- The sprite should feel like a lost Domain miracle rather than a faction production vessel.

## Ship Class

Recommended hull size: `CRUISER`

Although the reference sprite is capital-sized, the Toranaga concept is strongest if it remains a cruiser in game classification. This keeps the identity from becoming "just another capital ship" and supports the brief's destroyer-like responsiveness in a cruiser body.

Recommended combat role tags:

- Flagship
- Elite assault cruiser
- Explorer
- Prototype
- Unique hull

## Core Combat Identity

The Toranaga should win by maintaining pressure while denying enemies clean engagement windows.

Combat feel:

- Fast for a cruiser.
- Extremely responsive.
- Very strong shield profile.
- Excellent sustained flux performance.
- High forward and broadside firepower.
- Enough point defense to ignore light pressure.
- Vulnerable mainly to extreme overcommitment, EMP saturation, or being surrounded by endgame fleets.

## Proposed Baseline Stats

These values are first-pass implementation targets and can be adjusted after in-game testing.

| Stat | Proposed Value | Intent |
| --- | ---: | --- |
| Hull size | Cruiser | Keeps the prototype identity focused and agile. |
| Ordnance points | 360 | Supports capital-grade loadouts without forcing compromises. |
| Hull | 18,000 | High, but not the main defensive layer. |
| Armor | 1,500 | Strong mistake buffer, secondary to shields. |
| Flux capacity | 38,000 | Lets the ship sustain elite weapon packages. |
| Flux dissipation | 2,200 | High enough for aggressive continuous pressure. |
| Max speed | 95 | Fast cruiser, close to destroyer feel with skills. |
| Acceleration | 100 | Responsive flagship handling. |
| Deceleration | 90 | Allows precise shield and range control. |
| Turn rate | 55 | Agile for size. |
| Shield type | Omni | Primary defensive identity. |
| Shield arc | 360 | Full coverage, flagship-grade. |
| Shield efficiency | 0.45 | Very efficient, intentionally exceptional. |
| Shield upkeep | 250 | Low enough to feel advanced. |
| Supplies/month | 12 | Efficient for performance. |
| Supplies/recovery | 28 | Powerful but not punitive. |
| Fuel/ly | 3 | Exploration flagship economy. |
| Max burn | 10 | No logistics drag. |
| Cargo | 900 | Can begin campaign without immediate freighter support. |
| Fuel | 1,800 | Deep exploration capability. |
| Crew minimum | 120 | Advanced automation. |
| Crew maximum | 450 | Room for long expeditions. |

## Weapon Layout

The Toranaga should support multiple builds, with an emphasis on energy and hybrid technology.

Recommended slots:

- 2 large energy turrets on the upper and lower forward shoulders with broad arcs.
- 1 large universal or synergy hardpoint on the centerline nose.
- 2 medium synergy hardpoints on forward lateral arms.
- 2 medium hybrid turrets near the central ring with wide arcs.
- 1 medium energy turret aft for rear coverage.
- 8 small energy turrets distributed along lateral and forward hull edges for point defense.
- 2 small missile or synergy mounts near the nose for utility pressure.

Recommended built-in decorative or hidden slots:

- Central ring or reactor visual weapon slot.
- Aft gravitic engine visual slot.
- Optional integrated drone bay visual slot if a ship system uses drones.

Design note: avoid copying the Filament slot map directly. Use the same broad ideas: forward large mounts, central wide-arc mounts, lateral PD, and distinctive built-in visual technology.

## Fighter Bays

Recommended baseline: 2 bays.

The Filament inspiration includes multiple launch bays, and the Toranaga should preserve a controlled version of that identity. Two bays give the ship autonomous expeditionary reach and tactical support without turning it into a dedicated carrier-capital.

Design intent:

- Bays should feel like integrated Domain support systems, not the ship's main damage source.
- The Toranaga remains a direct-combat flagship first.
- Fighter choices should complement the ship's pressure, defense, and pursuit roles.
- The sprite should include visible bay geometry along the lateral forward or midship structures.

Preferred loadout direction:

- 2 standard fighter bays for player flexibility.
- Default variant may use advanced interceptors, support drones, or strike craft depending on available mod content.
- If custom wings are added later, they should be elite autonomous craft with defensive or precision-strike behavior.

## Ship System

Recommended system name: `Gravitic Command Matrix`

Role: mobility, shield reinforcement, and flux control in a single prototype system.

Proposed behavior:

- Briefly increases speed, acceleration, and turn rate.
- Reduces shield damage taken while active.
- Increases weapon rate of fire modestly or improves energy weapon flux efficiency.
- Emits a visible pulse from the central ring.

Balance target:

- Strong enough to feel unique.
- Short enough duration that timing still matters.
- Better as an engagement control tool than a panic button.

Possible implementation approaches:

- Start with an existing vanilla-style system behavior if available in the mod framework.
- Implement a custom system script only if the existing system APIs cannot express the intended feel.

## Built-In Hullmods

The Toranaga should include numerous built-in hullmods to represent integrated Domain engineering.

Recommended built-ins:

- `surveying_equipment`
- `efficiency_overhaul`
- `solar_shielding`
- `resistantfluxconduits`
- `advancedoptics` or a custom advanced targeting equivalent
- `turretgyros`
- `automated` or custom autonomous command hullmod, if compatible with campaign goals

Recommended custom hullmod:

### Toranaga Prototype Core

Effects:

- Reduces campaign sensor profile.
- Improves sensor strength.
- Improves salvage or survey performance.
- Slightly reduces supply and fuel use.
- Grants EMP resistance or reduced weapon/engine disable chance.
- Marks the hull as unique and non-standard.

The custom hullmod should carry the lore and campaign identity so the ship file does not need to encode every special rule directly.

## Variants

Initial implementation should include one complete player-facing variant.

### `toranaga_elite`

Purpose: default flagship loadout.

Suggested fit:

- Large energy weapons for sustained frontal pressure.
- Hybrid/synergy mounts split between anti-shield and finishing tools.
- Small energy mounts mostly point defense.
- Hullmods focused on range, flux, shield quality, and maneuverability.

Additional variants can come later for testing:

- `toranaga_assault`
- `toranaga_explorer`
- `toranaga_testbed`

## Campaign Integration

Minimum campaign implementation:

- Add hull definition.
- Add ship sprite.
- Add ship variant.
- Add codex/description text.
- Make the ship available to the intended new-campaign start path.

Preferred campaign identity:

- Unique hull, not common market stock.
- Starting flagship for the custom campaign scenario.
- Recoverable or discoverable only through a special route if added outside the starting fleet.

## Description Text Direction

Tone: mythic but technical.

The description should frame the ship as a late-Domain autonomous strategic cruiser intended to explore, survey, secure, and reclaim frontier systems without support. It should imply that the ship was not mass-produced because the Collapse ended the program, not because the design failed.

Avoid making the description too breathless. The ship can be legendary while still sounding like a military-industrial artifact.

## Asset Plan

Required assets:

- New Toranaga ship sprite.
- Optional engine glow or decorative ring assets.
- Optional custom hullmod icon.

Sprite strategy:

- Use the Filament image as visual reference only.
- Produce a distinct sprite with similar silhouette principles.
- Preserve Starsector top-down readability.
- Keep weapon slot positions visually aligned with hardpoints in the sprite.

Recommended target sprite dimensions:

- Around 300x380 if preserving the reference proportions.
- Center near the geometric middle, adjusted slightly forward if the bow is visually dominant.

## File Plan

Expected implementation files may include:

- `mod/mod_info.json`
- `mod/data/hulls/toranaga.ship`
- `mod/data/variants/toranaga_elite.variant`
- `mod/data/hulls/ship_data.csv`
- `mod/data/strings/descriptions.csv`
- `mod/graphics/ships/toranaga.png`
- `mod/graphics/hullmods/toranaga_prototype_core.png`
- `mod/jars/src/.../ToranagaPrototypeCore.java`
- `mod/jars/src/.../GraviticCommandMatrixStats.java`

The exact Java package and CSV schema should be chosen after inspecting the existing mod structure.

## Testing Plan

After implementation:

- Confirm the mod loads without CSV or JSON errors.
- Confirm the sprite displays at correct scale and orientation.
- Confirm weapon slots align with visible hardpoints.
- Confirm collision bounds match the hull silhouette.
- Confirm shields cover the sprite correctly.
- Test refit screen loadout behavior.
- Test combat against vanilla cruiser, capital, and mixed fleet opponents.
- Test campaign logistics: burn speed, cargo, fuel, survey behavior, and supply use.

## Open Review Questions

- Should the Toranaga have any fighter or drone component, or should it be a pure warship?
- Should the ship system prioritize mobility, shield defense, weapon output, or a hybrid of all three?
- Should the visual palette lean mostly Domain blue-white, or preserve the Filament-inspired crimson energy accents?
- Should the ship be obtainable only as the starting flagship, or also through exploration content later?

## Review Gate

Implementation should not begin until this document is reviewed and approved.
