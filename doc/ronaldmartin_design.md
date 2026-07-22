# Ronald Martin-Class Exploration Cruiser

## Implementation Design Document

Status: Draft for review before implementation.

Source brief: `doc/ronaldmartin.md`

Visual inspiration: `inspiration/Gensoukyou/graphics/ships/FM_Miracle.png`

Reference hull: `inspiration/Gensoukyou/data/hulls/FM_Miracle.ship`

---

## Design Goal

The Ronald Martin is a no-compromise Domain exploration cruiser built to conduct long-duration expeditions without a support fleet. It combines exceptional survey, sensor, salvage, cargo, and fuel capabilities with the shield strength and sustained firepower needed to survive the threats it is meant to investigate.

The ship is intentionally stronger than ordinary exploration cruisers. Its power should not come from simply matching the Toranaga in every category. The Toranaga remains the program family's military flagship; the Ronald Martin should be the superior independent expedition platform and a formidable defensive combatant.

The design must avoid two failure modes:

- A frontline warship with campaign hullmods bolted on.
- A civilian utility hull whose combat strength exists only in its description.

Its laboratories, stores, sensor equipment, and defensive systems should feel like parts of one integrated mission architecture.

## Naming and ID Direction

Player-facing name: `Ronald Martin`

Recommended internal IDs:

- Hull ID: `ronaldmartin`
- Expedition variant ID: `ronaldmartin_expedition`
- Sprite path: `graphics/ships/ronaldmartin.png`
- Hull file: `Toranaga/data/hulls/ronaldmartin.ship`
- Variant file: `Toranaga/data/variants/ronaldmartin_expedition.variant`

As with the RayChen design, search core and inspiration data for `ronaldmartin` before implementation to confirm that the hull and variant IDs are unique.

## Visual Direction

The first implementation should use the FM Miracle reference sprite directly.

Key reference facts:

- Sprite: `FM_Miracle.png`
- Width: `166`
- Height: `274`
- Center: `[83, 129.5]`
- Collision radius: `153.5`
- Shield center: `[0, 0]`
- Shield radius: `149.5`
- Hull size: `CRUISER`
- Source identity: elegant, symmetrical high-tech cruiser with a long central hull, broad lateral structures, and a dense but integrated engine cluster
- Source weapon layout: one large energy turret, four medium energy mounts, and five small energy turrets

Recommended sprite strategy:

- Copy `FM_Miracle.png` exactly as `Toranaga/graphics/ships/ronaldmartin.png` for the first implementation.
- Preserve the source dimensions, center, collision bounds, shield geometry, engine locations, and weapon coordinates.
- Do not scale, pad, or redraw the sprite during the first pass.
- Replace the source `FM` style and `FantasyBasicMod` dependency with Toranaga-compatible high-tech settings.

The silhouette already communicates a capable scientific cruiser: graceful rather than overtly aggressive, with space for sensor and research structures and weapon mounts integrated into the hull.

## Ship Class

Recommended hull size: `CRUISER`

The Ronald Martin should remain cruiser-sized in classification and handling. Its capital-like quality comes from endurance, shields, flux performance, campaign reach, and the ability to fight independently—not from a capital-sized footprint or an oversized weapon grid.

Recommended role tags:

- Exploration cruiser
- Long-range expedition flagship
- Survey and salvage platform
- Defensive combat cruiser
- Domain prototype
- Rare hull

## Relationship to the Program Family

The Ronald Martin shares the family principles established by Toranaga, DiAnn, RayChen, and Hahn:

- High-efficiency omnidirectional shields.
- Exceptional flux reactors.
- Responsive high-tech handling.
- Integrated energy weapon systems.
- Late-Domain prototype construction.

Its distinguishing priority is autonomous exploration.

- Toranaga controls battles and supports a campaign.
- DiAnn establishes local superiority.
- RayChen and Hahn control small-ship engagements.
- Ronald Martin discovers, analyzes, recovers, and returns without needing a logistics train.

## Core Combat Identity

The Ronald Martin should be difficult to force away from its mission.

Combat feel:

