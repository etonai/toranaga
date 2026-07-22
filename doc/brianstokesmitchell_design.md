# Brian Stokes Mitchell-Class Destroyer

## Implementation Design Document

Status: Draft for review before implementation.

Source brief: `doc/mitchell.md`

Visual inspiration: `inspiration/Gensoukyou/graphics/ships/FM_Witch.png`

Reference hull: `inspiration/Gensoukyou/data/hulls/FM_Witch.ship`

---

## Design Goal

The Brian Stokes Mitchell is the pure combat destroyer of the Toranaga program family: a no-compromise Domain prototype designed to seize the initiative, break defended positions, and destroy opponents that should outclass a destroyer.

The ship is intentionally stronger than conventional destroyers. Its performance should come from an integrated offensive cycle—mobility to establish the engagement, missiles to force a defensive failure, an axial heavy weapon to exploit it, and a prototype reactor and shield system that sustain pressure afterward.

The design should avoid turning the ship into either:

- A cruiser compressed into a destroyer classification.
- A second DiAnn/Nebula with a different sprite.

It must remain destroyer-like in footprint, acceleration, attack rhythm, and exposure when overcommitted. Unlike the DiAnn/Nebula design, it has no fighter bays and no support role. Unlike RayChen and Hahn, it wins through coordinated heavy weapons rather than frigate evasion.

## Naming and ID Direction

Player-facing name: `Brian Stokes Mitchell`

Recommended internal IDs:

- Hull ID: `brianstokesmitchell`
- Elite variant ID: `brianstokesmitchell_elite`
- Sprite path: `graphics/ships/brianstokesmitchell.png`
- Hull file: `Toranaga/data/hulls/brianstokesmitchell.ship`
- Variant file: `Toranaga/data/variants/brianstokesmitchell_elite.variant`

The full internal name is long but unambiguous and follows the requested class name. Before implementation, search core and inspiration data for `brianstokesmitchell` to confirm the hull and variant IDs are unique.

Do not shorten the internal ID to `mitchell`: it is less distinctive and could cause ambiguity if additional namesake hulls are introduced later.

## Visual Direction

The first implementation should use the FM Witch reference sprite directly.

Key Witch visual facts:

- Sprite: `FM_Witch.png`
- Width: `130`
- Height: `190`
- Center: `[65, 93]`
- Collision radius: `93`
- Shield center: `[0, 0]`
- Shield radius: `90.5`
- Hull size: `DESTROYER`
- Source identity: narrow, symmetrical high-tech attack hull with large swept lateral structures and a pronounced central weapon feature
- Source weapon layout: two medium missile hardpoints, four small energy turrets, and one hidden built-in large weapon
- Source engine layout: six conventional aft exhausts plus four unusual lateral maneuvering exhausts

Recommended sprite strategy:

- Copy `FM_Witch.png` exactly as `Toranaga/graphics/ships/brianstokesmitchell.png` for the first implementation.
- Preserve its dimensions, center, bounds, shield geometry, engine slots, and weapon coordinates.
- Do not scale, pad, or redraw the sprite during the first pass.
- Replace the source `FM` style and `FantasyBasicMod` dependency with Toranaga-compatible high-tech settings.
- Remove the dependency on `FM_Masterspark`; replace it with a verified vanilla weapon for the first pass or a Toranaga-owned built-in weapon later.

The silhouette should read as a weapon built around a central combat core. Its lateral structures visually support the twin missile hardpoints and exceptional directional control, while the narrow body supports an integrated axial heavy weapon.

## Ship Class

Recommended hull size: `DESTROYER`

The Brian Stokes Mitchell must remain physically and tactically distinct from the Toranaga and Ronald Martin cruisers. It can defeat cruisers through superior technology and attack sequencing, but it should not inherit cruiser-scale mass, logistics, or a cruiser-sized collection of ordinary weapon mounts.

Recommended combat role tags:

- Elite assault destroyer
- Breakthrough destroyer
- Cruiser hunter
- Strategic interceptor
- Independent combatant
- Domain prototype

