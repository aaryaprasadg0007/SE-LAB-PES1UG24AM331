# Lab 4 VibeCoding - prompt and implementation log

**Student:** Aarya Prasad G  
**SRN:** PES1UG24AM331  
**Repository under review:** `SETAPESU26/31_galaga`  
**Purpose:** Record the prompts and checks used to work through the four README tasks.

> This is a concise work log prepared from the implementation process, not a literal export of the ChatGPT conversation. The course's requested platform export/share link still needs to be attached separately.

## Step 1 - Fix the cubic Bézier curve

**Prompt used:**

> Inspect the `bezier()` function against the standard cubic Bézier formula. Identify the incorrect middle term and make the smallest fix so the curve still starts at `p0`, ends at `p3`, and follows the two control points correctly. Explain the change.

**Implementation decision:** The standard formula is `u³p0 + 3u²tp1 + 3ut²p2 + t³p3`, where `u = 1 - t`. The original code used `3 * u * t * p2` and omitted the second power of `t`. Both x and y coordinates now use `3 * u * t ** 2 * p2`.

**Check:** Added tests for the curve's endpoints and expected midpoint value. Both pass.

## Step 2 - Implement enemy tinting

**Prompt used:**

> Implement `enemy_tint(kind)` so waves after wave 1 use visibly different enemy color palettes. The function receives `boss`, `red`, or `blue`, and should return an RGB tuple or `None` when the original color should be used. Keep the rendering fallback safe.

**Implementation decision:** Wave 1 returns `None` to preserve original colors; later waves cycle between three explicit palettes. Unknown kinds return `None`.

**Check:** Test verifies default wave-1 behavior, a known wave-2 tint, and safe fallback for an unknown kind.

## Step 3 - Add a wave-start banner

**Prompt used:**

> Implement `on_wave_start(wave)` to show a short `WAVE n` banner each time a wave starts. The hook is called by `spawn_wave()`, so keep the signature and existing spawn flow unchanged. Make the banner appear for a limited time rather than remaining on screen forever.

**Implementation decision:** The hook updates the current-wave state, banner label, and a 1.5-second timer. `Game.update()` decrements the timer and `Game.draw()` renders the banner while time remains.

**Check:** Test verifies the selected wave, label text, and timer initialization.

## Step 4 - Add shield charges

**Prompt used:**

> Implement `shield_charges(wave)` with one shield hit on every third wave (3, 6, 9, ...), and zero on other waves. Keep the existing `hit_player()` shield consumption logic unchanged.

**Implementation decision:** Return `1` when the wave is positive and divisible by 3; otherwise return `0`.

**Check:** Test verifies the expected values for waves 1 through 9.

## Final verification prompt

**Prompt used:**

> Review the four requested tasks against the README, add focused unit tests for the logic, run the tests and Python syntax compilation, and list anything that still needs human evidence rather than fabricating it.

**Result:** Five unit tests passed and all three Python files compiled. The two 10-second videos and an actual exported/shareable platform chat history remain manual evidence requirements.

## What I learned / review notes

- Small exponent errors can preserve curve endpoints while distorting the path between them, so a midpoint test is necessary in addition to endpoint tests.
- Optional hooks are easier to review when their inputs and return values stay consistent with the provided game code.
- Visual features such as color changes and banners must be checked during live gameplay as well as with unit tests.
- The AI output was reviewed against the assignment README and covered with focused tests; the game should still be played locally before final submission.
