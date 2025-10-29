"""
The filter() function is used to pick only those elements from a 
list (or any iterable) that satisfy a certain condition.
"""

# Example 1: Using filter() to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Example 2: Using filter() to get strings with more than 3 characters
words = ['apple', 'banana', 'cherry', 'date']
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)  # Output: ['apple', 'banana', 'cherry']

# Example 3: Using filter() with a custom function
def is_positive(n):
    return n > 0

numbers = [-2, -1, 0, 1, 2]
positive_numbers = list(filter(is_positive, numbers))
print(positive_numbers)  # Output: [1, 2]

# Summary:
# The filter() function is a useful tool for extracting elements from a
# collection based on a specified condition.