## Relationship to the Program Family

Shared family technologies:

- High-efficiency omnidirectional shields.
- Exceptional flux reserves and dissipation.
- Responsive high-tech maneuvering.
- Integrated fire-control and energy systems.
- Late-Domain prototype construction unconstrained by cost.

Distinct tactical roles:

- Toranaga is the military flagship and battlefield controller.
- Ronald Martin is the autonomous exploration cruiser.
- DiAnn/Nebula is a superiority escort with integrated fighter support.
- RayChen and Hahn are elite pursuit and interception frigates.
- Brian Stokes Mitchell is the dedicated destroyer-scale breakthrough weapon.

It should have the highest direct assault focus of the destroyers, but no bays, exploration systems, or campaign utility to compensate.

## Core Combat Identity

The Brian Stokes Mitchell creates and exploits short windows of decisive advantage.

Combat feel:

- Fast enough to dictate engagements with other destroyers and many cruisers.
- Highly responsive acceleration, strafing, and turning.
- A strong omni shield that supports forward pressure.
- Twin medium missile batteries that overwhelm shields, armor, or point defense.
- An integrated axial heavy energy weapon that punishes the opening created by the missiles.
- Four wide-arc energy turrets that provide point defense and continuous pressure.
- Enough flux performance to remain dangerous after its initial strike.
- No fighters, support systems, or campaign bonuses distracting from direct combat.

The ship should reward deliberate aggression. A successful pilot establishes an angle, forces the target to commit flux or defensive systems, fires the missile salvo, and converts the resulting opening with the axial weapon. Firing everything indiscriminately should be less effective than synchronizing the attack.

## Proposed Baseline Stats

These are first-pass implementation targets and should be adjusted after simulator testing.

| Stat | Proposed Value | Intent |
| --- | ---: | --- |
| Hull size | Destroyer | Preserves destroyer mechanics and footprint. |
| Ordnance points | 235 | Supports elite missile and energy fittings without cruiser-scale slot count. |
| Hull | 9,500 | Exceptional structural resilience for a destroyer. |
| Armor | 1,000 | Forgives mistakes without replacing the shield as primary defense. |
| Flux capacity | 24,000 | Supports the axial weapon, turrets, and aggressive shielding. |
| Flux dissipation | 2,100 | Sustains pressure after the opening missile strike. |
| Fighter bays | 0 | Pure direct-combat identity. |
| Max speed | 135 | Superior destroyer interception and engagement control. |
| Acceleration | 180 | Rapid commitment and directional changes. |
| Deceleration | 155 | Precise range and attack-pass control. |
| Turn rate | 82 | Keeps the missile hardpoints and axial weapon aligned. |
| Turn acceleration | 165 | Aggressive, highly responsive handling. |
| Mass | 700 | Substantial enough to feel like a destroyer, not an enlarged frigate. |
| Shield type | Omni | Prototype-grade full defensive control. |
| Shield arc | 360 | Supports aggressive maneuvering under crossfire. |
| Shield upkeep | 0.04 | Very low passive burden. |
| Shield efficiency | 0.35 | Slightly stronger than DiAnn's current shield target. |
| Supplies/month | 11 | Expensive dedicated combat readiness. |
| Supplies/recovery | 16 | Reflects prototype complexity and combat power. |
| Fuel/ly | 2 | Standard destroyer combat logistics. |
| Max burn | 11 | Keeps pace with fast strike fleets. |
| Cargo | 90 | Ammunition and combat stores only. |
| Fuel | 160 | Normal operational reserve, not exploration range. |
| Crew minimum | 55 | Advanced automation reduces crew needs. |
| Crew maximum | 170 | Destroyer-scale complement. |
| CR recovery/day | 4% | Strong readiness recovery without exploration specialization. |
| CR to deploy | 20% | Its exceptional combat value carries a meaningful deployment cost. |
| Peak CR seconds | 420 | Sufficient for sustained battles, but below expedition-cruiser endurance. |

