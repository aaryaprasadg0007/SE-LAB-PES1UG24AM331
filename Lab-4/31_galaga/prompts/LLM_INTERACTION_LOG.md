# Lab 4 VibeCoding - Prompt and Implementation Log

**Student:** Aarya Prasad G  
**SRN:** PES1UG24AM331  
**Game:** `SETAPESU26/31_galaga`

> This is a prepared work log of prompts and implementation decisions, not a verbatim ChatGPT export. Attach the actual platform export or share link separately if required.

## Task 1 - Correct the cubic Bezier formula

**Prompt:** Inspect `bezier()` against the standard cubic Bezier formula. Find the incorrect middle term and make the smallest correction while preserving the endpoints.

**Decision:** The standard coefficients are `u**3`, `3*u**2*t`, `3*u*t**2`, and `t**3`, where `u = 1 - t`. The original third term missed `t**2`; both x and y equations were corrected.

**Validation:** Tests check the two endpoints and the midpoint weight.

## Task 2 - Implement enemy tinting

**Prompt:** Implement `enemy_tint(kind)` with distinct palettes for later waves while preserving the default palette on wave 1 and a safe fallback for unknown types.

**Decision:** Wave 1 returns `None`; later waves cycle through three explicitly defined RGB palettes.

**Validation:** Tests cover default colors, wave 2, and unknown kinds.

## Task 3 - Implement a wave-start banner

**Prompt:** Make `on_wave_start(wave)` show a short `WAVE n` banner each time enemies spawn, without changing the spawn flow.

**Decision:** The function records the active wave, banner label, and a 1.5-second timer. The update and draw methods decrement and render it.

**Validation:** Test checks wave number, label, and timer.

## Task 4 - Implement shield charges

**Prompt:** Grant one shield hit on waves 3, 6, 9, and so on; disable it for other waves and keep the existing hit logic.

**Decision:** Return 1 for positive wave numbers divisible by 3, otherwise 0.

**Validation:** Test checks waves 1-9.

## Final verification

**Prompt:** Review the README tasks, add focused unit tests, run the tests and syntax compilation, and list any evidence that still needs a real user capture.

**Result:** Five unit tests pass in the prepared local project and Python source compiles. A live Pygame run and genuine before/after 10-second recordings must be completed on the target machine. The provided PDF is a work log, not the platform's literal exported chat history.
