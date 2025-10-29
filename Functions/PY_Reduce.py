"""
The reduce() function takes a list of values and keeps combining 
them one by one until only one final result is left.

syntax: reduce(function, iterable, [initializer])
"""

# Example 1: Using reduce() to sum a list of numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15


# Example 2: Using reduce() to find the maximum value in a list
numbers = [3, 1, 4, 1, 5, 9]
max_result = reduce(lambda x, y: x if x > y else y, numbers)
# How does this work on each step? First it compares 3 and 1, keeps 3. 
# Then compares 3 and 4, keeps 4. 
# Then compares 4 and 1, keeps 4. 
# Then compares 4 and 5, keeps 5. Finally compares 5 and 9, keeps 9.
print(max_result)  # Output: 9


# Example 3: Using reduce() to concatenate a list of strings
strings = ['Hello', ' ', 'World', '!']
concat_result = reduce(lambda x, y: x + y, strings)
print(concat_result)  # Output: 'Hello World!'

# Example 4: Using reduce() with an initializer
numbers = [1, 2, 3]
product_result = reduce(lambda x, y: x * y, numbers, 10)
# Here the initializer is 10, so the calculation goes like this:
# 10 (initializer) * 1 = 10
# 10 * 2 = 20
# 20 * 3 = 60
print(product_result)  # Output: 60

#Summary:
# The reduce() function is a powerful tool for performing cumulative operations
# on a list of values, allowing you to reduce the list to a single value based
# on a specified function.