These targets place it modestly above the DiAnn baseline in direct hull, armor, flux, and mobility while removing the DiAnn's two fighter bays. The additional power is concentrated into its integrated weapon cycle, not free utility.

## Weapon Layout

The Witch sprite supports seven slots. Preserve every source coordinate and visible mount rather than adding unsupported hardpoints.

Proposed first-pass slot plan:

| Slot | Size | Type | Mount | Location | Arc | Role |
| --- | --- | --- | --- | --- | ---: | --- |
| `WS0001` | Medium | Missile | Hardpoint | `[36, 52]` | Fixed | Port assault battery. |
| `WS0004` | Medium | Missile | Hardpoint | `[36, -52]` | Fixed | Starboard assault battery. |
| `WS0007` | Large | Built-in | Hidden | `[12.5, 0]` | Fixed | Integrated axial heavy weapon. |
| `WS0005` | Small | Energy | Turret | `[40, 22]` | 240° | Forward pressure and point defense. |
| `WS0006` | Small | Energy | Turret | `[40, -22]` | 240° | Forward pressure and point defense. |
| `WS0002` | Small | Energy | Turret | `[-17, 23]` | 240° | Lateral and aft point defense. |
| `WS0003` | Small | Energy | Turret | `[-17, -23]` | 240° | Lateral and aft point defense. |

This is a deliberately compact weapon grid. The two medium missile mounts and integrated large weapon provide heavy striking power; the four small turrets make the ship self-defending without turning it into a broadside cruiser.

Do not expose `WS0007` as a normal player-changeable large slot during the first pass. The sprite and source hull treat it as an internal weapon, and making it a general large mount would both weaken the visual identity and create avoidable loadout extremes.

## Integrated Axial Weapon

Recommended first-pass approach: bind a verified vanilla large energy weapon to `WS0007` as a built-in.

Preferred test weapon: `tachyonlance`

Role:

- Converts missile-created overloads and armor openings into decisive damage.
- Gives the destroyer credible reach against cruisers.
- Provides precision rather than constant indiscriminate damage.
- Preserves the source hull's hidden large built-in architecture without retaining `FM_Masterspark`.

The Tachyon Lance is a test implementation, not necessarily the final fiction. If the ship's identity is approved and custom content is desired later, replace it with a Toranaga-owned weapon such as `Mitchell Axial Lance` or `Dominion Lance`.

Desired custom-weapon traits:

- Large built-in energy weapon.
- Long-range, high-precision burst.
- Significant flux cost so timing matters.
- Strong armor/hull finishing or EMP exploitation.
- Clearly telegraphed charge and firing effect.
- No independent ammunition system.

The weapon should not erase cruisers by itself. The intended power comes from synchronizing it with the missile batteries and ship system.

## Missile Philosophy

The medium missile hardpoints are the ship's defining player-configurable weapons.

They should support several assault patterns:

- Kinetic missiles to force shield overloads for the axial lance.
- High-explosive missiles to open armor before an energy finishing strike.
- Guided strike missiles for pursuit and cruiser elimination.
- Sustained missile options for longer engagements.

Because the mounts sit far out on the lateral structures, preserve their exact source coordinates and verify projectile clearance in combat. Their fixed orientation makes ship handling and attack angle meaningful.

## Ship System

Recommended first-pass system: `fastmissileracks`

Player-facing design direction: `Assault Weapons Synchronization`

Role: enable a second decisive missile sequence and reinforce aggressive attack timing.

Why it fits:

- Directly supports the Witch sprite's two most prominent configurable heavy mounts.
- Gives the ship a unique rhythm relative to the energy-focused family hulls.
- Rewards commitment and target selection rather than passive defense.
- Uses stable vanilla behavior for the first implementation.

Desired custom system behavior for a later pass:

- Rapidly replenishes or accelerates the missile batteries.
- Briefly improves weapon turn rate and projectile guidance.
- Modestly reduces weapon flux cost or improves the axial weapon's charge timing.
- Provides no major defensive bonus.
- Does not grant invulnerability or an easy disengagement.

