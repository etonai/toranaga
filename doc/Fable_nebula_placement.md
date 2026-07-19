# Nebula Placement Failure — Root Cause Analysis

Date: 2026-07-18
Scope: Why the Nebula's sprite, shield, weapon markers, and bay markers refuse to line up in-game (DevCycle 002, Phase 3, mod versions `0.2.2`–`0.2.6`), and why no amount of coordinate tuning could ever have fixed it.

## Executive Summary

**The hull ID `nebula` collides with a vanilla Starsector ship.** Starsector 0.98a ships a *Nebula-class Civilian Transport* whose hull spec lives at exactly the same relative path the mod uses:

- Vanilla: `starsector-core/data/hulls/nebula.ship` — `"hullId": "nebula"`
- Mod: `Toranaga/data/hulls/nebula.ship` — `"hullId": "nebula"`

Because both the file path and the hull ID collide, the game does not load the mod's hull cleanly. The effective in-game hull spec is a *contaminated blend* of both files: it renders the mod's Tress-based sprite, but it applies the **vanilla ship's `center` value (`[60, 99]`)** — which was authored for a 120×200 transport sprite, not the 188×134 Tress sprite — and it carries the **vanilla ship's weapon slots** alongside the mod's.

The result is precisely every symptom in `doc/error/`:

1. The visible sprite renders **34 units to the right and 32 units aft** of the ship's logical center, so the ship sits low-right inside its shield and fighters/markers cluster up-left of the hull.
2. Four extra "ghost" slot markers appear that exist in **no version of the mod's hull file** — they are the vanilla Nebula's four **small ballistic turrets**. This is why the refit screen in `Screenshot 2026-07-18 174559.png` shows the tooltip **"Small Ballistic Turret (Empty)"**, a slot type the mod has never defined.
3. The ghost markers never move no matter how the mod's coordinates are edited, while the mod's own four slots *do* move — which is exactly the confusing mixed behavior the `0.2.4`–`0.2.6` attempts observed.

The Tress works in ScalarTech because its hull ID is `tahlan_tress` — namespaced, colliding with nothing. The mod's geometry was never wrong: version `0.2.3` (exact Tress values) would have rendered perfectly if the hull ID had been unique.

**Fix: rename the hull ID and file to a namespaced ID (e.g. `trng_nebula`), propagate the rename to every referencing file, and revert the slot coordinates to the exact Tress values.** No visual tuning is needed at all.

## Evidence

Every claim below was verified directly on this machine on 2026-07-18.

### 1. The sprite is not the problem

`Toranaga/graphics/ships/nebula.png` and `inspiration/scalartech-solutions-0.9.3b/graphics/tahlan/ships/tahlan_tress.png` have **identical MD5 hashes** (`e5fb4a8a071883d1fceded95bd459191`) and both are 188×134 pixels. The image is a byte-for-byte copy; no cropping, padding, or re-encoding occurred.

### 2. The deployed mod is not stale

