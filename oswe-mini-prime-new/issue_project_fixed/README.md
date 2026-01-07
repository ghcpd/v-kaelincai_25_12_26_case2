# Knapsack Solver - 0-1 Knapsack Problem

A dynamic programming solution for the classic 0-1 knapsack problem, designed for algorithm learning platforms.

## Project Structure

```
issue_project_fixed/
├── src/
│   ├── __init__.py
│   └── knapsack_solver.py      # Core DP implementation (fixed)
├── tests/
│   ├── __init__.py
│   └── test_knapsack_solver.py # Test suite
├── README.md
├── requirements.txt
└── FIX_SUMMARY.md              # Fix documentation
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
Maximum value: 10
```

The optimal solution selects items with weights [3, 5] (total weight 8 ≤ 10) for a total value of 4 + 6 = 10.

## Running Tests

Execute the test suite to verify functionality:

```bash
python -m unittest discover tests -v
```

## Current Status

✅ **All tests pass** in this fixed version.

### Test Results (Fixed)

- ✅ `test_basic_example` - PASS
- ✅ `test_simple_case` - PASS
- ✅ `test_single_item_fits` - PASS
- ✅ `test_empty_knapsack` - PASS
- ✅ `test_empty_items` - PASS
- ✅ `test_classic_example` - PASS

**6 tests run, 0 failures, 0 errors**

## Fixed Issues

- Corrected input validation logic that previously rejected valid positive weights (regression bug). See `FIX_SUMMARY.md` for details.

## Features

- Dynamic programming implementation with O(n×W) time complexity
- Input validation for edge cases
- Comprehensive test coverage
- Clean, readable code structure

## Algorithm Complexity

- **Time Complexity**: O(n × W) where n is the number of items and W is the capacity
- **Space Complexity**: O(n × W) for the DP table

## Contributing

This project is a demonstration of how a minimal, targeted fix can address a regression bug while keeping the codebase simple and maintainable.