- Strong, stable cruiser handling rather than interceptor agility.
- Excellent omni shield performance under sustained fire.
- A large flux reserve and high dissipation for long engagements.
- Broad weapon coverage that discourages flanking and protects against dispersed threats.
- Enough frontal pressure to defeat ordinary cruisers decisively.
- Strong point defense appropriate to independent operation.
- Less concentrated alpha strike and fewer heavy mounts than the Toranaga.
- Vulnerable to coordinated capital-grade pressure, massed kinetic damage, and careless encirclement.

The ship should be overpowered for a normal exploration vessel without making every escort, combat freighter, or dedicated warship irrelevant.

## Proposed Baseline Stats

These are first-pass implementation targets and should be adjusted after combat and campaign testing.

| Stat | Proposed Value | Intent |
| --- | ---: | --- |
| Hull size | Cruiser | Preserves the intended exploration-cruiser identity. |
| Ordnance points | 300 | Supports a complete combat fit plus expedition hullmods. |
| Hull | 16,000 | Protects crew and research spaces after shields fail. |
| Armor | 1,400 | Heavy cruiser-grade mistake buffer. |
| Flux capacity | 34,000 | Sustains shields and energy weapons in long engagements. |
| Flux dissipation | 2,600 | Exceptional endurance without exceeding Toranaga's implemented reactor. |
| Fighter bays | 0 | Keeps the ship a self-contained cruiser rather than a carrier. |
| Max speed | 85 | Respectable for a heavily equipped cruiser. |
| Acceleration | 85 | Responsive navigation and combat handling. |
| Deceleration | 75 | Supports precise range control. |
| Turn rate | 48 | Agile enough to use its broad mount layout effectively. |
| Turn acceleration | 80 | Smooth, confident cruiser response. |
| Shield type | Omni | Primary defensive identity. |
| Shield arc | 360 | Protects irreplaceable personnel and equipment from all directions. |
| Shield upkeep | 0.05 | Very low passive burden. |
| Shield efficiency | 0.40 | Prototype-grade sustained defense. |
| Supplies/month | 10 | Extremely efficient for its capability and mission duration. |
| Supplies/recovery | 24 | Meaningful combat recovery cost without requiring a logistics fleet. |
| Fuel/ly | 2 | Superior long-range efficiency. |
| Max burn | 10 | Does not slow an expedition fleet. |
| Cargo | 1,200 | Carries supplies, machinery, samples, and recovered technology. |
| Fuel | 2,400 | Exceptional autonomous range. |
| Crew minimum | 140 | Scientific personnel and advanced automation. |
| Crew maximum | 600 | Supports large research teams and recovered personnel. |
| CR recovery/day | 5% | Rapid turnaround during extended expeditions. |
| CR to deploy | 18% | Powerful but efficient cruiser deployment. |
| Peak CR seconds | 720 | Designed for prolonged operations and engagements. |

## Weapon Layout

The Miracle reference provides a coherent cruiser weapon grid that already satisfies the source brief's need for large, medium, and point-defense coverage. Preserve all ten visible mounts and their source coordinates.

Proposed first-pass slot plan:

| Slot | Size | Type | Mount | Location | Arc | Role |
| --- | --- | --- | --- | --- | ---: | --- |
| `WS0001` | Medium | Energy | Hardpoint | `[54.5, 12]` | 13° | Forward precision fire. |
| `WS0002` | Medium | Energy | Hardpoint | `[54.5, -12]` | 13° | Forward precision fire. |
| `WS0003` | Medium | Energy | Turret | `[-2, -44.5]` | 160° | Broadside and flank coverage. |
| `WS0004` | Medium | Energy | Turret | `[-2, 44.5]` | 160° | Broadside and flank coverage. |
| `WS0005` | Large | Energy | Turret | `[-38, 0]` | 210° | Main sustained-fire battery. |
| `WS0006` | Small | Energy | Turret | `[35.5, 29]` | 230° | Forward point defense or utility. |
| `WS0007` | Small | Energy | Turret | `[35.5, -29]` | 230° | Forward point defense or utility. |
| `WS0008` | Small | Energy | Turret | `[-38.5, 51]` | 270° | Lateral and aft point defense. |
| `WS0009` | Small | Energy | Turret | `[-38.5, -51]` | 270° | Lateral and aft point defense. |
| `WS0010` | Small | Energy | Turret | `[-76.5, 0]` | 210° | Rear point defense. |

