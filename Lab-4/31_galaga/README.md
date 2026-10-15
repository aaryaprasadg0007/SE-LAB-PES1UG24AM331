# Lab 4 - VibeCoding: Galaga Repair

**Student:** Aarya Prasad G  
**SRN:** PES1UG24AM331  
**Assigned game:** [SETAPESU26/31_galaga](https://github.com/SETAPESU26/31_galaga)  
**Personal lab repository:** [SE-LAB-PES1UG24AM331](https://github.com/aaryaprasadg0007/SE-LAB-PES1UG24AM331)

## Tasks completed in code

1. **Corrected cubic Bezier paths.** Both coordinate equations now use the standard term `3 * u * t ** 2 * p2`, with `u = 1 - t`.
2. **Wave-aware enemy tint.** Wave 1 keeps the supplied palette; later waves cycle through distinct RGB palettes.
3. **Timed wave banner.** `on_wave_start(wave)` stores the wave number and displays a `WAVE n` banner for 1.5 seconds.
4. **Shield charges.** `shield_charges(wave)` grants one hit of shield protection on waves 3, 6, 9, etc.

Each requested code task has a separate commit in the Lab-4 folder history. No pull request was opened against the upstream course repository.

## Setup

Requires Python 3.10+ and Pygame.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python game.py
```

Controls: Left/Right arrow keys move, Space fires, and R resets.

Run the logic tests with:

```bash
python -m unittest discover -s tests -v
```

## Submission evidence

- `prompts/LLM_INTERACTION_LOG.md` and `docs/LLM_Prompt_History.pdf` are a prepared prompt/implementation log, **not** a verbatim platform export.
- `evidence/baseline_game.py` retains the original upstream source for reproducing the bug.
- The two MP4s in the downloadable package's `previews/` folder are clearly watermarked generated previews, not screen recordings; they do not replace the course's requested before/after 10-second screen captures.
- Record the real before and after gameplay on your Mac, then add them as `evidence/before/before.mp4` and `evidence/after/after.mp4`.
- Add the real exported ChatGPT history or a valid share link if your instructor requires the actual conversation export.

See [the course handout](https://github.com/aaryaprasadg0007/SE-LAB-PES1UG24AM331) for the parent lab repository and submission organization.
