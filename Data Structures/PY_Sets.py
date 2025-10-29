"""
Python Sets

Set is an unordered collection of multiple items having different datatypes.

Characteristics of Sets:
- Sets are unordered, which means that the items do not have a defined order, and you cannot access items using an index.
- Sets are mutable, meaning you can add or remove items after the set has been created.
- Sets do not allow duplicate items. If you try to add a duplicate item, it will
    be ignored.
- Sets are defined using curly braces {} or the set() function.
- Can store None values.
- Sets are not inherently thread safe, so concurrent modifications may lead to unexpected behavior. 
- Internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time.


syntax: my_set = {item1, item2, item3}
"""

#Example 1: Creating a Set
my_set = {1, 2, 3, 4, 5}


#Example 2: Using the set() function
set1 = set()
print(set1)
# o/p: set()

set1 = set("Python")
print(set1)
# o/p: {'h', 'P', 'n', 'o', 't', 'y'} here order may vary as sets are unordered

# Creating a Set with the use of a List
set1 = set(["Python", "For", "ML"])
print(set1)
# o/p: {'ML', 'For', 'Python'} here order may vary as sets are unordered

# Creating a Set with the use of a tuple
tup = ("Python", "for", "ML")
print(set(tup))
# o/p: {'ML', 'for', 'Python'}

# Creating a Set with the use of a dictionary
d = {"Python": 1, "for": 2, "ML": 3}
print(set(d.keys()))
# o/p: {'ML', 'for', 'Python'} 


#Example 3: Adding elements to a Set
my_set = {1, 2, 3}
my_set.add(4)  # Adding a single element

print(my_set)  # Output: {1, 2, 3, 4}


#Example 4: Removing elements from a Set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # Removes 3 from the set
print(my_set)  # Output: {1, 2, 4, 5}


my_set = {1, 2, 3, 4, 5, 10}
my_set.discard(10)  # Removes 10 from the set if it exists, does nothing if it doesn't
print(my_set)  # Output: {1, 2, 3, 4, 5}


#Example 5: Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Union
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}



#Example 6: Set Methods
my_set = {1, 2, 3}
print(len(my_set))  # Output: 3
print(2 in my_set)  # Output: True
print(my_set)  # Output: {1, 2, 3}



#Example 7: Iterating through a Set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
# Output (order may vary):
# 1
# 2
# 3
# 4
# 5


#Example 8: Set Comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16} (order may vary)


# Example 9: Frozenset - Immutable version of a set
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})


#Example 10: Set Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_set = set1.difference(set2) # Elements in set1 but not in set2
difference_set2 = set1 - set2 # Another way to find difference
print(difference_set2)  # Output: {1, 2}
print(difference_set)  # Output: {1, 2}


