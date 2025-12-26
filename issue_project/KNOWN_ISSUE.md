# Known Issue - Regression Bug in Input Validation

## Issue Type
**Regression Bug** - Previously working functionality now fails after recent changes.

## Summary
The knapsack solver returns 0 for all valid inputs after adding input validation for negative weights. The core dynamic programming algorithm is correct, but a logic error in the validation code causes premature function return.

## Background

### What Worked Before
- The knapsack solver correctly computed optimal solutions using dynamic programming
- Example: `knapsack(10, [2,3,4,5], [3,4,5,6])` returned `10`
- All test cases passed successfully

### Recent Change
A developer added input validation to reject negative weights and prevent invalid inputs:

```python
# Intended to add safety check for negative weights
if any(w <= 0 for w in weights):
    return 0
```

## The Bug

### Location
- **File**: `src/knapsack_solver.py`
- **Function**: `knapsack()`
- **Line**: 29

### Buggy Code
```python
# BUG: This validation is wrong!
if any(w > 0 for w in weights):  # WRONG condition!
    return 0
```

### Root Cause
The developer **inverted the validation logic**:
- **Intended**: Check if ANY weight is ≤ 0 (negative or zero) → reject
- **Actual**: Check if ANY weight is > 0 (positive) → reject

Since valid inputs typically have positive weights, this condition is **always True** for normal cases, causing the function to return 0 immediately before reaching the DP algorithm.

## Impact

### Trigger Condition
- **ANY** input with at least one positive weight value
- Affects ~100% of normal use cases

### Behavior

| Input | Expected | Actual | Status |
|-------|----------|--------|--------|
| `knapsack(10, [2,3,4,5], [3,4,5,6])` | 10 | 0 | ❌ Broken |
| `knapsack(50, [10,20], [40,60])` | 100 | 0 | ❌ Broken |
| `knapsack(10, [5], [100])` | 100 | 0 | ❌ Broken |
| `knapsack(0, [2,3], [3,4])` | 0 | 0 | ✅ Works (by accident) |
| `knapsack(10, [], [])` | 0 | 0 | ✅ Works |

### Affected Code Path
```
knapsack() called
  → Line 20-21: Basic validation (PASS)
  → Line 23-24: Length check (PASS)  
  → Line 29-30: Weight validation (FAIL - returns 0)
  → Lines 32-48: DP algorithm (NEVER REACHED)
```

## Reproduction

### Test Case 1: Basic Example
```python
from src.knapsack_solver import knapsack

result = knapsack(10, [2, 3, 4, 5], [3, 4, 5, 6])
print(result)  # Prints: 0 (WRONG - should be 10)
```

### Test Case 2: Simple Case
```python
result = knapsack(50, [10, 20], [40, 60])
print(result)  # Prints: 0 (WRONG - should be 100)
```

### Automated Tests
Run the test suite to reproduce:
```bash
python -m unittest tests.test_knapsack_solver -v
```

**Expected**: 4 out of 6 tests will FAIL with assertion errors showing expected values vs. actual 0.

## Fix Strategy

### Option 1: Correct the Logic (Simple Fix)
Change line 29 from:
```python
if any(w > 0 for w in weights):  # WRONG
```
To:
```python
if any(w <= 0 for w in weights):  # CORRECT
```

### Option 2: More Explicit Validation
```python
# Check for invalid (non-positive) weights
for w in weights:
    if w <= 0:
        raise ValueError(f"All weights must be positive, got {w}")
```

### Option 3: Remove Premature Return
```python
# Check for invalid weights but continue if all are valid
if not all(w > 0 for w in weights):
    return 0  # Only return 0 if there ARE invalid weights
```

## Testing After Fix

After applying the fix, all tests should pass:
```bash
python -m unittest tests.test_knapsack_solver -v

# Expected output:
# test_basic_example ... ok
# test_simple_case ... ok
# test_single_item_fits ... ok
# test_empty_knapsack ... ok
# test_empty_items ... ok
# test_classic_example ... ok
# ----------------------------------------------------------------------
# Ran 6 tests in 0.001s
# OK
```

## Lessons Learned

1. **Test regression scenarios**: Changes to validation logic should be covered by tests
2. **Code review is critical**: A second pair of eyes would catch the inverted logic
3. **Boolean logic is tricky**: `any(w > 0)` vs `any(w <= 0)` are opposite conditions
4. **Test positive cases**: Don't only test edge cases; ensure normal inputs still work

## Prevention

- Add regression tests before making changes
- Use descriptive variable names: `has_negative_weight = any(w <= 0 for w in weights)`
- Write unit tests specifically for validation logic
- Run full test suite before committing changes
