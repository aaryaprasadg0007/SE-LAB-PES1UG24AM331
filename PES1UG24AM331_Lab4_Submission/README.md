# Software Engineering Lab 4 - VibeCoding

**Student:** Aarya Prasad G  
**SRN:** PES1UG24AM331  
**Game repository used:** [`SETAPESU26/31_galaga`](https://github.com/SETAPESU26/31_galaga)  
**Personal lab repository:** [`aaryaprasadg0007/SE-LAB-PES1UG24AM331`](https://github.com/aaryaprasadg0007/SE-LAB-PES1UG24AM331)

## What this submission changes

This project starts from the Galaga-lite Pygame game and addresses all four tasks listed in its upstream README.

1. **Cubic Bézier path fix.** The third term now uses `3 * u * t ** 2 * p2`; the previous term omitted the second power of `t`, distorting the middle of enemy entry and dive paths.
2. **Wave-aware enemy tint.** `enemy_tint(kind)` keeps the original colors on wave 1 and cycles through distinct palettes on later waves. Unknown enemy kinds safely fall back to the game's default colors.
3. **Wave-start banner.** `on_wave_start(wave)` records the current wave and starts a 1.5-second `WAVE n` banner. The game update loop counts the banner down, and the draw method renders it near the top of the playfield.
4. **Shield charges.** `shield_charges(wave)` grants one damage-absorbing shield charge on waves 3, 6, 9, and so on, and zero on other waves. Existing `hit_player()` shield handling consumes the charge.

## Setup and run

Requires Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python game.py
```

**Controls:** Left/Right arrows move the player, Space fires, and `R` resets the game.

Run the focused regression tests:

```bash
python -m unittest discover -s tests -v
```

The tests cover the Bézier endpoints and midpoint weighting, wave palette selection, banner state, and the shield schedule. They can run without a display; interactive play still requires Pygame.

## Gameplay videos

The `videos/` folder contains `before_gameplay_demo.mp4` and `after_gameplay_demo.mp4`, each 10 seconds long. These were rendered deterministically from Python gameplay logic using ordinary drawing and video-encoding code; no AI image/video generation model was used. They show the original and corrected Bézier behavior in the game playfield, without a fabricated Mac desktop frame. They are programmatic gameplay demonstrations, not screen recordings captured from a running Pygame window. The course specifically asks for genuine recordings, so do not describe these demos as macOS screen captures.

## AI interaction record

`prompts/LLM_INTERACTION_LOG.md` and `docs/LLM_Prompt_History.pdf` record the focused prompts, decisions, and validation performed while completing the tasks. This is a prepared work log, not a verbatim ChatGPT platform export. The lab handout asks for exported chat history and the upstream README asks for a chat/LLM page link, so attach the actual exported conversation or add the share link before final submission.

## Submission checklist

- [x] Updated Python source.
- [x] README and dependency declaration.
- [x] Separate tests for all four task areas.
- [x] Prompt/implementation log in Markdown and PDF.
- [x] Baseline source retained to make the original defect reproducible.
- [x] Include 10-second before and after programmatic gameplay demonstrations in `videos/`.
- [ ] Add genuine before/after screen recordings if strict screen-capture evidence is required.
- [ ] Add the actual full chat export or ChatGPT share link requested by the course.
- [x] Assigned game confirmed as `31_galaga`.

## Source and assignment note

The assigned game is `31_galaga`. The original baseline is retained under `evidence/baseline_game.py` so the faulty curve can be reproduced locally.
