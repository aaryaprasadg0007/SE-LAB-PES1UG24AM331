# Lab 5 Issue Log

**Student:** Aarya Prasad G  
**SRN:** PES1UG24AM331  
**Source:** [`before/address_book.py`](before/address_book.py), captured from [the assigned repository](https://github.com/SETAPESU26/L5_27_address_book).

The line numbers below refer to the original source before fixes. Severity labels are a manual code-review prioritization, not reported scores from an executed scanner.

| # | Priority | Tool/category | Original line(s) | Issue found | Fix applied |
|---:|---|---|---:|---|---|
| 1 | High | Bandit / unsafe deserialization | 3, 60–67 | `pickle.load()` can execute attacker-controlled code when a backup file is untrusted. | Replaced pickle serialization/deserialization with JSON. Loaded JSON is validated before it is returned. |
| 2 | Medium | Bandit / weak hash | 18–19 | MD5 is used to generate contact identifiers. It is not appropriate when collision resistance is expected. | Replaced MD5 with the full SHA-256 digest. The identifier is not used as an authentication token. |
| 3 | Medium | Error handling / Pylint | 30–36 | `except Exception` hides unrelated programming and runtime errors. | Check for a missing contact explicitly with `dict.get()` and return `False` only for the expected missing-contact case. |
| 4 | Low | Hard-coded secret / Bandit | 6 | An unused hard-coded `SYNC_PASSWORD` value is present in source. | Removed the unused embedded password constant. No password or secret is required by the demonstrated program. |
| 5 | Medium | Maintainability / Pylint | 10, 18, 22, 30, 39, 47, 53, 60, 65, 70 | Function names use camelCase rather than conventional Python `snake_case`; functions lack descriptions and type annotations. | Applied `snake_case`, added docstrings and type annotations, and kept the function responsibilities separate. |
| 6 | Low | File handling / portability | 53–67 | File reads and writes do not set an explicit text encoding. | CSV and JSON files now use UTF-8 explicitly and use `pathlib.Path` context-managed file operations. |
| 7 | Low | Runtime behavior / import side effects | 88 | `main()` is called unconditionally when the module is imported, which prevents safe reuse and unit testing. | Added the `if __name__ == "__main__":` guard. Running the script still executes the original demonstration. |
| 8 | Low | Flake8 / formatting | 23, 46, 84 and multiple function definitions | Spacing, blank lines, naming, and a long line are inconsistent with standard Python style. | Applied consistent formatting, conventional naming, line wrapping, and standard imports. |

## Verification

Eleven unit tests cover phone validation, case-insensitive name search, phone substring search, missing-contact updates, city grouping, identifier stability, JSON backup/restore, malformed JSON, unexpected backup structure, invalid phone data inside a backup, and CSV export. See `evidence/unit_test_output.txt`.

The original and corrected demo outputs are captured in `evidence/`. The analysis report files are clearly marked as not run because the tools were unavailable here; `run_static_analysis.sh` is included to create genuine report output instead of presenting guessed output as tool results.
