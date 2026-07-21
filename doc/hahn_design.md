# Hahn-Class Frigate

## Implementation Design Document

Status: Draft for review before implementation.

Source brief: `doc/raychen.md` (shared with the RayChen-class; see [Relationship to the RayChen](#relationship-to-the-raychen) below)

Visual inspiration: `inspiration/scalartech-solutions-0.9.3b/graphics/tahlan/ships/tahlan_curl.png`

Reference hull: `inspiration/scalartech-solutions-0.9.3b/data/hulls/tahlan_curl.ship`

---

## Relationship to the RayChen

The Hahn is a second frigate-scale realization of the same design brief (`doc/raychen.md`) that produced the RayChen. Both ships share the same design philosophy, mission, and family technologies. They are not variants of the same hull — they are two independent answers to the same brief, built from different source hulls, and should end up feeling like siblings rather than duplicates.

Where the RayChen is built from the Tahlan Skirt (a blade-like, four-forward-hardpoint silhouette), the Hahn is built from the Tahlan Curl: a rounder, more enclosed hull with a mixed missile/energy weapon spread and a distinctive six-engine rear cluster. The Curl's layout naturally pulls the Hahn toward a slightly different combat identity within the same philosophy:

- The RayChen reads as a pure energy-weapon duelist with all firepower on the nose.
- The Hahn has two forward missile hardpoints in addition to its energy slots, giving it an opening-strike/finisher tool that the RayChen lacks, plus turret-mounted energy weapons (vs. the RayChen's fixed hardpoints) that give it a little more flexibility to track targets off-axis.
- The Curl hull is more compact and rounder (108x105) than the Skirt (100x124), and its shield is offset (`[-3.5, 0]`) rather than centered, which should be preserved as a small asymmetry in the Hahn's shield feel rather than corrected away.

Both ships should still clearly read as members of the Toranaga family (see Visual Style in `doc/raychen.md`), and both should clearly read as distinct from each other in a side-by-side comparison.

---

## Design Goal

The Hahn is the frigate-scale member of the Toranaga program family: a no-compromise Domain prototype built to define the upper limit of frigate performance.

The ship is intentionally stronger than vanilla frigates. It should not feel like a fair early-game frigate or a cheap fleet filler. It should feel like an elite interceptor that wins through speed, precision, shield control, and overwhelming reactor efficiency.

The design should avoid turning the Hahn into a miniature cruiser. It should remain physically and tactically frigate-like: small, fast, responsive, and dangerous because it is hard to pin down.

## Naming and ID Direction

Player-facing name: `Hahn`

Recommended internal IDs:

- Hull ID: `hahn`
- Elite variant ID: `hahn_elite`
- Sprite path: `graphics/ships/hahn.png`
- Hull file: `Toranaga/data/hulls/hahn.ship`
- Variant file: `Toranaga/data/variants/hahn_elite.variant`

Important lesson from the DiAnn/Nebula work: do not use a hull ID or file name that collides with vanilla Starsector or another known mod. Before implementation, search core and inspiration data for `hahn` to confirm it is unique.

## Visual Direction

The Hahn should look like the Tahlan Curl reference.

Key Curl visual facts:

- Sprite: `tahlan_curl.png`
- Width: `108`
- Height: `105`
- Center: `[54, 60]`
- Collision radius: `80`
- Shield center: `[-3.5, 0]` (off-center toward the stern — preserve this asymmetry)
- Shield radius: `71.5`
- Hull size: `FRIGATE`
- Source weapon layout: two forward missile hardpoints, one forward-fixed energy hardpoint, two near-center energy turrets
- Source engine layout: a compact quad of small engines plus a large primary rear engine and a secondary rear engine — six engine slots total
- Source identity: rounder, more enclosed frigate silhouette, less blade-like than the Skirt

Recommended sprite strategy:

- Copy `tahlan_curl.png` exactly as `Toranaga/graphics/ships/hahn.png` for the first implementation.
- Preserve Curl dimensions and center values.
- Use exact Curl bounds, engine slots, and shield geometry unless testing proves a clear reason to adjust.
- Do not scale or pad the sprite during first implementation.

## Ship Class

Recommended hull size: `FRIGATE`

The Hahn must remain visibly and mechanically distinct from the DiAnn destroyer and Toranaga cruiser, and from its sibling RayChen. It can outperform ordinary frigates by a large margin, but it should still be a frigate in footprint, deployment role, maneuvering style, and tactical vulnerability to mistakes.

Recommended combat role tags:

- Elite frigate
- Interceptor
- Hunter-killer
- Fleet screen
- Pursuit frigate
- Prototype

## Core Combat Identity

The Hahn controls engagement timing, same as the RayChen, but leans slightly more on burst opening damage before settling into sustained pressure.

Combat feel:

- Blindingly fast.
- Nearly instant acceleration and deceleration.
- Extremely responsive turning and strafing.
- Strong enough to bully ordinary frigates and threaten destroyers.
- Able to pressure cruisers through positioning rather than raw cruiser-scale firepower.
- A forward missile alpha strike on approach, followed by sustained energy turret pressure once in range.
- Shield-first defense with very low upkeep, offset slightly toward the stern per the Curl's native shield geometry.
- High dissipation for near-continuous weapon pressure.
- Punished by being cornered, surrounded, or caught by area denial weapons.

## Proposed Baseline Stats

These are first-pass implementation targets and should be adjusted after simulator testing. Kept in line with the RayChen's baseline (see `doc/raychen_design.md`) so the two ships remain balanced siblings rather than one outclassing the other.

| Stat | Proposed Value | Intent |
| --- | ---: | --- |
| Hull size | Frigate | Keeps the Hahn in its intended role. |
| Ordnance points | 95 | Matches RayChen; very high for a frigate, supports elite fittings. |
| Hull | 3,800 | Strong for a frigate, but not a tank. |
| Armor | 450 | Forgives mistakes without making it armor-centric. |
| Flux capacity | 10,000 | Prototype reactor reserve. |
| Flux dissipation | 950 | Sustains shield and weapon pressure. |
| Fighter bays | 0 | Avoids making the Hahn a carrier. |
| Max speed | 185 | Slightly below the RayChen; the Curl's rounder hull trades a hair of top speed for the missile slots. |
| Acceleration | 255 | Near-instant response. |
| Deceleration | 235 | Allows precise strike passes. |
| Turn rate | 130 | Slightly higher than RayChen; the turret-mounted energy slots reward keeping the nose loosely on target rather than locked on. |
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
| Fuel | 60 | Better than Curl baseline, still not exploration-focused. |
| Crew minimum | 12 | Advanced automation and compact systems. |
| Crew maximum | 40 | Frigate-scale crew footprint. |
| CR to deploy | 12 | Expensive but usable elite frigate. |
| Peak CR seconds | 300 | Enough endurance for decisive engagements. |

## Weapon Layout

The source brief suggests:

- 1 large weapon mount
- 2 medium weapon mounts
- 4 small weapon mounts

The Curl reference sprite, like the Skirt, does not visually support seven normal visible mounts. Its actual hull has five compact slots:

- `WS0001`: small missile hardpoint at `[34, 19]`
- `WS0002`: small missile hardpoint at `[34, -19]`
- `WS0003`: small energy hardpoint (fixed forward) at `[39, 0]`
- `WS0004`: small energy turret at `[10, 17]`, 180-degree arc
- `WS0005`: small energy turret at `[10, -17]`, 180-degree arc

This is a meaningfully different shape from the RayChen's four fixed forward hardpoints: the Hahn trades one visible mount for a missile pair, and its two energy mounts are turrets rather than hardpoints, giving it a wider effective firing arc at the cost of pure forward alpha.

Recommended first-pass compromise:

- Preserve all five visible Curl mounts.
- Upgrade power through slot size/type and built-in weapon choices rather than adding floating hardpoints.
- Use exact Curl coordinates, arcs, and angles for all visible slots.

Proposed first-pass slot plan:

| Slot | Size | Type | Mount | Location | Arc | Role |
| --- | --- | --- | --- | --- | --- | --- |
| `WS0001` | Small | Missile | Hardpoint | `[34, 19]` | 5° | Opening strike / finisher. |
| `WS0002` | Small | Missile | Hardpoint | `[34, -19]` | 5° | Opening strike / finisher. |
| `WS0003` | Medium | Energy | Hardpoint | `[39, 0]` | 5° | Primary forward pressure. |
| `WS0004` | Small | Energy | Turret | `[10, 17]` | 180° | Sustained pressure, tracks off-axis targets. |
| `WS0005` | Small | Energy | Turret | `[10, -17]` | 180° | Sustained pressure, tracks off-axis targets. |

This creates a frigate with a distinct rhythm from the RayChen — missile pressure into an approach, energy turrets for the brawl — while respecting the sprite. If the user strongly wants the full `1 large / 2 medium / 4 small` fantasy later, that should be a custom-art or visual-editor phase, not a blind `.ship` slot expansion.

## Ship System

Recommended first-pass system: `maneuveringjets` or `phasecharge`, matching the RayChen's direction so the two ships pilot similarly at the core.

Preferred design direction: `Vector Thrusters`

Role: aggressive repositioning and pursuit.

Desired behavior:

- Increases speed, acceleration, deceleration, and turn rate.
- Enables sharp attack angles and rapid disengagement.
- Rewards closing, flanking, and finishing rather than passive kiting.
- Should synergize with the missile hardpoints by letting the Hahn open a fight from an optimal angle rather than just running straight in.

Possible first-pass implementation:

- Use `maneuveringjets` if mobility feel is the priority.
- Use `highenergyfocus` only if the first implementation needs more weapon pressure.
- Defer custom Java until the hull, slots, and balance direction are stable.

## Built-In Hullmods

Recommended built-ins:

- `advancedoptics`
- `turretgyros` (particularly relevant here since two of the five mounts are turrets, unlike the RayChen's all-hardpoint layout)
- `unstable_injector` if testing shows it does not make handling too slippery
- `hardenedshieldemitter` or `stabilizedshieldemitter` if available and compatible

Avoid built-ins:

- Exploration or logistics hullmods.
- Fighter/carrier hullmods.
- Anything that makes the Hahn feel like a carrier or support craft.

## Drone/Wing Question

Unlike the Tahlan Skirt (which has a built-in drone wing), the Tahlan Curl reference hull has no built-in wing data. This makes the "no fighter bays" decision simpler for the Hahn than it was for the RayChen: there is no source drone identity to preserve or discard.

For the Hahn first pass, the recommendation is `0` fighter bays and no wing data, matching the RayChen and keeping both ships distinct from the DiAnn's two-bay identity.

## Variants

Initial implementation should include one complete player-facing variant.

### `hahn_elite`

Purpose: default elite interceptor.

Suggested fit:

- `WS0001`: Harpoon MRM, Sabot Pod, or similar light strike missile.
- `WS0002`: Harpoon MRM, Sabot Pod, or similar light strike missile.
- `WS0003`: Pulse Laser or Heavy Blaster depending on slot tuning.
- `WS0004`: Tactical Laser, Ion Cannon, or a built-in precision weapon.
- `WS0005`: Tactical Laser, Ion Cannon, or a built-in precision weapon.
- Max vents before capacitors.
- Hullmods focused on shield efficiency, acceleration, and weapon control.

Preferred first-pass weapon direction:

- Avoid weapons that instantly overload the ship despite its strong reactor.
- Favor missiles that reward a well-timed opening pass rather than passive spam (limited ammo, no built-in reload expected on the small hardpoints).
- Favor energy turret weapons with clean tracking and good AI behavior at the 180-degree arc.
- Keep the loadout strong enough to delete ordinary frigates quickly.

Possible future variants:

- `hahn_interceptor`
- `hahn_duelist`
- `hahn_pursuit`
- `hahn_testbed`

## Campaign Integration

Minimum campaign implementation:

- Add hull definition.
- Add ship sprite.
- Add elite variant.
- Add ship data row.
- Add description text.

Preferred campaign identity:

- Rare Domain prototype, sibling to the RayChen rather than a replacement for it.
- Related to Toranaga, DiAnn, and the same late-Domain weapons program.
- Not common market stock.
- Possible reward ship, unique start ship, or special prototype escort later.

## Description Text Direction

Tone: fast, technical, precise, prestigious — consistent with the RayChen's description, but should note the Hahn as a parallel line of development rather than a reskin. It should emphasize mobility, responsiveness, and tactical superiority, not endurance or logistical flexibility. Where the RayChen's text can lean on "fastest, most precise," the Hahn's text should lean on its opening-strike missile capability paired with the same elite mobility.

Avoid:

- Calling it a carrier.
- Framing it as a mini cruiser.
- Making it sound mass-produced.
- Describing it as a reskin or upgrade of the RayChen — it is a sibling design, not a successor.

## Asset Plan

Required assets:

- `Toranaga/graphics/ships/hahn.png`

Sprite strategy:

- Copy `tahlan_curl.png` exactly for the first implementation.
- Preserve Curl dimensions: `108x105`.
- Preserve Curl center: `[54, 60]`.
- Preserve Curl shield geometry: `[-3.5, 0]`, radius `71.5`.
- Preserve Curl bounds and all six engine slots unless testing proves a concrete issue.

## File Plan

Expected implementation files:

- `Toranaga/data/hulls/hahn.ship`
- `Toranaga/data/variants/hahn_elite.variant`
- `Toranaga/data/hulls/ship_data.csv`
- `Toranaga/data/strings/descriptions.csv`
- `Toranaga/graphics/ships/hahn.png`

Custom code is not expected for the first pass.

## Testing Plan

After implementation:

- Confirm no vanilla/core ID collision for `hahn` or `hahn_elite`.
- Confirm the mod loads without JSON or CSV errors.
- Confirm the sprite displays at correct scale and orientation.
- Confirm weapon slots align with the Curl visible hardpoints and turrets, including correct turret arcs.
- Confirm shields raise without excessive passive flux, and that the off-center shield geometry feels intentional rather than buggy.
- Confirm mobility feels elite-frigate fast, not physically absurd.
- Test against vanilla frigates, destroyers, and light cruisers.
- Test alongside Toranaga and DiAnn to confirm shared family feel.
- Test alongside the RayChen specifically to confirm the two frigates feel like distinct siblings rather than duplicates.

## Open Review Questions

- Should the Hahn preserve exactly five visible mounts, or should later custom art support the brief's full seven-mount layout?
- Should the missile hardpoints (`WS0001`/`WS0002`) be player-changeable small missile mounts or built-in precision weapons?
- Should the ship use `maneuveringjets`, `highenergyfocus`, or another vanilla system for the first pass?
- Should the Hahn's off-center shield geometry be preserved as-is, or nudged toward center for gameplay clarity?
- Should the default elite loadout lean sustained pressure or burst assassination?
- How much stat differentiation from the RayChen is desired — should the Hahn be a near-mirror with a different weapon flavor, or should its baseline stats diverge further to reflect the missile/turret identity?

## Review Gate

Implementation should not begin until this document is reviewed and approved.
