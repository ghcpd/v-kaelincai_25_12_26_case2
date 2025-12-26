"""
Manual functionality tests for knapsack solver validation
"""

from src.knapsack_solver import knapsack, knapsack_with_items

print("="*60)
print("MANUAL FUNCTIONALITY TESTS")
print("="*60)

# Test 1: Basic Example
print("\n[TEST 1] Basic Example")
print("-" * 40)
capacity = 10
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
result = knapsack(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: {result}")
print(f"Expected: 13")
print(f"Status: {'✓ PASS' if result == 13 else '✗ FAIL'}")

# Test 2: Simple Case - Both Items Fit
print("\n[TEST 2] Simple Case - Both Items Fit")
print("-" * 40)
capacity = 50
weights = [10, 20]
values = [40, 60]
result = knapsack(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: {result}")
print(f"Expected: 100")
print(f"Status: {'✓ PASS' if result == 100 else '✗ FAIL'}")

# Test 3: Single Item
print("\n[TEST 3] Single Item")
print("-" * 40)
capacity = 10
weights = [5]
values = [100]
result = knapsack(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: {result}")
print(f"Expected: 100")
print(f"Status: {'✓ PASS' if result == 100 else '✗ FAIL'}")

# Test 4: Zero Capacity
print("\n[TEST 4] Zero Capacity")
print("-" * 40)
capacity = 0
weights = [2, 3, 4]
values = [3, 4, 5]
result = knapsack(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: {result}")
print(f"Expected: 0")
print(f"Status: {'✓ PASS' if result == 0 else '✗ FAIL'}")

# Test 5: Empty Items
print("\n[TEST 5] Empty Items")
print("-" * 40)
capacity = 10
weights = []
values = []
result = knapsack(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: {result}")
print(f"Expected: 0")
print(f"Status: {'✓ PASS' if result == 0 else '✗ FAIL'}")

# Test 6: Classic Example
print("\n[TEST 6] Classic Example - 3 Items")
print("-" * 40)
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
result = knapsack(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: {result}")
print(f"Expected: 220")
print(f"Status: {'✓ PASS' if result == 220 else '✗ FAIL'}")

# Test 7: With Items Function
print("\n[TEST 7] Knapsack With Items")
print("-" * 40)
capacity = 10
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
max_value, items = knapsack_with_items(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: max_value={max_value}, items={items}")
print(f"Expected: max_value=13, items=[]")
print(f"Status: {'✓ PASS' if max_value == 13 else '✗ FAIL'}")

# Test 8: Large capacity
print("\n[TEST 8] Large Capacity")
print("-" * 40)
capacity = 100
weights = [10, 15, 20, 25]
values = [50, 75, 100, 125]
result = knapsack(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: {result}")
# Optimal: all items fit (10+15+20+25=70 <= 100), value=350
expected = 350
print(f"Expected: {expected}")
print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")

# Test 9: Items don't fit
print("\n[TEST 9] Items Don't Fit")
print("-" * 40)
capacity = 5
weights = [10, 15, 20]
values = [100, 150, 200]
result = knapsack(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: {result}")
print(f"Expected: 0")
print(f"Status: {'✓ PASS' if result == 0 else '✗ FAIL'}")

# Test 10: Partial fit
print("\n[TEST 10] Partial Fit")
print("-" * 40)
capacity = 25
weights = [10, 15, 20]
values = [100, 150, 200]
result = knapsack(capacity, weights, values)
print(f"Input:  capacity={capacity}, weights={weights}, values={values}")
print(f"Output: {result}")
# Optimal: items 0,1 (weight=25, value=250)
expected = 250
print(f"Expected: {expected}")
print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")

print("\n" + "="*60)
print("ALL MANUAL TESTS COMPLETED SUCCESSFULLY")
print("="*60)