If custom synchronization proves too broad or difficult to communicate, retain Fast Missile Racks. It already expresses the ship's core offensive loop cleanly.

## Built-In Hullmods

Recommended built-ins:

- `advancedoptics`
- `turretgyros`
- `eccm` if compatible with the intended missile choices and verified as a valid built-in ID
- `expanded_missile_racks` only if Fast Missile Racks testing shows the base ammunition pool is too restrictive

Use restraint with missile stacking. Fast Missile Racks, expanded ammunition, elite flux stats, and a large built-in weapon can compound rapidly. Add `expanded_missile_racks` only after combat testing rather than assuming it is necessary.

Avoid built-ins:

- Exploration and survey hullmods.
- Efficiency or logistics packages.
- Fighter and carrier hullmods.
- Civilian-grade systems.
- Mobility hullmods that make the already-high base handling physically erratic.
- The source-only `FantasyBasicMod` and `high_scatter_amp` dependencies.

## Fighter and Drone Question

The Witch reference has no launch bays or built-in wings. The Brian Stokes Mitchell should preserve that identity.

Recommended baseline:

- `0` fighter bays.
- No built-in wing.
- No decorative drone system.

This is an important distinction from DiAnn/Nebula. All deployment points and ordnance investment should be visible in the destroyer's own direct combat performance.

## Variants

Initial implementation should include one complete player-facing variant.

### `brianstokesmitchell_elite`

Purpose: default breakthrough and cruiser-hunter loadout.

Suggested fit:

- `WS0001` and `WS0004`: complementary medium missiles chosen to create and exploit defensive failure.
- `WS0007`: built-in Tachyon Lance for the first test pass.
- `WS0005` and `WS0006`: forward energy weapons for pressure or close point defense.
- `WS0002` and `WS0003`: efficient point-defense weapons with good AI behavior.
- Vents prioritized before capacitors until the axial weapon's flux cycle is proven.
- Hullmods focused on missile reliability, range, shield control, and sustained flux performance.

Preferred first-pass loadout behavior:

- Strong enough to destroy ordinary destroyers rapidly.
- Able to defeat cruisers through attack sequencing rather than raw durability.
- Resistant to fighters and missiles without making the four small turrets a primary damage battery.
- Capable of continuing to fight after the initial missile exchange.

Possible future variants:

- `brianstokesmitchell_breakthrough`
- `brianstokesmitchell_hunter`
- `brianstokesmitchell_siege`
- `brianstokesmitchell_testbed`

## Campaign Characteristics

The Brian Stokes Mitchell receives no specialized campaign bonuses.

Recommended logistics identity:

- Normal destroyer fuel consumption and operational range.
- Low cargo and fuel reserves.
- High supply cost for its hull size.
- No survey, salvage, sensor, navigation, or terrain bonuses.
- High base value and rare availability.

It should be desirable because it wins fights, not because it replaces freighters, tankers, survey ships, or the Ronald Martin.

## Campaign Integration

Minimum campaign implementation:

- Add the hull definition.
- Copy the ship sprite.
- Add the elite variant.
- Add the ship data row.
- Add description text.
- Verify the built-in axial weapon ID.

Preferred campaign identity:

- Rare late-Domain prototype.
- Not common market stock.
- Appropriate as a high-threat fleet centerpiece, special reward, or limited prototype companion.
- Related to Toranaga program content without replacing the Toranaga as flagship.

The first implementation should not require custom acquisition missions or production systems.

## Description Text Direction

Tone: forceful, technical, and controlled.

The description should present the Brian Stokes Mitchell as the result of removing cost, manufacturability, and role-flexibility constraints from destroyer development. It was built to engage superior forces, create a local breakthrough, and destroy the most important hostile vessel before conventional reinforcements could respond.

Emphasize:

- Pure combat specialization.
- Coordinated missile and axial-weapon fire.
- Exceptional destroyer mobility and reactor performance.
- Trial results against larger ships.
- Extreme cost and low production numbers.

Avoid:

