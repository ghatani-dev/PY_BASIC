"""
Tuples in Python
-> Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
-> Tuples can hold elements of different data types.
-> Tuples are defined by enclosing elements in parentheses ().
-> The main characteristics of tuples are being ordered, heterogeneous and immutable.

Syntax: my_tuple = (element1, element2, element3, ...)
"""

#Example 1: Creating a Tuple
my_tuple = (1, "Hello", 3.14, True) # A tuple with different data types
print(my_tuple)  # Output: (1, 'Hello', 3.14, True)


#Example 2: Accessing Tuple Elements
print(my_tuple[1])  # Output: Hello (Accessing the second element)
print(my_tuple[-1]) # Output: True (Accessing the last element)
print(my_tuple[1:3]) # Output: ('Hello', 3.14) (Slicing the tuple)
print(my_tuple[:2])  # Output: (1, 'Hello') (Slicing from start to index 2)
print(my_tuple[2:])  # Output: (3.14, True) (Slicing from index 2 to end)
print(my_tuple[::2]) # Output: (1, 3.14) (Slicing with step of 2), meaning every second element
print(my_tuple[::-1]) # Output: (True, 3.14, 'Hello', 1) (Reversing the tuple)
print(my_tuple[1:4:2]) # Output: ('Hello', True) (Slicing from index 1 to 4 with step of 2)
print(my_tuple[-3:-1]) # Output: ('Hello', 3.14) (Slicing with negative indices)
print(my_tuple[-1:-4:-1]) # Output: (True, 3.14, 'Hello') (Slicing with negative indices in reverse order)
print(my_tuple[-4:]) # Output: (1, 'Hello', 3.14, True) (Slicing from negative index to end)
print(my_tuple[:-2]) # Output: (1, 'Hello') (Slicing from start to negative index)
print(my_tuple[-3:2]) # Output: () (Slicing with negative start index and positive end index, results in empty tuple)
print(my_tuple[::3]) # Output: (1, True) (Slicing with step of 3)
print(my_tuple[1::2]) # Output: ('Hello', True) (Slicing from index 1 to end with step of 2)
print(my_tuple[1:-1]) # Output: ('Hello', 3.14) (Slicing from index 1 to negative index -1)
print(my_tuple[0:3:2]) # Output: (1, 3.14) (Slicing from index 0 to 3 with step of 2)
print(my_tuple[-4:-1:2]) # Output: (1, 3.14) (Slicing with negative indices and step of 2)
print(my_tuple[-1:1:-1]) # Output: (True, 3.14, 'Hello') (Slicing in reverse order from negative index to positive index)
print(my_tuple[2:0:-1]) # Output: (3.14, 'Hello') (Slicing in reverse order from index 2 to 0)
print(my_tuple[::]) # Output: (1, 'Hello', 3.14, True) (Slicing the entire tuple)
print(my_tuple[:]) # Output: (1, 'Hello', 3.14, True) (Slicing the entire tuple)
print(my_tuple[-2:]) # Output: (3.14, True) (Slicing from negative index -2 to end)


#Example 3: Empty Tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

#Example 4: Using Strings
string_tuple = tuple("Hello") # Converting a string to a tuple
print(string_tuple)  # Output: ('H', 'e', 'l', 'l', 'o')


#Example 5: Using Lists
list_data = [1, 2, 3]
list_to_tuple = tuple(list_data) # Converting a list to a tuple
print(list_to_tuple)  # Output: (1, 2, 3)

#Example 6: Tuple with One Element
single_element_tuple = (42,) # Note the comma
print(single_element_tuple)  # Output: (42,)

#Example 7: Tuple with nested tuples
tuple_1 = (1, 2)
tuple_2 = (3, 4)
nested_tuple = (tuple_1, tuple_2)
print(nested_tuple)  # Output: ((1, 2), (3, 4))

#Example 8: Tuple with repetition
repeated_tuple = ("Python",) * 3
print(repeated_tuple)  # Output: ('Python', 'Python', 'Python')


#Example 9: Tuple with the use of loop
tuple_loop = (10, 20, 30)
for item in tuple_loop:
    print(item)
# Output:
# 10
# 20
# 30