This layout gives the Ronald Martin one large and four medium mounts rather than the Toranaga's three large and five medium mounts. Its combat excellence therefore comes from reactor quality, shield endurance, wide coverage, and system integration instead of copying the military flagship's raw battery.

Do not add floating mounts solely to meet an abstract “multiple large weapons” target. A second large mount should require custom art or a later visual-editor pass.

## Ship System

Recommended first-pass system: `highenergyfocus`

Player-facing design direction: `Spectral Analysis Matrix`

Role: focus the ship's sensor and fire-control systems on an immediate threat.

Desired behavior:

- Temporarily improves energy weapon damage and effectiveness.
- Converts a broad defensive battery into a focused response when required.
- Rewards deliberate target selection rather than reckless engagement.
- Uses existing, reliable system behavior for the first implementation.

If custom Java is added later, the system could provide a modest energy range or flux-cost benefit instead of simply increasing burst damage. It should remain an analytical fire-control tool, not a mobility escape or invulnerability button.

## Built-In Hullmods

Recommended standard built-ins:

- `surveying_equipment`
- `efficiency_overhaul`
- `solar_shielding`
- `advancedoptics`
- `turretgyros`

Recommended custom built-in:

### Autonomous Research Complex

This hullmod should carry the Ronald Martin's exploration identity without depending on a long list of unrelated built-ins.

Proposed campaign effects:

- Increases fleet sensor strength.
- Reduces the ship's sensor profile.
- Improves survey efficiency beyond standard surveying equipment.
- Improves post-battle and derelict salvage yields.
- Reduces supply and fuel consumption.
- Provides a navigation or terrain-effect benefit appropriate to deep-space operations.

Proposed combat or recovery effects:

- Improves combat readiness recovery.
- Reduces weapon and engine repair time or disable duration.
- Provides modest EMP resistance to represent redundant scientific and control systems.

The implementation must verify which campaign effects can be expressed cleanly by hullmod APIs and avoid stacking bonuses so high that every other logistics hull becomes completely obsolete in a mixed fleet.

Avoid:

- Fighter and carrier hullmods.
- Civilian-grade hull penalties.
- Militarized subsystems as a workaround for civilian penalties.
- Automation mechanics that impose officer or fleet-point restrictions contrary to the intended player flagship role.

## Scientific Facilities

The laboratories and research spaces primarily belong in lore, description text, campaign modifiers, and visual interpretation. They should not become fighter bays or decorative weapon slots.

The Autonomous Research Complex represents:

- Geological and materials laboratories.
- Biological containment.
- Archaeological analysis facilities.
- Engineering workshops.
- High-performance computational centers.
- Secure sample and recovered-technology storage.

Future campaign content could use the hull ID or custom hullmod as a condition for special exploration interactions, but such content is outside the first implementation pass.

## Variants

Initial implementation should include one complete player-facing variant.

### `ronaldmartin_expedition`

Purpose: default independent expedition flagship.

Suggested fit:

- Large energy turret: sustained long-range pressure rather than a flux-crippling burst weapon.
- Forward medium hardpoints: complementary anti-shield and armor damage.
- Lateral medium turrets: efficient weapons with reliable AI behavior and wide coverage.
- Small mounts: predominantly point defense, with full lateral and rear protection.
- Vents prioritized before capacitors because sustained operation defines the hull.
- Combat hullmods focused on range, shields, flux control, and weapon reliability.

The default variant should demonstrate that the ship can finish fights, not merely survive them. At the same time, it should leave enough ordnance flexibility for the player to personalize the loadout.

Possible future variants:

- `ronaldmartin_longrange`
- `ronaldmartin_defense`
- `ronaldmartin_recovery`
- `ronaldmartin_testbed`

## Campaign Integration

Minimum campaign implementation:

- Add the hull definition.
- Add the copied ship sprite.
- Add the expedition variant.
- Add the ship data row.
- Add description text.
- Add the custom exploration hullmod only if its effects and package structure are confirmed.

