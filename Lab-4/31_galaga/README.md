# Software Engineering Lab 4 - VibeCoding

**Student:** Aarya Prasad G  
**SRN:** PES1UG24AM331  
**Assigned game:** [SETAPESU26/31_galaga](https://github.com/SETAPESU26/31_galaga)  
**Personal lab repository:** [SE-LAB-PES1UG24AM331](https://github.com/aaryaprasadg0007/SE-LAB-PES1UG24AM331)

## What changed

The four code tasks listed in the assigned repository's README are implemented:

1. **Cubic Bézier path correction:** fixed the third weighted term from `3 * u * t * p2` to `3 * u * t ** 2 * p2` for both x and y.
2. **Wave-aware enemy colors:** wave 1 uses the original palette; later waves cycle through three RGB palettes.
3. **Wave-start banner:** `on_wave_start(wave)` displays a `WAVE n` banner for 1.5 seconds.
4. **Shield charges:** `shield_charges(wave)` grants one hit of protection on waves 3, 6, 9, and so on.

## Run the game

Requires Python 3.10+ and Pygame.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python game.py
```

Controls: Left/Right arrows move, Space fires, and R resets.

Run the regression tests:

```bash
python -m unittest discover -s tests -v
```

The focused tests cover Bézier endpoints and midpoint weighting, wave palettes, banner state, and shield scheduling. Five unit tests passed, and Python syntax compilation passed in the preparation environment. A live gameplay check still requires Pygame to be installed.

## Recording files and submission status

The folder `previews/` contains two 10-second MP4 **generated visual previews**:
- `before_bug_preview_NOT_SCREEN_RECORDING.mp4`
- `after_features_preview_NOT_SCREEN_RECORDING.mp4`

They are visibly labelled as generated previews. They are not captured from a live game window and must not be submitted as the required screen-recording evidence.

To create the real recordings on your Mac:
1. Install Pygame with `python -m pip install -r requirements.txt`.
2. Record the original behavior by running `python evidence/baseline_game.py`; use QuickTime Player's **File > New Screen Recording** or **Command-Shift-5**. Save a genuine 10-second capture as `evidence/before/before.mp4`.
3. Run `python game.py` and capture the corrected behavior for 10 seconds; save it as `evidence/after/after.mp4`.
4. Add the actual ChatGPT conversation export or a valid share link if the instructor asks for the full chat export.

## AI prompt log

- `prompts/LLM_INTERACTION_LOG.md` contains the focused prompts and implementation notes.
- `docs/LLM_Prompt_History.pdf` is a prepared summary log, **not** a verbatim export of the ChatGPT interface.

## Checklist

- [x] Updated Python game source for all four tasks.
- [x] Four task-specific Git commits in the personal GitHub Lab-4 folder.
- [x] Regression tests and requirements file.
- [x] Original baseline source retained for reproducing the bug.
- [x] Markdown prompt log and PDF summary.
- [x] Watermarked 10-second visual previews.
- [ ] Genuine 10-second before and after screen recordings.
- [ ] Actual full platform chat history export or share link, if required.
