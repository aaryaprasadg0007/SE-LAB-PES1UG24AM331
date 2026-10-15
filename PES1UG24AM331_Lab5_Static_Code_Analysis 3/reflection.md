# Lab 5 Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without running the program. It helps detect likely defects, unsafe patterns, and style problems early, before they reach users. It is most useful when its findings are reviewed and the fixed program is also tested.

## 2. What are the different roles of Pylint, Bandit, and Flake8?

Pylint checks code quality, naming, design choices, and likely programming errors. Bandit looks for common security risks in Python code, including unsafe deserialization. Flake8 checks style and formatting rules such as whitespace, unused imports, and line length. The tools overlap in places but have different priorities.

## 3. Which issue was most important in this program, and how was it fixed?

The unsafe use of `pickle.load()` was the most serious finding because loading a malicious pickle can execute code. The backup and restore functions now use JSON, which does not deserialize arbitrary Python objects, and the decoded data is validated before it is accepted. MD5 was also replaced with SHA-256 for the demo's short contact identifier.

## 4. How can static analysis improve maintainability without changing intended behavior?

Small functions, clear names, narrow exception handling, explicit file encodings, and consistent formatting make the code easier to understand and extend. Unit tests then check that the address book still validates numbers, searches contacts, updates cities, exports CSV, and restores a backup after the cleanup.

## Verification note

These responses address the objectives and reflection deliverable in the supplied lab handout. The provided PDF lists the reflection deliverable but does not display a separate verbatim list of four reflection prompts.
