"""
Operators in Python

Arithmetic Operators in Python

a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)   



Python Assignment Operators
# assign 5 to x 
x = 5


Python Comparison Operators
a = 5
b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)


Python Logical Operators
print((a > 2) and (b >= 6))    # True
print((a > 2) or (b >= 6))     # True
print(not(a > 2))              # False


Identity operators
is and is not are the identity operators in Python. 
They are used to compare the memory locations of two objects.

a = 5
b = 5

# is operator
print('a is b =', a is b) o/p -> True

# is not operator
print('a is not b =', a is not b) o/p -> False

c = [1, 2, 3]
d = [1, 2, 3]

print('c is d =', c is d) o/p -> False
print('c is not d =', c is not d) o/p -> True



Membership operators in Python
in and not in are the membership operators in Python. 
They are used to test whether a value or variable 
is found in a sequence (string, list, tuple, set, or dictionary).

a = 5
b = 10
list = [1, 2, 3, 4, 5]
print(a in list)        # True
print(b not in list)    # True
print(a not in list)    # False
print(b in list)        # False
"""