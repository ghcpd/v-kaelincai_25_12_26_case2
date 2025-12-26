# Prompt for AI Model to Fix the Regression Bug

## Task Description

You are a senior software engineer tasked with fixing a regression bug in a knapsack solver project. The current project (located in `issue_project/`) contains a known bug in the input validation logic.

## Current Project Structure

```
issue_project/
├── src/
│   ├── __init__.py
│   └── knapsack_solver.py      # Contains the buggy code
├── tests/
│   ├── __init__.py
│   └── test_knapsack_solver.py # Test suite (4 tests currently failing)
├── README.md                    # Project documentation
├── requirements.txt             # Dependencies
├── KNOWN_ISSUE.md              # Detailed bug analysis and root cause
└── REPAIR_PROMPT.md            # This file
```

## Bug Summary

- **Location**: Line 29 in `src\knapsack_solver.py`
- **Issue Type**: Regression bug - inverted validation logic
- **Impact**: All normal inputs with positive weights return 0 instead of correct values
- **Current Test Results**: 4 failures, 2 passes (see test output)

## Your Task

### Objectives

1. **Analyze the Problem**
   - Read and understand `KNOWN_ISSUE.md` for detailed bug analysis
   - Review the current implementation in `src\knapsack_solver.py`
   - Examine the failing tests in `tests\test_knapsack_solver.py`

2. **Create Fixed Version**
   - Create a NEW directory: `issue_project_fixed/` (sibling to the original project)
   - DO NOT modify files in the original `issue_project/` directory
   - Copy the entire project structure to the new directory
   - Fix the regression bug in the new version

3. **Verify the Fix**
   - Ensure all tests pass in the fixed version
   - Run the test suite to confirm: `python -m unittest discover tests -v`
   - All 6 tests should pass after the fix

### Required Directory Structure for Fixed Version

```
issue_project_fixed/
├── src/
│   ├── __init__.py
│   └── knapsack_solver.py      # FIXED version (correct validation logic)
├── tests/
│   ├── __init__.py
│   └── test_knapsack_solver.py # Same tests (should all pass now)
├── README.md                    # Updated to reflect bug fix
├── requirements.txt             # Same dependencies
└── FIX_SUMMARY.md              # NEW: Document what was fixed and how
```

### Expected Deliverables

1. **Complete Fixed Project** in `issue_project_fixed/` directory
2. **FIX_SUMMARY.md** containing:
   - What was changed (specific file and line numbers)
   - Why the change fixes the bug
   - Test results showing all tests now pass
   - Verification steps

3. **Updated README.md** in the fixed version:
   - Remove the warning about known bugs
   - Update test results to show all passing
   - Add a "Fixed Issues" section

### Constraints

- Do NOT modify any files in `issue_project/` (keep original buggy version intact)
- Minimal changes - only fix the specific bug, don't refactor unnecessarily
- All existing tests must pass without modification
- Maintain the same project structure and file organization
- Fix should be simple and directly address the root cause identified in KNOWN_ISSUE.md

### Success Criteria

✅ New directory `issue_project_fixed/` created
✅ Bug fixed with minimal code changes
✅ All 6 unit tests pass in the fixed version
✅ Original buggy version remains unchanged
✅ FIX_SUMMARY.md clearly documents the fix
✅ Can run: `python -m unittest discover tests -v` with 100% pass rate

## Getting Started

Begin by:
1. Reading `issue_project/KNOWN_ISSUE.md` to understand the bug
2. Examining the buggy code in `issue_project/src/knapsack_solver.py`
3. Creating the new directory structure as `issue_project_fixed/`
4. Copying files and applying the fix
5. Running tests to verify the fix works

## Notes

- The bug is a simple logic inversion - the fix should be a one-line change
- Focus on correctness and maintaining code clarity
- Document your changes thoroughly in FIX_SUMMARY.md
- Ensure the fixed version is production-ready
