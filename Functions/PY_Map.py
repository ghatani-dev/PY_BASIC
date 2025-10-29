"""
map() function in python applies a given function to all items 
in an input list (or any iterable) and returns an iterator (map object) with the results.

Syntax:map(function, iterable, ...)

"""

"""
Understanding the map() Function in Python, how it works behind the scenes.

numbers = (1,2)
result = map(lambda x: x**2, numbers)
print(result)


Here, map() takes two arguments: 

1. a lambda function that squares a number (lambda x: x**2) 
2. an iterable (numbers  which can be a list, tuple, or any other iterable).

The map() function applies the lambda function to each item in the numbers iterable.

o/p: <map object at 0x7bd5e6bcde10>  # Not a list or tuple!

So, the result is a map object, which is an iterator -- meaning you can loop through it, 
but it doesn’t display values directly.

Therefore, to view or store the results:

1. if you want a list, you do: list(map(...))
2. if you want a tuple, you do: tuple(map(...))

=> Analogy (Real-Life Example)

Think of map() like juice machine:
- You have a basket of fruits (your iterable).
- You have a recipe (your function) that tells you how to make juice from each fruit.
- The juice machine (map function) takes each fruit from the basket, applies the recipe, and produces juice (the result).
- But this juice is not stored yet! You need to collect it in a container (like a list or tuple) to use it later.

=> What does 0x7bd5e6bcde10 mean in <map object at 0x7bd5e6bcde10> ?
This is a memory address in hexadecimal format.
It tells you where in memory the map object is stored.
That hexadecimal number is just a memory address, It does not represent the data itself — it's just a reference.


=> In Python, almost all objects — including the <map> object you see — are stored on the heap.
- Objects (like lists, tuples, dicts, map objects, functions, lambdas, etc.) are always allocated on the heap.

"""

# Example 1: Using map() with a built-in function
numbers = [1, 2, 3, 4, 5] # List of numbers
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Example 2: Using map() with multiple iterables
numbers1 = [1, 2, 3] # First list of numbers
numbers2 = [4, 5, 6] # Second list of numbers
summed = map(lambda x, y: x + y, numbers1, numbers2)
print(list(summed))  # Output: [5, 7, 9]


# Example 3: Using map() with a custom function
def to_uppercase(s):
    return s.upper() # Here upper() is a built-in string method to convert a string to uppercase.
strings = ['hello', 'world'] # List of strings
uppercased = map(to_uppercase, strings)
print(list(uppercased))  # Output: ['HELLO', 'WORLD']   


# Example 4: Using map() with a list of tuples
tuples = [(1, 2), (3, 4), (5, 6)] # List of tuples, (1, 2) is a tuple with elements 1 and 2.
summed_tuples = map(lambda x: x[0] + x[1], tuples) # Here x[0] and x[1] are the elements of each tuple.
print(list(summed_tuples))  # Output: [3, 7, 11] 

# Example 5: Using map() with a string to convert each character to its ASCII value
chars = 'abc' # String of characters
ascii_values = map(lambda c: ord(c), chars) # Here ord() is a built-in function that returns the ASCII value of a character.
print(list(ascii_values))  # Output: [97, 98, 99]

# Example 6: Using map() with a dictionary to get its keys
my_dict = {'a': 1, 'b': 2, 'c': 3} # Dictionary
keys = map(lambda x: x, my_dict) # Here x is each key in the dictionary.
print(list(keys))  # Output: ['a', 'b', 'c']


# Example 7: Using map() with a dictionary to get its values
my_dict = {'a': 1, 'b': 2, 'c': 3} 
values = map(lambda x: my_dict[x], my_dict) # Here  my_dict[x] gets the value for each key x in the dictionary.
print(list(values))  # Output: [1, 2, 3]

# Example 8: Using map() with a dictionary to get its items
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = map(lambda x: (x, my_dict[x]), my_dict) # Here  my_dict[x] gets the value for each key x in the dictionary and returns a tuple (key, value).
print(list(items))  # Output: [('a', 1), ('b', 2), ('c', 3)]


# Example 9: Using map() with a list of strings to get their lengths
strings = ['apple', 'banana', 'cherry']
lengths = map(lambda s: len(s), strings) # Here len(s) gets the length of each string s.
print(list(lengths))  # Output: [5, 6, 6]

# Example 10: Using map() with a list of numbers to convert them to strings
numbers = [1, 2, 3, 4, 5]       
string_numbers = map(lambda x: str(x), numbers) # Here str(x) converts each number x to a string.
print(list(string_numbers))  # Output: ['1', '2', '3', '4', '5']

#Summary:
# The map() function is a powerful tool in Python that allows you to apply a 
# function to all items in an iterable (like a list) and return a new iterable with
# the results. It's often used for transforming data in a concise and readable way.