#Example 10: Tuple with the use of if-else
tuple_if_else = (5, 10, 15)
if 10 in tuple_if_else:
    print("10 is present in the tuple")
else:
    print("10 is not present in the tuple")


# Example 11: Tuple with the use of functions
def sum_of_tuple(tup):
    return sum(tup) # Function to calculate the sum of elements in a tuple
result = sum_of_tuple((1, 2, 3, 4))
print(result)  # Output: 10


#Example 12: Tuple Unpacking
coordinates = (10, 20)
x, y = coordinates # Unpacking the tuple into variables
print(f"x: {x}, y: {y}")  # Output: x: 10, y: 20


#Example 13: Tuple Methods
sample_tuple = (1, 2, 3, 2, 4, 2)
count_of_2 = sample_tuple.count(2) # Count occurrences of 2
index_of_3 = sample_tuple.index(3)   # Find index of first occurrence of 3
print(f"Count of 2: {count_of_2}")  # Output: Count of 2: 3
print(f"Index of 3: {index_of_3}")    # Output: Index of 3: 2

#Example 14: Nested Tuples
nested = (1, (2, 3), (4, (5, 6)))
print(nested[1])        # Output: (2, 3)
print(nested[2][1][0])  # Output: 5

# Note 1: if its wrapped in []  or passed into list(), it's a list. eg: [1, 2, 3] or list((1, 2, 3))
# Note 2: if its wrapped in () or seperated by commas, it's a tuple. eg: (1, 2, 3) or 1, 2, 3 or tuple([1, 2, 3])
# Note 3: Tuples are faster than lists because of their immutability


#Example 15: Immutability of Tuples
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 10  # This will raise a TypeError
# print(immutable_tuple)  # Uncommenting the above lines will show that tuples cannot be modified


#Example 16: Tuple Concatenation
tuple_a = (1, 2)
tuple_b = ("Hello", "Python!")
concatenated_tuple = tuple_a + tuple_b # Concatenating two tuples
print(concatenated_tuple)  # Output: (1, 2, 'Hello', 'Python!')


#Example 17: Tuple Repetition
repeated = ("Repeat",) * 3 # Repeating a tuple
print(repeated)  # Output: ('Repeat', 'Repeat', 'Repeat')

#Example 18: Tuple Membership
membership_tuple = (10, 20, 30)
print(10 in membership_tuple)  # Output: True
print(40 in membership_tuple)  # Output: False

#Example 19: Tuple Length
length = len(membership_tuple)
print(f"Length of membership_tuple: {length}")  # Output: Length of membership_tuple: 3


#Example 20: Converting Other Data Types to a Tuple
list_data = [1, 2, 3]
tuple_from_list = tuple(list_data) # Here tuple() constructor is used to convert list to tuple
print(tuple_from_list)  # Output: (1, 2, 3)

set_data = {4, 5, 6}
tuple_from_set = tuple(set_data) # Here tuple() constructor is used to convert set to tuple
print(tuple_from_set)  # Output: (4, 5, 6)

dict_data = {'a': 1, 'b': 2, 'c': 3}
tuple_from_dict = tuple(dict_data) # Here tuple() constructor is used to convert dict keys to tuple
print(tuple_from_dict)  # Output: ('a', 'b', 'c')


dict_data = {'a': 1, 'b': 2, 'c': 3}
tuple_from_dict = tuple(dict_data.keys()) # Here tuple() constructor is used to convert dict keys to tuple
print(tuple_from_dict)  # Output: ('a', 'b', 'c')

dict_values_tuple = tuple(dict_data.values()) # Here tuple() constructor is used to convert dict values to tuple
print(dict_values_tuple)  # Output: (1, 2, 3)

dict_items_tuple = tuple(dict_data.items()) # Converting dict items to tuple of tuples
print(dict_items_tuple)  # Output: (('a', 1), ('b', 2), ('c', 3))



#Example 21: Tuple with zip()
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = tuple(zip(list1, list2)) # Zipping two lists into a tuple of tuples
print(zipped)  # Output: ((1, 'a'), (2, 'b'), (3, 'c'))

    
#Example 22: Tuple with map()
numbers = (1, 2, 3, 4)
squared = tuple(map(lambda x: x**2, numbers)) # Squaring each element in the tuple
print(squared)  # Output: (1, 4, 9, 16)


