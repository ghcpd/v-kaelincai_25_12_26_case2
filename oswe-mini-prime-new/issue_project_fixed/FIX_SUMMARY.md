# FIX_SUMMARY

## Summary
A regression bug in `src/knapsack_solver.py` caused the `knapsack()` function to return 0 for valid inputs due to an inverted validation condition. This fix corrects that condition and restores expected behavior.

## What was changed
- File: `src/knapsack_solver.py`
  - Line (~29): Changed validation condition from:
    ```python
    if any(w > 0 for w in weights):  # WRONG
        return 0
    ```
    to:
    ```python
    if any(w <= 0 for w in weights):  # CORRECT
        return 0
    ```
  - This is a one-line fix that corrects the input validation logic for weights.

## Why this fixes the bug
The original condition rejected cases where any weight was positive (which is most valid inputs). The corrected condition rejects only non-positive weights (0 or negative), which matches the intended validation.

## Test results (after fix)
Ran:
```
python -m unittest discover tests -v
```
Output summary:
```
Ran 6 tests in 0.001s

OK
```
All tests pass.

## Verification steps
1. Navigate to the fixed project:
   ```bash
   cd oswe-mini-prime-new/issue_project_fixed
   ```
2. Run the test suite:
   ```bash
   python -m unittest discover tests -v
   ```
3. Observe that all 6 tests pass.

## Notes
- Minimal, targeted change applied as required by the repair prompt.
- The original project in `issue_project/` was left unchanged.
