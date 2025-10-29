"""
In Python, a list is a mutable sequence of elements, 
which can be of different types.

Mutable: Lists can be modified after their creation (elements can be added, removed, or changed).
Ordered: Elements in a list maintain their order, and each element can be accessed by its index.
Allows Duplicates: Lists can contain duplicate elements.
Lists are defined using square brackets [] and elements are separated by commas.
Index-based: Each element in a list can be accessed using its index, starting from 0 for the first element.
Supports Various Data Types: Lists can contain elements of different
data types, including integers, strings, floats, and even other lists or tuples.

"""

#Example 1: Creating Lists
list1 = [1, 2, 3, 4, 5] #numeric list   
list2 = ["apple", "banana", "cherry"]  #string list
print(list1)
print(list2)

# Example 1.1: List() Constructor
list3 = list((1, 2, 3, 4, 5)) # using list() constructor with a tuple
list4 = list(["apple", "banana", "cherry"]) # using list() constructor with a list
print(list3)
print(list4)

# Creating list using square brackets [] vs list() constructor
list_a = [1, 2, 3]  # Using square brackets
list_b = list((1, 2, 3))  # Using list() constructor
print(list_a)  # Output: [1, 2, 3]
print(list_b)  # Output: [1, 2, 3]
# Both methods create a list with the same elements, but the syntax is different.
# The square brackets [] are more commonly used for creating lists.
# The list() constructor can be useful when converting other data types (like tuples or sets) into lists.

#Example 2: Accessing Elements
sample_list = [10, 20, 30, 40, 50]
print(sample_list[0])  # Output: 10
print(sample_list[1])  # Output: 20
print(sample_list[2])  # Output: 30
print(sample_list[3])  # Output: 40
print(sample_list[4])  # Output: 50
# Lists are indexed starting from 0 from the left and -1 from the right.
# Note: Accessing an index out of range will cause an IndexError. 
# Only integers are allowed as indices and using a float or other types will result in a TypeError.

#Example 3: List Mutability
mutable_list = [1, 2, 3]
mutable_list[0] = 100  # This is allowed
print(mutable_list)    # Output: [100, 2, 3]
# Lists can be changed after they are created.

#Example 4: List Concatenation
list_a = [1, 2, 3]
list_b = [4, 5, 6]
concatenated_list = list_a + list_b
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

#Example 5: List Slicing
slice_list = [1, 2, 3, 4, 5]
print(slice_list[0:3])  # Output: [1, 2, 3] # Slicing from index 0 to 2 (3 is excluded)
print(slice_list[2:])    # Output: [3, 4, 5] # Slicing from index 2 to the end
print(slice_list[:3])    # Output: [1, 2, 3] # Slicing from the start to index 2 (3 is excluded)
print(slice_list[-2:])   # Output: [4, 5] # Slicing the last two elements
print(slice_list[:-2])   # Output: [1, 2, 3] # Slicing from the start to the third last element (excluding the last two elements)
# Slicing allows you to extract a portion of a list by specifying a start and end index

#Example 6: List Methods
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)            # Output: ['apple', 'banana', 'cherry', 'orange']
fruits.remove("banana")
print(fruits)            # Output: ['apple', 'cherry', 'orange']
print(fruits.index("cherry"))  # Output: 2, here the index of cherry is 2
print(fruits.count("apple"))   # Output: 1
fruits.sort()
print(fruits)            # Output: ['apple', 'cherry', 'orange']
fruits.reverse()
print(fruits)            # Output: ['orange', 'cherry', 'apple']

#Example 7: List Comprehension, meaning creating a new list by applying an expression to each item in an existing iterable (like a list or range).
squared_numbers = [x**2 for x in range(1, 6)] # here range(1,6) generates numbers from 1 to 5
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


#Example 8: Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0])      # Output: [1, 2, 3]
print(nested_list[1][1])   # Output: 5  # Accessing element 5 from the second list
print(nested_list[2][0])   # Output: 7  # Accessing element 7 from the third list
# Nested lists are lists within lists, allowing for multi-dimensional data structures.
#    0 1 2
# 0 [1,2,3]  # First list
# 1 [4,5,6]  # Second list [1][1] = 5
# 2 [7,8,9]  # Third list [2][0] = 7


#Example 9: List Length
length_list = [10, 20, 30, 40, 50]
print(len(length_list))  # Output: 5, as there are 5 elements in the list
# The len() function returns the number of elements in a list.

#Example 10: Iterating Through a List
iterate_list = ["apple", "banana", "cherry"]
for fruit in iterate_list:
    print(fruit)
# Output:
# apple 
# banana
# cherry
# You can use a for loop to iterate through each element in a list.



