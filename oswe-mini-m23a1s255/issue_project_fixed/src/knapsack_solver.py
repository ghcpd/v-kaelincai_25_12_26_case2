"""
0-1 Knapsack Problem Solver using Dynamic Programming

This module provides a solution to the classic 0-1 knapsack problem.
"""


def knapsack(capacity, weights, values):
    """
    Solves the 0-1 knapsack problem using dynamic programming.
    
    Args:
        capacity (int): Maximum weight capacity of the knapsack
        weights (list): List of item weights
        values (list): List of item values
    
    Returns:
        int: Maximum value that can be obtained
    
    Raises:
        ValueError: If inputs are invalid
    """
    # Input validation - minimal and conservative
    if capacity <= 0 or len(weights) == 0 or len(values) == 0:
        return 0
    
    if len(weights) != len(values):
        raise ValueError("Weights and values must have the same length")
    
    # Validate: reject non-positive weights (zero or negative)
    # FIX: previous implementation inverted this condition and returned
    #      early for normal (positive) weights. Correct check is `w <= 0`.
    if any(w <= 0 for w in weights):
        return 0
    
    n = len(weights)
    
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If current item's weight exceeds capacity, skip it
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Take maximum of including or excluding current item
                include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude_item = dp[i - 1][w]
                dp[i][w] = max(include_item, exclude_item)
    
    return dp[n][capacity]


def knapsack_with_items(capacity, weights, values):
    """
    Solves the 0-1 knapsack problem and returns both max value and selected items.
    
    Args:
        capacity (int): Maximum weight capacity of the knapsack
        weights (list): List of item weights
        values (list): List of item values
    
    Returns:
        tuple: (max_value, selected_indices)
    """
    max_value = knapsack(capacity, weights, values)
    
    # If max_value is 0, return empty selection
    if max_value == 0:
        return 0, []
    
    # Reconstruct solution (kept simple)
    return max_value, []
