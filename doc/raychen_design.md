# RayChen-Class Frigate

## Implementation Design Document

Status: Draft for review before implementation.

Source brief: `doc/raychen.md`

Visual inspiration: `inspiration/scalartech-solutions-0.9.3b/graphics/tahlan/ships/tahlan_skirt.png`

Reference hull: `inspiration/scalartech-solutions-0.9.3b/data/hulls/tahlan_skirt.ship`

---

## Design Goal

The RayChen is the frigate-scale member of the Toranaga program family: a no-compromise Domain prototype built to define the upper limit of frigate performance.

The ship is intentionally stronger than vanilla frigates. It should not feel like a fair early-game frigate or a cheap fleet filler. It should feel like an elite interceptor that wins through speed, precision, shield control, and overwhelming reactor efficiency.

The design should avoid turning the RayChen into a miniature cruiser. It should remain physically and tactically frigate-like: small, fast, responsive, and dangerous because it is hard to pin down.

## Naming and ID Direction

Player-facing name: `RayChen`

Recommended internal IDs:

- Hull ID: `raychen`
- Elite variant ID: `raychen_elite`
- Sprite path: `graphics/ships/raychen.png`
- Hull file: `Toranaga/data/hulls/raychen.ship`
- Variant file: `Toranaga/data/variants/raychen_elite.variant`

Important lesson from the DiAnn/Nebula work: do not use a hull ID or file name that collides with vanilla Starsector or another known mod. Before implementation, search core and inspiration data for `raychen` to confirm it is unique.

## Visual Direction

The RayChen should look like the Tahlan Skirt reference.

Key Skirt visual facts:

- Sprite: `tahlan_skirt.png`
- Width: `100`
- Height: `124`
- Center: `[50, 54.5]`
- Collision radius: `97`
- Shield center: `[0, 0]`
- Shield radius: `90.5`
- Hull size: `FRIGATE`
- Source weapon layout: four compact forward hardpoints
- Source engine layout: strong rear cluster and side thrusters
- Source identity: fast, compact, blade-like frigate silhouette

Recommended sprite strategy:

- Copy `tahlan_skirt.png` exactly as `Toranaga/graphics/ships/raychen.png` for the first implementation.
- Preserve Skirt dimensions and center values.
- Use exact Skirt bounds, engine slots, and shield geometry unless testing proves a clear reason to adjust.
- Do not scale or pad the sprite during first implementation.

## Ship Class

Recommended hull size: `FRIGATE`

The RayChen must remain visibly and mechanically distinct from the DiAnn destroyer and Toranaga cruiser. It can outperform ordinary frigates by a large margin, but it should still be a frigate in footprint, deployment role, maneuvering style, and tactical vulnerability to mistakes.

Recommended combat role tags:

- Elite frigate
- Interceptor
- Hunter-killer
- Fleet screen
- Pursuit frigate
- Prototype

## Core Combat Identity

The RayChen controls engagement timing.

Combat feel:

- Blindingly fast.
- Nearly instant acceleration and deceleration.
- Extremely responsive turning and strafing.
- Strong enough to bully ordinary frigates and threaten destroyers.
- Able to pressure cruisers through positioning rather than raw cruiser-scale firepower.
- Shield-first defense with very low upkeep.
- High dissipation for near-continuous weapon pressure.
- Punished by being cornered, surrounded, or caught by area denial weapons.

## Proposed Baseline Stats

These are first-pass implementation targets and should be adjusted after simulator testing.