- Exploration or scientific capability.
- Carrier or escort framing.
- Describing it as a small cruiser.
- Implying it was mass-produced.
- Claiming that the built-in weapon alone accounts for its combat superiority.

## Asset Plan

Required assets:

- `Toranaga/graphics/ships/brianstokesmitchell.png`

Optional future assets:

- Custom axial weapon projectile and effects.
- Custom system icon for Assault Weapons Synchronization.
- Custom weapon icon and description assets.

Sprite strategy:

- Copy `FM_Witch.png` exactly for the first implementation.
- Preserve dimensions: `130x190`.
- Preserve center: `[65, 93]`.
- Preserve collision radius: `93`.
- Preserve shield center `[0, 0]` and radius `90.5`.
- Preserve source bounds and all ten engine slots.
- Preserve all seven weapon coordinates and the hidden status of `WS0007`.
- Use `HIGH_TECH` engine styling and a Toranaga-compatible ship style.
- Do not retain `FM`, `FantasyBasicMod`, `FM_Masterspark`, or other dependencies on the inspiration mod.

## File Plan

Expected first-pass implementation files:

- `Toranaga/data/hulls/brianstokesmitchell.ship`
- `Toranaga/data/variants/brianstokesmitchell_elite.variant`
- `Toranaga/data/hulls/ship_data.csv`
- `Toranaga/data/strings/descriptions.csv`
- `Toranaga/graphics/ships/brianstokesmitchell.png`

If a custom axial weapon or system is approved later, additional files may include:

- `Toranaga/data/weapons/weapon_data.csv`
- `Toranaga/data/weapons/mitchell_axial_lance.wpn`
- `Toranaga/graphics/weapons/...`
- `Toranaga/graphics/fx/...`
- `Toranaga/graphics/icons/hullsys/...`
- `Toranaga/jars/src/.../AssaultWeaponsSynchronizationStats.java`

The exact Java package should follow the existing mod source structure discovered during implementation.

## Testing Plan

After implementation:

- Confirm no core or inspiration ID collision for `brianstokesmitchell` or its variant.
- Confirm the mod loads without JSON, CSV, weapon, style, or hullmod errors.
- Confirm the sprite displays at the source scale and orientation.
- Confirm both missile hardpoints align with the lateral structures and fire clear of the hull.
- Confirm all four small turrets align and cover the intended arcs.
- Confirm the hidden axial weapon fires from the correct central position.
- Confirm collision bounds and shield radius cover the sprite correctly.
- Confirm all ten engine glows align, especially the four lateral maneuvering exhausts.
- Test Fast Missile Racks with limited-ammo and regenerating missile choices.
- Test AI timing of missiles, system activation, and the built-in axial weapon.
- Test against vanilla destroyers, cruisers, capitals, fighter pressure, and mixed fleets.
- Confirm it defeats ordinary destroyers decisively and threatens cruisers without becoming invulnerable.
- Confirm mobility feels like an exceptional destroyer, not a frigate with destroyer mass.
- Compare directly with DiAnn/Nebula to verify that the two destroyers have distinct roles and similar overall family value.
- Test campaign supply consumption, recovery, burn speed, cargo, and fuel to confirm the absence of hidden logistics advantages.

## Open Review Questions

- Should the first-pass axial weapon be the vanilla Tachyon Lance, or should a custom Mitchell Axial Lance be required before implementation?
- Should the twin medium hardpoints remain missile-only, or become synergy mounts for more loadout flexibility?
- Should the ship use plain `fastmissileracks`, or should Assault Weapons Synchronization be custom from the start?
- Should `expanded_missile_racks` become built-in after testing, or should ammunition remain a meaningful limit?
- Should the four small energy turrets be entirely player-configurable or include integrated point-defense weapons?
- Should the default variant use kinetic missiles to set up the axial weapon, or mixed kinetic/high-explosive missiles for independence?
- Should the sprite palette remain an exact Witch copy for the first implementation, or receive a later Toranaga-family color pass?

## Review Gate

Implementation should not begin until this document is reviewed and approved.