#Example 23: Tuple with filter()
numbers = (1, 2, 3, 4, 5, 6)
even_numbers = tuple(filter(lambda x: x % 2 == 0, numbers)) # Filtering even numbers from the tuple
print(even_numbers)  # Output: (2, 4, 6)


#Example 24: Tuple with sorted()
unsorted_tuple = (3, 1, 4, 2)   
sorted_tuple = tuple(sorted(unsorted_tuple)) # Sorting the tuple
print(sorted_tuple)  # Output: (1, 2, 3, 4)

# Note: Since tuples are immutable, operations that would modify a tuple 
# (like adding or removing elements) will return a new tuple instead.

# Take (1, 2, 3) → add 4 → (1, 2, 3, 4)
# Take (1, 2, 3, 4) → remove 2 → (1, 3, 4)
# Take (1, 3, 4) → extend (5, 6, 7) → (1, 3, 4, 5, 6, 7)
# Take (1, 3, 4, 5, 6, 7) → remove 3 → (1, 4, 5, 6, 7)
# Take (1, 4, 5, 6, 7) → insert 2 at index 1 → (1, 2, 4, 5, 6, 7)
# Take (1, 2, 4, 5, 6, 7) → remove last element → (1, 2, 4, 5, 6)
# Take (1, 2, 4, 5, 6) → remove element at index 2 → (1, 2, 5, 6)
# Take (1, 2, 5, 6) → clear all elements → ()


#Example 25: Using enumerate() with Tuples, enumerate means adding a counter to an iterable and returning it as an enumerate object.
enumerate_tuple = ('a', 'b', 'c')
enumerated = tuple(enumerate(enumerate_tuple))
print(enumerated)  # Output: ((0, 'a'), (1, 'b'), (2, 'c'))

# Note: The enumerate object can be converted to a list or tuple to see the indexed pairs.

#Example 26: Tuple with all() and any()
bool_tuple = (True, True, False)
print(all(bool_tuple))  # Output: False
print(any(bool_tuple))  # Output: True
# Note: all() returns True if all elements are True, any() returns True if any element is True.

any_false = any(x is False for x in bool_tuple)
print(any_false) # Output: True, Check if any element is False

all_false = all(x is False for x in bool_tuple) # Check if all elements are False
print(all_false) # Output: False


#Example 27: Tuple with id() and type()
sample_tuple = (1, 2, 3)
print(id(sample_tuple))  # Output: Unique ID of the tuple
print(type(sample_tuple))  # Output: <class 'tuple'>
# Note: id() returns the unique identifier of the object, type() returns the type of the object.


#Example 28: Tuple with divmod()
a = 10
b = 3
result = divmod(a, b)  # Returns a tuple (quotient, remainder)
print(result)  # Output: (3, 1)
# Note: divmod() takes two numbers and returns a tuple containing their quotient and remainder.


#Example 29: Tuple with pow()
base = 2
exponent = 3
result = pow(base, exponent)  # Returns base raised to the power of exponent
print(result)  # Output: 8
# Note: pow() can also take a third argument for modulo operation.


#Example 30: Tuple with repr()
sample_tuple = (1, 2, 3)
print(repr(sample_tuple))  # Output: (1, 2, 3)
# Note: repr() returns a string representation of the object.


#Example 31: Tuple with slice()
sample_tuple = (1, 2, 3, 4, 5)
sliced = sample_tuple[1:4]  # Slicing the tuple
print(sliced)  # Output: (2, 3, 4)


# Note: slice() can also be used to create a slice object for more complex slicing operations.
slice_obj = slice(1, 4)
sliced_with_obj = sample_tuple[slice_obj]
print(sliced_with_obj)  # Output: (2, 3, 4)



#Example 32: Tuple with comprehensions (using generator expressions)
squared_tuple = tuple(x**2 for x in range(5)) # Creating a tuple of squares using a generator expression
print(squared_tuple)  # Output: (0, 1, 4, 9, 16)