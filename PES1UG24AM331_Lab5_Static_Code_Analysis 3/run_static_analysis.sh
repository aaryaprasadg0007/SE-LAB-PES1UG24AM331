#!/usr/bin/env bash
# Run the required tools on the assigned baseline and corrected implementation.
set -u
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"
STATUS_FILE="$ROOT/evidence/tool_run_status.txt"
: > "$STATUS_FILE"

run_tool() {
    local tool="$1"
    local target="$2"
    local report="$3"
    local label="$4"
    local status=0

    if ! command -v "$tool" >/dev/null 2>&1; then
        printf 'NOT RUN: %s is not installed or not on PATH.\n' "$tool" > "$report"
        printf '%s: NOT RUN (tool unavailable)\n' "$label" >> "$STATUS_FILE"
        return 0
    fi

    case "$tool" in
        pylint) pylint "$target" > "$report" 2>&1 || status=$? ;;
        bandit) bandit -r "$target" > "$report" 2>&1 || status=$? ;;
        flake8) flake8 "$target" > "$report" 2>&1 || status=$? ;;
    esac
    printf '%s: exit status %s\n' "$label" "$status" >> "$STATUS_FILE"
}

for tool in pylint bandit flake8; do
    run_tool "$tool" "$ROOT/before/address_book.py" \
        "$ROOT/reports/before/${tool}_report.txt" "before/$tool"
    run_tool "$tool" "$ROOT/address_book.py" \
        "$ROOT/reports/after/${tool}_report.txt" "after/$tool"
done

printf 'Python: ' >> "$STATUS_FILE"
"$PYTHON" --version >> "$STATUS_FILE" 2>&1 || true
printf '\nReport generation completed. Review reports and statuses in the reports/ and evidence/ folders.\n'
