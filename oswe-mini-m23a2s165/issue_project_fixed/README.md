# Knapsack Solver - 0-1 Knapsack Problem (Fixed)

This is the fixed version of the knapsack solver where the regression in input validation has been corrected.

## Changes
- Fixed input validation that incorrectly rejected valid positive weights.
- All unit tests now pass.

## Test Results (Fixed)
- ✅ `test_basic_example` - PASS
- ✅ `test_simple_case` - PASS
- ✅ `test_single_item_fits` - PASS
- ✅ `test_empty_knapsack` - PASS
- ✅ `test_empty_items` - PASS
- ✅ `test_classic_example` - PASS

**6 tests run, 6 passed**

## Fixed Issues
- Corrected inverted validation in `src/knapsack_solver.py` that wrongly returned 0 for normal inputs.

## Running Tests
```bash
python -m unittest discover tests -v
```