#Example 11: Checking Membership
membership_list = [1, 2, 3, 4, 5]
print(3 in membership_list)   # Output: True
print(6 in membership_list)   # Output: False
print(3 not in membership_list) # Output: False
print(6 not in membership_list) # Output: True
# The 'in' keyword checks if an element exists in the list, returning True or False.
# The 'not in' keyword checks if an element does not exist in the list, returning True or False.

#Example 12: Copying a List
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # Output: [1, 2, 3]

# Note: Using assignment (e.g., list2 = list1) creates a reference to the same list,
# so changes to one list will affect the other. Using the copy() method creates a shallow copy of the list.
original_list1 = [1, 2, 3]
original_list2 = [2, 3, 4]

original_list2 = original_list1.copy()
print(original_list2) # Output: [1, 2, 3]


#Example 13: Clearing a List
clear_list = [1, 2, 3, 4, 5]
clear_list.clear()
print(clear_list)  # Output: []
# The clear() method removes all elements from the list, resulting in an empty list.


#Example 14: Extending a List
extend_list1 = [1, 2, 3]
extend_list2 = [4, 5, 6]
extend_list1.extend(extend_list2) 
print(extend_list1)  # Output: [1, 2, 3, 4, 5, 6]
# The extend() method adds elements from another list (or any iterable) to the end of the current list.


#Example 15: Appending vs Extending
append_list = [1, 2, 3]
append_list.append([4, 5])  # Appending a list as a single element
print(append_list)  # Output: [1, 2, 3, [4, 5]]
append_list = [1, 2, 3]
append_list.extend([4, 5])  # Extending the list with elements from another list
print(append_list)  # Output: [1, 2, 3, 4, 5]
# The append() method adds its argument as a single element to the end of a list,
# while the extend() method iterates over its argument adding each element to the list, extending the list.


#Example 16: Inserting Elements
insert_list = [1, 2, 4, 5]
insert_list.insert(2, 3)  # Insert 3 at index 2
print(insert_list)  # Output: [1, 2, 3, 4, 5]
# The insert() method allows you to add an element at a specific index in the list.
# Note: If the index is greater than the list length, the element will be added to the end of the list.
# If the index is negative, it counts from the end of the list.


#Append vs Insert
append_list = [1, 2, 3]
append_list.append(4)  # Appending 4 to the end of the list
print(append_list)  # Output: [1, 2, 3, 4]

insert_list = [1, 2, 4]
insert_list.insert(2, 3)  # Inserting 3 at index 2
print(insert_list)  # Output: [1, 2, 3, 4]



#Example 17: Removing Elements by Index
remove_index_list = [1, 2, 3, 4, 5]
removed_element = remove_index_list.pop(2)  # Remove element at index 2
print(removed_element)  # Output: 3
print(remove_index_list)  # Output: [1, 2, 4, 5]
# The pop() method removes and returns the element at the specified index.


#Example 18: Finding the Minimum and Maximum
min_max_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(min(min_max_list))  # Output: 1
print(max(min_max_list))  # Output: 9
# The min() and max() functions return the smallest and largest elements in the list, respectively.


#Example 19: Repeating Lists
repeat_list = [1, 2, 3]
repeated_list = repeat_list * 3
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
# You can repeat the elements of a list by multiplying the list by an integer.


#Example 20: Converting Other Data Types to a List
tuple_data = (1, 2, 3)
list_from_tuple = list(tuple_data) # Here list() constructor is used to convert tuple to list
print(list_from_tuple)  # Output: [1, 2, 3]
# You can convert other data types, like tuples or sets, to a list using the list() constructor.

set_data = {4, 5, 6}
list_from_set = list(set_data) # Here list() constructor is used to convert set to list
print(list_from_set)  # Output: [4, 5, 6]

dict_data = {'a': 1, 'b': 2, 'c': 3}
list_from_dict = list(dict_data.keys())  # Converts dictionary keys to a list
print(list_from_dict)  # Output: ['a', 'b', 'c']

dict_data = {'a': 1, 'b': 2, 'c': 3}
list_from_dict = list(dict_data.values())  # Converts dictionary values to a list
print(list_from_dict)  # Output: [1, 2, 3]


dict_data = {'a': 1, 'b': 2, 'c': 3}
list_from_dict = list(dict_data.items())  # Converts dictionary items (key-value pairs) to a list
print(list_from_dict)  # Output: [('a', 1), ('b', 2), ('c', 3)]



#Example 21: List with Mixed Data Types
mixed_list = [1, "two", 3.0, [4, 5], (6, 7)]
print(mixed_list)  # Output: [1, 'two', 3.0 [4, 5], (6, 7)]
# Lists can contain elements of different data types, including integers, strings, floats, and even other lists or tuples.
# Example 22: List with Different Data Types
data_type_list = [42, "Hello", 3.14, True, None, [1, 2, 3], (4, 5)]
print(data_type_list)  # Output: [42, 'Hello', 3.14, True, None, [1, 2, 3], (4, 5)]
# This list contains an integer, a string, a float, a boolean, a NoneType, a list, and a tuple. 
# Python lists are versatile and can hold a variety of data types within the same list.




