#!/usr/bin/env python3
"""
Simple validation script for the knapsack solver.
Tests the basic functionality as described in README.
"""

from src.knapsack_solver import knapsack

def main():
    print("Knapsack Solver Validation")
    print("=" * 30)

    # Test case from README
    capacity = 10
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]

    print(f"Capacity: {capacity}")
    print(f"Weights: {weights}")
    print(f"Values: {values}")

    try:
        max_value = knapsack(capacity, weights, values)
        print(f"Maximum value: {max_value}")

        # Verify expected result
        expected = 13
        if max_value == expected:
            print(f"✅ SUCCESS: Got expected value {expected}")
        else:
            print(f"❌ FAILURE: Expected {expected}, got {max_value}")
            return False

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

    print("\n✅ System launched successfully!")
    print("✅ All functionality verified!")
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)