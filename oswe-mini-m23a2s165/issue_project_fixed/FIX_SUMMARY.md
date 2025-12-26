# FIX SUMMARY

## What was changed
- File: `src/knapsack_solver.py`
- Change: Fixed inverted validation logic on line that checked item weights.
- Exact change (one-line):
  - From: `if any(w > 0 for w in weights):` (incorrect — rejected positive weights)
  - To:   `if any(w <= 0 for w in weights):` (correct — rejects non-positive weights)

## Why this fixes the bug
The original condition returned early for any positive weight, preventing the DP algorithm from running. The corrected condition now only rejects invalid (non-positive) weights and allows valid inputs to proceed to the dynamic programming solver.

## Test results after fix
All tests in `tests/test_knapsack_solver.py` now pass.

Command used:
```
python -m unittest discover tests -v
```

Expected / Actual:
- 6 tests run, 6 passed

## Additional test correction
- While fixing the validation bug we discovered that the `test_basic_example` and `test_basic_with_items` expectations were incorrect: the true optimal value for `capacity=10, weights=[2,3,4,5], values=[3,4,5,6]` is **13** (items with weights `[2,3,5]`), not 10. Those two assertions were updated in the fixed test suite to reflect the mathematically correct result.

## Verification steps
1. Navigate to the fixed project:
   - `cd issue_project_fixed`
2. Run the test suite:
   - `python -m unittest discover tests -v`
3. Confirm all tests show `ok`.

## Notes
- Primary fix was a single-line change to input validation. One minor test expectation was corrected to match the correct knapsack optimal result.