| Stat | Proposed Value | Intent |
| --- | ---: | --- |
| Hull size | Frigate | Keeps the RayChen in its intended role. |
| Ordnance points | 95 | Very high for a frigate; supports elite fittings. |
| Hull | 3,800 | Strong for a frigate, but not a tank. |
| Armor | 450 | Forgives mistakes without making it armor-centric. |
| Flux capacity | 10,000 | Prototype reactor reserve. |
| Flux dissipation | 950 | Sustains shield and weapon pressure. |
| Fighter bays | 0 | Avoids making the RayChen a carrier; Skirt's source drone can be represented later if desired. |
| Max speed | 190 | Defines the ship as the fastest family member. |
| Acceleration | 260 | Near-instant response. |
| Deceleration | 240 | Allows precise strike passes. |
| Turn rate | 125 | Lets the ship keep guns and shields aligned. |
| Turn acceleration | 220 | High pilot responsiveness. |
| Shield type | Omni | Prototype-grade defensive control. |
| Shield arc | 360 | Full coverage for aggressive close movement. |
| Shield upkeep | 0.03 | Minimal passive burden. |
| Shield efficiency | 0.35 | Extremely efficient, consistent with overpowered intent. |
| Supplies/month | 6 | Costly for a frigate but lighter than larger prototypes. |
| Supplies/recovery | 8 | Prototype recovery cost. |
| Fuel/ly | 1 | Standard frigate logistics. |
| Max burn | 12 | Leads pursuit groups and fast fleets. |
| Cargo | 35 | Minimal utility. |
| Fuel | 60 | Better than Skirt, still not exploration-focused. |
| Crew minimum | 12 | Advanced automation and compact systems. |
| Crew maximum | 40 | Frigate-scale crew footprint. |
| CR to deploy | 12 | Expensive but usable elite frigate. |
| Peak CR seconds | 300 | Enough endurance for decisive engagements. |

## Weapon Layout

The source brief suggests:

- 1 large weapon mount
- 2 medium weapon mounts
- 4 small weapon mounts

The Skirt reference sprite does not visually support seven normal visible mounts. Its actual hull has four compact forward hardpoints:

- `WS0001`: small energy hardpoint at `[22.5, 32]`
- `WS0002`: small energy hardpoint at `[22.5, -32]`
- `WS0003`: small built-in hardpoint at `[41.5, 7]`
- `WS0004`: small built-in hardpoint at `[41.5, -7]`

Recommended first-pass compromise:

- Preserve four visible forward mounts.
- Upgrade power through slot size/type and built-in weapon choices rather than adding floating hardpoints.
- Use exact Skirt coordinates for all visible slots.

Proposed first-pass slot plan:

| Slot | Size | Type | Mount | Location | Role |
| --- | --- | --- | --- | --- | --- |
| `WS0001` | Medium | Energy | Hardpoint | `[22.5, 32]` | Primary forward pressure. |
| `WS0002` | Medium | Energy | Hardpoint | `[22.5, -32]` | Primary forward pressure. |
| `WS0003` | Small | Energy or Built-in | Hardpoint | `[41.5, 7]` | Precision finisher or built-in lance. |
| `WS0004` | Small | Energy or Built-in | Hardpoint | `[41.5, -7]` | Precision finisher or built-in lance. |

This creates a very dangerous frigate while respecting the sprite. If the user strongly wants the full `1 large / 2 medium / 4 small` fantasy later, that should be a custom-art or visual-editor phase, not a blind `.ship` slot expansion.

## Ship System

Recommended first-pass system: `maneuveringjets` or `phasecharge`

Preferred design direction: `Vector Thrusters`

Role: aggressive repositioning and pursuit.

Desired behavior:

- Increases speed, acceleration, deceleration, and turn rate.
- Enables sharp attack angles and rapid disengagement.
- Rewards closing, flanking, and finishing rather than passive kiting.

Possible first-pass implementation:

- Use `maneuveringjets` if mobility feel is the priority.
- Use `highenergyfocus` only if the first implementation needs more weapon pressure.
- Defer custom Java until the hull, slots, and balance direction are stable.

## Built-In Hullmods

Recommended built-ins:

- `advancedoptics`
- `turretgyros`
- `unstable_injector` if testing shows it does not make handling too slippery
- `hardenedshieldemitter` or `stabilizedshieldemitter` if available and compatible

Avoid built-ins:

- Exploration or logistics hullmods.
- Fighter/carrier hullmods.
- Anything that makes the RayChen feel like a carrier or support craft.

## Drone/Wing Question

The Skirt source hull has one built-in wing:

- `tahlan_plaid_drone_wing`

