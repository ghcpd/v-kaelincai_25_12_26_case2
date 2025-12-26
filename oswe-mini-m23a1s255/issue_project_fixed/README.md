# Knapsack Solver — Fixed Version

This repository is a fixed copy of the original `issue_project` where an input-validation regression caused valid inputs to be rejected.

## What changed
- Fixed an inverted validation in `src/knapsack_solver.py` that returned early for positive weights.
- Minimal, targeted change — algorithm and tests otherwise unchanged.

## Fixed Issues
- Regression: input validation returned 0 for any positive-weight inputs
- File: `src/knapsack_solver.py` — corrected validation condition for non-positive weights

## Test status (verified)
- All unit tests now pass.

## Running tests
```bash
python -m unittest discover tests -v
```

## Notes
- This directory is a safe, fixed copy of the original project for verification and regression testing.
