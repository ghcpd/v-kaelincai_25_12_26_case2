"""
Unit tests for knapsack solver

These tests expose a regression bug introduced during input validation updates.
"""

import unittest
import sys
import os

# Add parent directory to path to import src module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.knapsack_solver import knapsack, knapsack_with_items


class TestKnapsackSolver(unittest.TestCase):
    """Test cases for the knapsack solver"""
    
    def test_basic_example(self):
        """
        Test the basic example from the original requirements.
        
        This test SHOULD PASS but currently FAILS due to regression bug.
        Expected: max_value = 10 (items with weights 3 and 5, total weight 8)
        Actual: max_value = 0 (bug causes early return)
        """
        capacity = 10
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        
        result = knapsack(capacity, weights, values)
        
        # This assertion will FAIL - expected 10, but gets 0
        self.assertEqual(result, 10, 
                        "Should select items with weights [3,5] for max value 10")
    
    def test_simple_case(self):
        """
        Test a simple case with 2 items.
        
        This test SHOULD PASS but currently FAILS.
        Expected: max_value = 60 (select the second item)
        Actual: max_value = 0
        """
        capacity = 50
        weights = [10, 20]
        values = [40, 60]
        
        result = knapsack(capacity, weights, values)
        
        # This assertion will FAIL
        self.assertEqual(result, 100, 
                        "Should select both items for max value 100")
    
    def test_single_item_fits(self):
        """
        Test with single item that fits in knapsack.
        
        This test SHOULD PASS but currently FAILS.
        Expected: max_value = 100
        Actual: max_value = 0
        """
        capacity = 10
        weights = [5]
        values = [100]
        
        result = knapsack(capacity, weights, values)
        
        # This assertion will FAIL
        self.assertEqual(result, 100, 
                        "Should select the single item that fits")
    
    def test_empty_knapsack(self):
        """
        Test with zero capacity - should return 0.
        
        This test PASSES correctly.
        """
        capacity = 0
        weights = [2, 3, 4]
        values = [3, 4, 5]
        
        result = knapsack(capacity, weights, values)
        
        # This assertion PASSES
        self.assertEqual(result, 0, 
                        "Zero capacity should give zero value")
    
    def test_empty_items(self):
        """
        Test with no items - should return 0.
        
        This test PASSES correctly.
        """
        capacity = 10
        weights = []
        values = []
        
        result = knapsack(capacity, weights, values)
        
        # This assertion PASSES
        self.assertEqual(result, 0, 
                        "No items should give zero value")
    
    def test_classic_example(self):
        """
        Test classic knapsack problem example.
        
        This test SHOULD PASS but currently FAILS.
        Expected: Optimal solution value should be 220
        Actual: 0
        """
        capacity = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        
        result = knapsack(capacity, weights, values)
        
        # This assertion will FAIL - expected 220, gets 0
        self.assertEqual(result, 220, 
                        "Should select items 2 and 3 for max value 220")


class TestKnapsackWithItems(unittest.TestCase):
    """Test cases for knapsack solver with item tracking"""
    
    def test_basic_with_items(self):
        """
        Test that the function returns correct max value and items.
        
        This test FAILS due to the same regression bug.
        """
        capacity = 10
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        
        max_value, items = knapsack_with_items(capacity, weights, values)
        
        # This assertion will FAIL
        self.assertEqual(max_value, 10, 
                        "Max value should be 10")


if __name__ == '__main__':
    unittest.main()
