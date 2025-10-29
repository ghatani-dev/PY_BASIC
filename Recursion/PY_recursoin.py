"""
Recursion in Python
This script demonstrates the concept of recursion in Python.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
# Explanation:
# The factorial function calls itself with a decremented value of n until it reaches 0.

# Types of Recursion:
# 1. Tail Recursion: The recursive call is the last operation in the function.
def tail_recursive_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_recursive_factorial(n-1, n * accumulator)
print(tail_recursive_factorial(5))  # Output: 120

# 2. Non-Tail Recursion: The recursive call is not the last operation in the function.
def non_tail_recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + non_tail_recursive_sum(n-1)
print(non_tail_recursive_sum(5))  # Output: 15