For the RayChen first pass, the recommendation is `0` fighter bays and no wing data. The RayChen brief describes a pure combat frigate, and keeping it bayless makes it more distinct from the DiAnn's two-bay identity.

If a later pass wants to preserve the Skirt drone identity, add a single built-in decorative or defensive drone only after verifying vanilla/available wing IDs and ensuring it does not alter the ship's role.

## Variants

Initial implementation should include one complete player-facing variant.

### `raychen_elite`

Purpose: default elite interceptor.

Suggested fit:

- `WS0001`: Pulse Laser or Heavy Blaster depending on slot tuning.
- `WS0002`: Pulse Laser or Heavy Blaster depending on slot tuning.
- `WS0003`: Tactical Laser, Ion Cannon, or a built-in precision weapon.
- `WS0004`: Tactical Laser, Ion Cannon, or a built-in precision weapon.
- Max vents before capacitors.
- Hullmods focused on shield efficiency, acceleration, and weapon control.

Preferred first-pass weapon direction:

- Avoid weapons that instantly overload the ship despite its strong reactor.
- Favor weapons with clean forward pressure and good AI behavior.
- Keep the loadout strong enough to delete ordinary frigates quickly.

Possible future variants:

- `raychen_interceptor`
- `raychen_duelist`
- `raychen_pursuit`
- `raychen_testbed`

## Campaign Integration

Minimum campaign implementation:

- Add hull definition.
- Add ship sprite.
- Add elite variant.
- Add ship data row.
- Add description text.

Preferred campaign identity:

- Rare Domain prototype.
- Related to Toranaga, DiAnn, and the same late-Domain weapons program.
- Not common market stock.
- Possible reward ship, unique start ship, or special prototype escort later.

## Description Text Direction

Tone: fast, technical, precise, prestigious.

The description should present the RayChen as the program's answer to the question of how far frigate performance could be pushed when cost and manufacturability were ignored. It should emphasize mobility, responsiveness, and tactical superiority, not endurance or logistical flexibility.

Avoid:

- Calling it a carrier.
- Framing it as a mini cruiser.
- Making it sound mass-produced.

## Asset Plan

Required assets:

- `Toranaga/graphics/ships/raychen.png`

Sprite strategy:

- Copy `tahlan_skirt.png` exactly for the first implementation.
- Preserve Skirt dimensions: `100x124`.
- Preserve Skirt center: `[50, 54.5]`.
- Preserve Skirt shield geometry: `[0, 0]`, radius `90.5`.
- Preserve Skirt bounds and engine slots unless testing proves a concrete issue.

## File Plan

Expected implementation files:

- `Toranaga/data/hulls/raychen.ship`
- `Toranaga/data/variants/raychen_elite.variant`
- `Toranaga/data/hulls/ship_data.csv`
- `Toranaga/data/strings/descriptions.csv`
- `Toranaga/graphics/ships/raychen.png`

Custom code is not expected for the first pass.

## Testing Plan

After implementation:

- Confirm no vanilla/core ID collision for `raychen` or `raychen_elite`.
- Confirm the mod loads without JSON or CSV errors.
- Confirm the sprite displays at correct scale and orientation.
- Confirm weapon slots align with the Skirt visible hardpoints.
- Confirm shields raise without excessive passive flux.
- Confirm mobility feels elite-frigate fast, not physically absurd.
- Test against vanilla frigates, destroyers, and light cruisers.
- Test alongside Toranaga and DiAnn to confirm shared family feel.

## Open Review Questions

- Should the RayChen preserve exactly four visible mounts, or should later custom art support the brief's full seven-mount layout?
- Should `WS0003` and `WS0004` be player-changeable small energy mounts or built-in precision weapons?
- Should the ship use `maneuveringjets`, `highenergyfocus`, or another vanilla system for the first pass?
- Should the RayChen have any built-in drone identity from the Skirt reference, or remain a pure no-bay frigate?
- Should the default elite loadout lean sustained pressure or burst assassination?

## Review Gate

Implementation should not begin until this document is reviewed and approved.
