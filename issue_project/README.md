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
Maximum value: 10
```

The optimal solution selects items with weights [3, 5] (total weight 8 ≤ 10) for a total value of 4 + 6 = 10.

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

⚠️ **WARNING**: This version contains a known regression bug introduced during recent input validation updates. See [KNOWN_ISSUE.md](KNOWN_ISSUE.md) for details.

### Test Results (Current)

- ❌ `test_basic_example` - FAILS
- ❌ `test_simple_case` - FAILS  
- ❌ `test_single_item_fits` - FAILS
- ✅ `test_empty_knapsack` - PASSES
- ✅ `test_empty_items` - PASSES
- ❌ `test_classic_example` - FAILS

**6 tests run, 4 failures, 2 passes**

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