Preferred campaign identity:

- Rare late-Domain prototype.
- Not ordinary market stock.
- Suitable as a unique discovery, expedition reward, or alternate flagship.
- Capable of replacing several support vessels for a solo or compact exploration fleet.
- Expensive enough in base value and recovery cost that acquiring one remains significant.

The first pass should not add bespoke research events, survey interactions, or acquisition quests. Those can follow once the base hull is stable.

## Description Text Direction

Tone: assured, scientific, and prestigious.

The description should present the Ronald Martin as the Domain's answer to the limits of escorted survey fleets: a vessel able to cross the frontier, conduct a complete scientific expedition, defend its personnel and discoveries, and return without outside support.

Emphasize:

- Integrated exploration and defense.
- Long-duration autonomous operation.
- Irreplaceable scientific facilities.
- The Domain belief that discovery is meaningless if it cannot be brought home.

Avoid:

- Describing it as a dedicated warship.
- Claiming it has more direct firepower than the Toranaga.
- Making it sound civilian, fragile, or mass-produced.
- Treating laboratories as flavor unrelated to gameplay.

## Asset Plan

Required assets:

- `Toranaga/graphics/ships/ronaldmartin.png`
- Optional custom hullmod icon for Autonomous Research Complex.

Sprite strategy:

- Copy `FM_Miracle.png` exactly for the first implementation.
- Preserve dimensions: `166x274`.
- Preserve center: `[83, 129.5]`.
- Preserve collision radius: `153.5`.
- Preserve shield center `[0, 0]` and radius `149.5`.
- Preserve source bounds, engine slots, and weapon coordinates.
- Use `HIGH_TECH` engine styling and a Toranaga-compatible ship style.
- Do not retain `FantasyBasicMod`, `FM`, or any other dependency on the inspiration mod.

## File Plan

Expected implementation files:

- `Toranaga/data/hulls/ronaldmartin.ship`
- `Toranaga/data/variants/ronaldmartin_expedition.variant`
- `Toranaga/data/hulls/ship_data.csv`
- `Toranaga/data/strings/descriptions.csv`
- `Toranaga/graphics/ships/ronaldmartin.png`

If the custom exploration package is included:

- `Toranaga/data/hullmods/hull_mods.csv`
- `Toranaga/graphics/hullmods/autonomous_research_complex.png`
- `Toranaga/jars/src/.../AutonomousResearchComplex.java`

The exact Java package should follow the existing mod source structure discovered during implementation.

## Testing Plan

After implementation:

- Confirm no core or inspiration ID collision for `ronaldmartin` or `ronaldmartin_expedition`.
- Confirm the mod loads without JSON, CSV, missing-style, or missing-hullmod errors.
- Confirm the sprite displays at the source scale and orientation.
- Confirm all ten weapon slots align with visible mounts.
- Confirm collision bounds and shield radius cover the sprite correctly.
- Confirm engine glows align with the full Miracle engine cluster.
- Test against vanilla cruisers, capitals, and mixed exploration threats.
- Confirm the ship can win a sustained cruiser engagement without matching Toranaga's direct firepower.
- Test AI use of the broad weapon arcs and `highenergyfocus`.
- Test campaign survey cost, salvage, sensor strength/profile, cargo, fuel range, burn speed, supply use, and CR recovery.
- Test whether one Ronald Martin can support a long expedition without making all other logistics hulls categorically useless.
- Test alongside Toranaga to confirm that each cruiser retains a distinct reason to exist.

## Open Review Questions

- Should the first pass use plain `highenergyfocus`, or should Spectral Analysis Matrix be custom from the start?
- Should the large turret remain energy-only, or become universal for maximum expedition flexibility?
- How much of the custom exploration package should apply fleet-wide versus only to the Ronald Martin?
- Should the hull be a unique discovery, an alternate starting flagship, or an exceptionally rare blueprint hull?
- Should the first implementation copy the Miracle palette exactly, or reserve a later art pass for stronger Toranaga-family colors?
- Should the default expedition variant favor long-range beam pressure or closer sustained energy fire?

## Review Gate

Implementation should not begin until this document is reviewed and approved.
