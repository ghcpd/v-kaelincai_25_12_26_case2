#!/usr/bin/env python3
"""
Edge case validation for the knapsack solver.
"""

from src.knapsack_solver import knapsack

def test_edge_cases():
    print("Edge Case Validation")
    print("=" * 20)

    test_cases = [
        # (capacity, weights, values, expected, description)
        (0, [1, 2], [10, 20], 0, "Zero capacity"),
        (10, [], [], 0, "Empty items"),
        (10, [5], [100], 100, "Single item"),
        (10, [2, 3, 4], [3, 4, 5], 12, "Multiple items"),
        (50, [10, 20, 30], [60, 100, 120], 220, "Classic example"),
    ]

    all_passed = True

    for capacity, weights, values, expected, desc in test_cases:
        try:
            result = knapsack(capacity, weights, values)
            if result == expected:
                print(f"✅ {desc}: {result}")
            else:
                print(f"❌ {desc}: Expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            print(f"❌ {desc}: ERROR - {e}")
            all_passed = False

    return all_passed

if __name__ == "__main__":
    success = test_edge_cases()
    print(f"\n{'✅ All edge cases passed!' if success else '❌ Some edge cases failed!'}")
    exit(0 if success else 1)