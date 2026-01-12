# Knapsack Solver - 0-1 Knapsack Problem

A dynamic programming solution for the classic 0-1 knapsack problem, designed for algorithm learning platforms.

## Project Structure

```
issue_project/
├── src/
│   ├── __init__.py
│   └── knapsack_solver.py      # Core DP implementation
├── tests/
│   ├── __init__.py
│   └── test_knapsack_solver.py # Test suite
├── README.md
├── requirements.txt
└── KNOWN_ISSUE.md              # Bug documentation
```

## Problem Description

Given a knapsack with maximum weight capacity and a set of items with weights and values, determine the maximum total value that can be obtained by selecting items without exceeding the capacity constraint. Each item can be selected at most once (0-1 knapsack).

## Installation

```bash
# Install dependencies (if any)
pip install -r requirements.txt
```

## Usage

### As a Module

```python
from src.knapsack_solver import knapsack

# Define problem
capacity = 10
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]

# Solve
max_value = knapsack(capacity, weights, values)
print(f"Maximum value: {max_value}")
```

### Expected Output
```
Maximum value: 13
```

The optimal solution selects items with weights [2, 3, 5] (total weight 10 ≤ 10) for a total value of 3 + 4 + 6 = 13.

## Running Tests

Execute the test suite to verify functionality:

```bash
python -m pytest tests/ -v
```

Or using unittest:

```bash
python -m unittest discover tests -v
```

## Current Status

✅ **All tests passing** - Regression bug has been fixed.

### Test Results

- ✅ `test_basic_example` - PASSES
- ✅ `test_simple_case` - PASSES  
- ✅ `test_single_item_fits` - PASSES
- ✅ `test_empty_knapsack` - PASSES
- ✅ `test_empty_items` - PASSES
- ✅ `test_classic_example` - PASSES
- ✅ `test_basic_with_items` - PASSES

**7 tests run, 0 failures, 7 passes**

## Fixed Issues

### Regression Bug Fix (v1.1)

**Issue**: Input validation logic was inverted, causing all valid inputs to return 0.

**Root Cause**: The condition `if any(w > 0 for w in weights): return 0` incorrectly rejected positive weights instead of checking for negative weights.

**Fix**: Changed to `if any(w <= 0 for w in weights): return 0` to properly reject non-positive weights.

**Impact**: All normal use cases now work correctly, returning optimal knapsack values instead of 0.

**Files Changed**: `src/knapsack_solver.py` (line 32)

## Features

- Dynamic programming implementation with O(n×W) time complexity
- Input validation for edge cases
- Comprehensive test coverage
- Clean, readable code structure

## Algorithm Complexity

- **Time Complexity**: O(n × W) where n is the number of items and W is the capacity
- **Space Complexity**: O(n × W) for the DP table

## Contributing

This is a demonstration project for educational purposes showcasing regression bug detection and testing practices.
