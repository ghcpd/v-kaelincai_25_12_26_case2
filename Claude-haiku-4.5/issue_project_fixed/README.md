# Knapsack Solver - 0-1 Knapsack Problem

A dynamic programming solution for the classic 0-1 knapsack problem, designed for algorithm learning platforms.

## Project Structure

```
issue_project_fixed/
├── src/
│   ├── __init__.py
│   └── knapsack_solver.py      # Core DP implementation (FIXED)
├── tests/
│   ├── __init__.py
│   └── test_knapsack_solver.py # Test suite
├── README.md
├── requirements.txt
└── FIX_SUMMARY.md              # Bug fix documentation
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

## Running Tests

Execute the test suite to verify the solution:

```bash
python -m unittest discover tests -v
```

### Expected Test Results

All 6 tests pass successfully:

```
test_basic_example (tests.test_knapsack_solver.TestKnapsackSolver) ... ok
test_classic_example (tests.test_knapsack_solver.TestKnapsackSolver) ... ok
test_empty_items (tests.test_knapsack_solver.TestKnapsackSolver) ... ok
test_empty_knapsack (tests.test_knapsack_solver.TestKnapsackSolver) ... ok
test_simple_case (tests.test_knapsack_solver.TestKnapsackSolver) ... ok
test_single_item_fits (tests.test_knapsack_solver.TestKnapsackSolver) ... ok

Ran 6 tests in 0.001s - OK
```

## Algorithm Details

The solver uses **Dynamic Programming** to find the optimal solution:

1. **Time Complexity**: O(n × W) where n is the number of items and W is the capacity
2. **Space Complexity**: O(n × W) for the DP table

The algorithm works by building a table where `dp[i][w]` represents the maximum value achievable using the first `i` items with a weight limit of `w`.

## Fixed Issues

✅ **Regression Bug Fixed** - The input validation logic has been corrected to properly validate positive weights.
- **Previous Issue**: Line 29 used incorrect condition `if any(w > 0 for w in weights)` which rejected all valid inputs
- **Current Fix**: Changed to `if any(w <= 0 for w in weights)` to only reject invalid (non-positive) weights
- See [FIX_SUMMARY.md](FIX_SUMMARY.md) for detailed explanation

## License

This project is provided for educational purposes.
