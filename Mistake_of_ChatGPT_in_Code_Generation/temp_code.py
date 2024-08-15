import functools
import math
import random
import math

def f(max_value, items=[(3, 60, 5), (2, 100, 7), (1, 120, 11)], capacity=5) -> bool:
    dp = [0] * (capacity + 1)
    for item in items:
        for i in range(capacity, item[0] - 1, -1):
            dp[i] = max(dp[i], dp[i - item[0]] + item[1])
    return dp[capacity] == max_value
def g(items=[(3, 60, 5), (2, 100, 7), (1, 120, 11)], capacity=5, max_value=220):
    
    # Sort items by weight
    items.sort(key=lambda x: x[0])
    
    # Initialize a 2-D matrix dp, where dp[i][j] represents the current maximum value we can get
    # considering first i elements with total weight not exceeding j
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]
    
    # Process all items
    for i in range(1, len(items)+1):
        weight, value, _ = items[i-1]
        
        # Process all weights
        for j in range(capacity+1):
        
            # If the weight of the current item is less than or equal to j, then consider it
            if weight <= j:
                dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
            else: 
                dp[i][j] = dp[i-1][j]
                
    # The bottom-right corner of the dp table represents the maximum total value that can be put in the knapsack
    max_value = dp[len(items)][capacity]
    
    # Check if the solution satisfies the provided maximum value criterion
    if max_value > max_value:
        return "No solution can satisfy the provided maximum value criterion!"
    else:
        return "The maximum value that can be achieved is: " + str(max_value)
assert f(g())