#Example 23: List Comprehension with Condition, which means creating a new list by applying an expression to 
# each item in an existing iterable (like a list or range), but only including items that meet a certain condition.
conditional_list = [x for x in range(10) if x % 2 == 0]
print(conditional_list)  # Output: [0, 2, 4, 6, 8]
# This list comprehension creates a list of even numbers from 0 to 9 by including a condition (if x % 2 == 0).  



#Example 24: Flattening a Nested List
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [item for sublist in nested_list for item in sublist] # in this step we are using two for loops, one for iterating through each sublist and another for iterating through each item in the sublist.
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
# This list comprehension flattens a nested list (a list of lists) into a single list by iterating through each sublist and then through each item in the sublist.  

# Alternative method 
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = []
for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
# This method uses nested for loops to achieve the same result as the list comprehension above, app


# Iteration Step-by-Step
# First sublist: [1, 2, 3]
# Take 1 → append → [1]
# Take 2 → append → [1, 2]
# Take 3 → append → [1, 2, 3]
# Second sublist: [4, 5]
# Take 4 → append → [1, 2, 3, 4]
# Take 5 → append → [1, 2, 3, 4, 5]
# Third sublist: [6, 7, 8]
# Take 6 → append → [1, 2, 3, 4, 5, 6]
# Take 7 → append → [1, 2, 3, 4, 5, 6, 7]
# Take 8 → append → [1, 2, 3, 4, 5, 6, 7, 8]


#Example 25: Using enumerate() with Lists, enumerate means adding a counter to an iterable and returning it as an enumerate object.
enumerate_list = ['a', 'b', 'c']
for index, value in enumerate(enumerate_list):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: a
# Index: 1, Value: b
# Index: 2, Value: c
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# This is useful when you need both the index and the value while iterating through a list.


#Example 26: Using zip() with Lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_list = list(zip(list1, list2))
print(zipped_list)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# The zip() function combines elements from multiple iterables (like lists) into tuples,
# where the i-th tuple contains the i-th element from each of the input iterables.
# If the input iterables are of different lengths, zip() stops creating tuples when the shortest

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
zipped_list = list(zip(list1, list2))
print(zipped_list)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# In this case, since list1 has 3 elements and list2 has 4 elements#, zip() creates tuples only up to the length of the shorter list (list1).
# The extra element 'd' in list2 is ignored.

#Example 27: Using map() with Lists
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
# The map() function applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator).
# You can convert the map object to a list using the list() constructor.


#Example 28: Using filter() with Lists
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]
# The filter() function constructs an iterator from elements of an iterable for which a function returns true.  
# You can convert the filter object to a list using the list() constructor.

#Example 29: List with User Input
user_input_list = []
n = int(input("Enter the number of elements you want in the list: "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    user_input_list.append(element) 
print("Your list:", user_input_list)
# This code snippet allows the user to create a list by specifying the number of
# elements and entering each element one by one, appending each item to a new list using the append() method.



#Example 30: Reverse a List
reverse_list = [1, 2, 3, 4, 5]
reverse_list.reverse()
print(reverse_list)  # Output: [5, 4, 3, 2, 1]

# The reverse() method reverses the elements of the list in place, meaning it modifies the original list.
# Note: This method does not return a new list; it returns None. The original list is changed.


#Example 31: extending a List with Another Iterable
extend_iterable_list = [1, 2, 3]
extend_iterable_list.extend((4, 5))  # Extending with a tuple
print(extend_iterable_list)  # Output: [1, 2, 3, 4, 5]
extend_iterable_list.extend({6, 7})  # Extending with a set 

print(extend_iterable_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
# The extend() method can take any iterable (like a tuple, set, or string) and adds its elements to the end of the list.
# Note: When extending with a string, each character in the string is added as a separate




#Example 32: Shallow vs Direct reference Copy
original_list = [1, 2, 3]
shallow_copied_list = original_list.copy()  # Creates a shallow copy of the list
direct_reference_list = original_list      # Creates a direct reference to the same list
shallow_copied_list[0] = 100  # Modifying the shallow copy
print("Original List after modifying shallow copy:", original_list)  # Output: [1, 2, 3]
print("Shallow Copied List:", shallow_copied_list)  # Output: [100, 2, 3]
direct_reference_list[1] = 200  # Modifying the direct reference
print("Original List after modifying direct reference:", original_list)  # Output: [1, 200, 3]
print("Direct Reference List:", direct_reference_list)  # Output: [1, 200, 3]

# direct_reference_list = original_list  Direct reference
# Both variables point to the same list in memory.

# shallow_copied_list = original_list.copy()  Shallow copy
# A new list is created in memory, and changes to this new list do not affect the original list.
