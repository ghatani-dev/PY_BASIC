"""
For loop
syntax:
for item in iterable:
    statements
"""
# Example 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Iterating through a string
for char in "hello":
    print(char)


"""
range(stop): Generates numbers from 0 to stop-1
range(start, stop): Generates numbers from start to stop-1
range(start, stop, step): Generates numbers from start to stop-1 with incrementing by step
"""

# Example 3: Using range() function
for i in range(5):
    print(i)

# Example 4: Using break and continue
# Break exits the loop, Continue skips the current iteration
# reak statement is used to exit the loop prematurely when a specified condition is met.
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Print odd numbers only


#Example 5: range with start, stop
for i in range(2, 10):
    print(i)  # Prints even numbers from 2 to 8

    
#Example 6: range with start, stop, step
for i in range(1, 10, 2):
    print(i)  # Prints odd numbers from 1 to 9


#Example 7 : Iterating through a tuple
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

#Example 8 : Iterating through a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key in person:
    print(key, ":", person[key])


#Example 9 : Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")


#Example 10: Iterating through a set
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)