The deployed copy at `C:\Program Files (x86)\Fractal Softworks\Starsector\mods\Toranaga\data\hulls\nebula.ship` is byte-identical to the repo copy, and the deployed `mod_info.json` reads version `0.2.6`. The Phase 3 open question "is the game consuming our edits?" is answered: yes, it is. (This is also proven by the `0.2.4` observation that shifting the mod's slots moved four of the markers.)

### 3. The Tress comparison never actually ran in this install

`enabled_mods.json` lists only `lw_console`, `ed-pics`, `lw_lazylib`, `speedUp`, `toranaga`. **ScalarTech is not installed in this game copy**, so "the original mod places the ship correctly" was observed elsewhere or previously — it was never an A/B comparison against the same install. The Tress data is nonetheless correct; it works because `tahlan_tress` is a unique ID.

### 4. Vanilla Starsector owns the `nebula` ID

`starsector-core/data/hulls/nebula.ship` defines:

| Field | Vanilla Nebula (transport) | Mod Nebula (Tress copy) |
| --- | --- | --- |
| `hullId` | `nebula` | `nebula` ⚠ collision |
| Sprite | `graphics/ships/nebula/nebula.png`, 120×200 | `graphics/ships/nebula.png`, 188×134 |
| `center` | `[60, 99]` | `[94, 66.5]` |
| Weapon slots | 4 × SMALL **BALLISTIC** turret (`WS 001`–`WS 004`) + 2 hidden SYSTEM | 4 × MEDIUM ENERGY (`WS0001`–`WS0004`) + 2 launch bays |
| `shieldCenter` / radius | `[1, 0]` / 120 | `[0, 0]` / 125.5 |

Vanilla also defines `data/variants/nebula_Standard.variant` and a `Nebula,nebula,...` row in core `ship_data.csv` (`base_bp, merc, ind` tags — it spawns all over the sector).

### 5. The screenshot geometry matches the contamination hypothesis quantitatively

If the effective spec renders the mod's 188×134 sprite but uses the vanilla `center` `[60, 99]`, then the sprite's visible middle sits **34 units starboard and 32 units aft of the logical origin** (94−60 = 34 lateral; 67−99 = −32 forward). Predicted marker positions relative to the visible sprite middle (x = right, y = up, ship facing up):

| Marker | Predicted (units) | Observed in refit screenshots |
| --- | --- | --- |
| Vanilla `WS 001` (sm. ballistic, empty) | (−63, +108) | Yellow empty square floating well above the bow, left of centerline ✔ |
| Vanilla `WS 002` (sm. ballistic, empty) | (−5, +107) | Second floating square, roughly on the centerline ✔ |
| Vanilla `WS 003` (sm. ballistic, empty) | (−71, +5) | The selected mid-left square with tooltip "Small Ballistic Turret (Empty)" ✔ |
| Mod slots (0.2.6, shifted 60 aft) | on/near hull, biased left | Turret circles sitting on the hull, biased up-left ✔ |

Measured pixel positions of the two floating squares in `Screenshot 2026-07-18 174559.png` (≈2.15 px/unit) come out at x ≈ −72 and ≈ 0 units — against predictions of −63 and −5. The **asymmetry** of the floating squares (one near centerline, one offset left) is the giveaway: the mod's slots are symmetric about the centerline in every version, so no mod-only hypothesis can produce asymmetric markers. Vanilla slots at lateral ±29, viewed through a 34-unit lateral offset, produce exactly this asymmetric pattern.

The combat screenshot (`171214`) shows the same signature from the other direction: the ship renders low-right relative to its shield/fighter rally point, i.e. the sprite is drawn 34 right / 32 down of the logical ship position.

### 6. The tooltip is the smoking gun

"Small Ballistic Turret (Empty)" appears in the refit UI. No version of the mod's `nebula.ship` — Phase 1, 2, or 3 — ever contained a ballistic slot of any size. The only source of a small ballistic slot on a ship rendering the Tress sprite is the vanilla Nebula's hull spec bleeding into the loaded ship.

## Why Phase 3 Tuning Could Never Converge

The `0.2.2`–`0.2.6` log now reads coherently:

- **`0.2.2`** (move `center` to `[125, 95]`): attacked the right *kind* of problem (origin offset) but on the wrong file — the mod's `center` appears to be overridden by the vanilla value in the collision, so editing it did little, and the change was reverted.
- **`0.2.3`** (restore exact Tress values): "no visible change" — expected, because the mod's geometry was already effectively ignored where it collided and correct where it didn't.
- **`0.2.4`** (slots −50 aft): "much closer" — the real sprite offset is 32 units aft + 34 starboard. An aft shift of ~32 would perfectly cancel the *longitudinal* component; 50 overshot slightly but looked dramatically better. The *lateral* 34-unit component and the four ghost vanilla markers remained untouched, which is why it never looked right.
- **`0.2.5`** (−75 aft): overshot further; worse.
- **`0.2.6`** (−60 aft): split the difference; inconclusive — because no purely longitudinal, symmetric adjustment can cancel a lateral offset, and nothing the mod does moves the vanilla ghost slots.

Chasing the offset with shared slot shifts was fitting a two-dimensional, half-external error with a one-dimensional, internal knob. The process decision to stop blind tuning was correct; the visual-editor plan was unnecessary.

## Secondary Damage From the Collision (worth fixing at the same time)

1. **The mod currently overwrites a vanilla ship.** The `Nebula,nebula,...` row in `Toranaga/data/hulls/ship_data.csv` replaces the vanilla civilian transport's stats sector-wide: every merc/indie/trade fleet's Nebula liner becomes a 220-OP "Superiority Destroyer" with 22,000 flux. This silently breaks vanilla content and any save using it.
2. **The description row collides too.** `Toranaga/data/strings/descriptions.csv` id `nebula`/`SHIP` overrides the vanilla Nebula transport's description.
3. **Vanilla `nebula_Standard.variant` now references a mutated hull**, which can produce refit-time oddities or log warnings.

Renaming the hull ID fixes all three automatically.

## The Fix

Rename everything to a namespaced ID and restore the proven Tress geometry. Suggested prefix: `trng_` (mirroring ScalarTech's `tahlan_` author-prefix convention).

| File | Change |
| --- | --- |
| `Toranaga/data/hulls/nebula.ship` | Rename file to `trng_nebula.ship` (avoids the same-path shadow/merge of core's `data/hulls/nebula.ship`). Set `"hullId": "trng_nebula"`. Optionally rename the sprite to `graphics/ships/trng_nebula.png` and update `spriteName`. **Revert all slot and launch-bay coordinates to the exact Tress values** (undo the 60-unit aft shift): `WS0001 [-5.5, 39]`, `WS0002 [-5.5, -39]`, `WS0003 [55.5, 60]`, `WS0004 [55.5, -60]`, `LB 1 [30, 48.5, 19.5, 42.5, 9.5, 33.5]`, `LB 2 [8, -32.5, 15.5, -39, 26.5, -45.5]`. Keep `center [94, 66.5]`, `shieldCenter [0, 0]`, `shieldRadius 125.5`, `collisionRadius 136.5`. |
| `Toranaga/data/hulls/ship_data.csv` | Change the row's `id` from `nebula` to `trng_nebula` (this also un-breaks the vanilla transport). |
| `Toranaga/data/variants/nebula_elite.variant` | Rename file to `trng_nebula_elite.variant`; set `"hullId": "trng_nebula"`, `"variantId": "trng_nebula_elite"`. |
| `Toranaga/data/strings/descriptions.csv` | Change the description id from `nebula` to `trng_nebula`. |
| `Toranaga/graphics/ships/nebula.png` | Rename to `trng_nebula.png` if `spriteName` is updated (optional but recommended for hygiene; sprite content is already correct). |
| `Toranaga/mod_info.json` | Bump version (e.g. `0.3.0` — this is a behavior-level fix, not a tweak). |

Also audit the mod for any other reference to the old IDs (`nebula`, `nebula_elite`) — e.g. `default_ship_roles.json`, faction files, or mission files if any exist — and consider whether `toranaga`/`toranaga_elite` should get the same prefix for future-proofing (no vanilla collision exists for those today).

### Expected result

With a unique hull ID and the exact Tress geometry, the ship should render centered in its shield with all four mounts and both bays sitting on the hull **on the first deploy** — the same data already does so in ScalarTech under the `tahlan_tress` ID. In-game console: `AddShip trng_nebula_elite`.

## Verification Checklist (one pass)

1. Deploy with `utilities/deploy_mod.py`; full game restart.
2. Confirm the version string in the launcher mod list reads the bumped version.
3. Refit screen: exactly 4 weapon slot markers + 2 bay markers, all on the hull; **no** floating squares; **no** "Small Ballistic Turret" tooltip anywhere.
4. Combat/sim: ship centered in its shield bubble; fighters rally on the ship, not above-left of it.
5. Spawn a vanilla Nebula transport (`AddShip nebula_Standard`) and confirm it is back to the stock civilian liner with its own sprite and stats.
6. Check `starsector-core/starsector.log` for warnings mentioning `nebula` after load.

## Lessons Recorded

- **Namespace every ID** — hulls, variants, wings, weapons, description rows, and *file paths*. Vanilla and other mods share one global namespace. ScalarTech's `tahlan_` prefix exists precisely for this reason.
- When markers misbehave **asymmetrically** or extra markers appear that the data doesn't define, suspect a spec collision/merge before suspecting coordinates.
- Before tuning coordinates against in-game observations, confirm the loaded spec is *only* yours: search the core game data for your IDs and file names first (`grep -ri "<id>" starsector-core/data/`).
