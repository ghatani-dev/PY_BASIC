"""
Python Arrays

Arrays in Python can be implemented using the built-in `array` module, 
which provides an efficient way to store and manipulate homogeneous data types.
Unlike lists, which can hold elements of different types, 
arrays are designed to hold elements of the same type, making them more memory efficient for 
large datasets.

Characteristics of Arrays:
- Arrays are mutable, meaning you can change their content after creation.
- Arrays can hold elements of the same type, making them more memory efficient for large datasets.
- Arrays support various operations such as indexing, slicing, and iteration.
- The `array` module provides a convenient way to create and manipulate arrays in Python.
- Arrays are defined using the `array` module and require a type code to specify the data type of the elements.


syntax:import array as array
my_array = array.array(typecode, [elements])

"""


#Example 1: Creating an Array
import array as arr
my_array = arr.array('i', [1, 2, 3, 4, 5])
print(my_array)
# o/p: array('i', [1, 2, 3, 4, 5])


#Example 2: Accessing Array Elements
import array as arr
my_array = arr.array('i', [10, 20, 30, 40, 50])
print(my_array[0])  # Output: 10


#Example 3: Modifying Array Elements
import array as arr
my_array = arr.array('i', [10, 20, 30, 40, 50])
my_array[1] = 25
print(my_array)  # Output: array('i', [10, 25, 30, 40, 50])


#Example 4: Appending Elements to an Array
import array as arr
my_array = arr.array('i', [1, 2, 3])
my_array.append(4)
print(my_array)  # Output: array('i', [1, 2, 3, 4])


#Example 5: Removing Elements from an Array
import array as arr
my_array = arr.array('i', [1, 2, 3, 4, 5])
my_array.remove(3)
print(my_array)  # Output: array('i', [1, 2, 4, 5])


#Example 6: Iterating Through an Array
import array as arr
my_array = arr.array('i', [1, 2, 3, 4, 5])
for element in my_array:
    print(element)  
# Output:
# 1
# 2
# 3
# 4
# 5


#Example 7: Array Methods
import array as arr
my_array = arr.array('i', [1, 2, 3, 4, 5])
print(my_array.buffer_info())  # Output: (address, size)
print(my_array.typecode)  # Output: 'i'
print(my_array.tolist())  # Output: [1, 2, 3, 4, 5]
print(len(my_array))  # Output: 5   
print(my_array.index(3))  # Output: 2 (index of first occurrence of 3)
print(my_array.count(2))  # Output: 1 (number of occurrences of 2)
print(my_array.reverse())  # Reverses the array in place
print(my_array)  # Output: array('i', [5, 4, 3, 2, 1])
print(my_array.pop())  # Removes and returns the last element
print(my_array)  # Output: array('i', [5, 4, 3, 2]) here 1 is removed since the array is reversed before pop operation.
print(my_array.insert(1, 10))  # Inserts 10 at index 1
print(my_array)  # Output: array('i', [5, 10, 4, 3, 2]) here 10 is inserted at index 1.
print(my_array.extend([6, 7, 8]))  # Extends array by appending elements from the iterable
print(my_array)  # Output: array('i', [5, 10, 4, 3, 2, 6, 7, 8]) here [6,7,8] is added at the end of the array. 
print(my_array.count(10))  # Output: 1 (number of occurrences of 10)
print(my_array.pop(2))  # Removes and returns the element at index 2
print(my_array)  # Output: array('i', [5, 10, 3, 2, 6, 7, 8]) here 4 is removed since it was at index 2 before the previous pop operation.
print(my_array.remove(3))  # Removes the first occurrence of 3
print(my_array)  # Output: array('i', [5, 10, 2, 6, 7, 8]) here 3 is removed.



#Example 8: Slicing an Array
import array as arr
my_array = arr.array('i', [10, 20, 30, 44, 56, 70])
print(my_array[1:4])  # Output: array('i', [20, 30, 44])
print(my_array[:3])  # Output: array('i', [10, 20, 30])
print(my_array[2:])  # Output: array('i', [30, 44, 56, 70])
print(my_array[-3:])  # Output: array('i', [44, 56, 70]) staring from -3 index to the end
print(my_array[:-2])  # Output: array('i', [10, 20, 30, 44]) all elements except last two
print(my_array[::2])  # Output: array('i', [10, 30, 56]) every second element
print(my_array[::-1])  # Output: array('i', [70, 56, 44, 30, 20, 10]) reversed array
print(my_array[1:5:2])  # Output: array('i', [20, 44]) elements from index 1 to 4 with step 2
print(my_array[::3])  # Output: array('i', [10, 44]) every third element
print(my_array[1::3])  # Output: array('i', [20, 56]) every third element starting from index 1
print(my_array[2::3])  # Output: array('i', [30, 70]) every third element starting from index 2
print(my_array[-1::-1])  # Output: array('i', [70, 56, 44, 30, 20, 10]) reversed array using negative step
print(my_array[-2::-1])  # Output: array('i', [56, 44, 30, 20, 10]) reversed array starting from second last element


#Example 9: Creating an Array of Floats
import array as arr
my_float_array = arr.array('f', [1.1, 2.2, 3.3])
print(my_float_array)  # Output: array('f', [1.100000023841858, 2.200000047683716, 3.299999952316284])

#Example 10: Creating an Array of Characters
import array as arr
my_char_array = arr.array('u', ['a', 'b', 'c'])
print(my_char_array)  # Output: array('u', ['a', 'b', 'c'])


# Example 11: Creating an Array of Doubles
import array as arr
my_double_array = arr.array('d', [1.11, 2.22, 3.33])
print(my_double_array)  # Output: array('d', [1.11, 2.22, 3.33])


# Example 12: Creating an Array of Unsigned Integers, meaning only non-negative integers.
import array as arr
my_unsigned_array = arr.array('I', [1, 2, 3])
print(my_unsigned_array)  # Output: array('I', [1, 2, 3])


# Example 13: Creating an Array of Signed Integers, meaning both negative and positive integers.
import array as arr
my_signed_array = arr.array('i', [-1, 0, 1])
print(my_signed_array)  # Output: array('i', [-1, 0, 1])
    
