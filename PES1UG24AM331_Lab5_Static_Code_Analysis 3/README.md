# Lab 5: Static Code Analysis — Contact & Address Book Manager

**Student:** Aarya Prasad G  
**SRN:** PES1UG24AM331  
**Assigned repository:** https://github.com/SETAPESU26/L5_27_address_book

## What is included

- `address_book.py`: corrected address-book implementation, based on the assigned source.
- `before/address_book.py`: original source captured from the assigned repository for before/after comparison.
- `issues.md`: issue table tied to the actual original file and corresponding fixes.
- `reflection.md`: reflection answers aligned with the objectives in the supplied lab handout.
- `tests/test_address_book.py`: ten unit tests.
- `reports/before/` and `reports/after/`: reserved output paths for Pylint, Bandit, and Flake8.
- `run_static_analysis.sh`: runs all three tools against both versions and writes the actual reports.
- `evidence/`: recorded program output, test output, and environment/tool availability notes.

## Run the program

Requires Python 3.10 or newer; the program itself uses only the standard library.

```bash
python3 address_book.py
```

It prints the demonstration, exports `contacts.csv`, and writes a JSON-formatted backup to `contacts.bak` in the current working directory. The old version used Python pickle for the backup; the new version intentionally uses JSON, so an old pickle-format `.bak` must be recreated with the corrected program rather than loaded.

## Run the tests

From this folder:

```bash
python3 -m unittest discover -s tests -v
```

## Run the required static-analysis tools

Install Pylint, Bandit, and Flake8 into the active Python environment, then run:

```bash
python3 -m pip install pylint bandit flake8
./run_static_analysis.sh
```

The script creates six actual report files: one report from each tool for the original source and the corrected source. It also writes the exit status of each run. The files currently in the `reports/` folders explicitly state that these tools could not be executed in the build environment because they were not installed and package-index DNS access failed. They are not fabricated tool outputs or invented Pylint scores.

## Important verification status

The original source was retrieved from the assigned repository. The corrected program ran successfully, passed its ten unit tests, and compiled with Python. Pylint/Bandit/Flake8 command reports could not be generated inside this environment; use `run_static_analysis.sh` on a machine where the tools are installed to obtain real outputs and verify the Pylint target above 9.5.
