"""
Dictionary in python is a collection of key-value pairs. 

- Keys are case sensitive which means same name but different cases of Key will be treated distinctly.
- Keys must be immutable which means keys can be strings, numbers or tuples but not lists.
- Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
- Internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time.
- From Python 3.7 Version onward, Python dictionary are Ordered.


syntax:my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
"""

"""
=> Why must dictionary keys be immutable?
In Python, dictionary keys are used internally in a hashing mechanism to quickly find values.
 For this to work:
    1. Keys must not change after being created.
    2. If a key changed, Python wouldn’t be able to find the value again 
       (because its hash would change).


Therefore, only immutable (unchangeable) types like:

✔ str (string)
✔ int / float (numbers)
✔ tuple (only if it contains immutable elements)

can be used as dictionary keys.


1️⃣ How Python Dictionary Works Internally

Python dictionaries are implemented using a hash table:

    1. Each key is hashed using hash(key) → produces an integer called the hash value.

    2. This hash value determines the bucket in memory where the value will be stored.

    3. To retrieve a value, Python calculates hash(key) again and looks up the bucket.

2️⃣ Why Immutability Matters

    1. If a key changes after insertion, its hash value changes.

    2. Python cannot find the value anymore, because it will look in the wrong bucket.

    3. Mutable objects like lists can be changed, so their hash would be unreliable → not allowed.

_________________________________________   

my_dict = {"name": "Alice", "age": 25, "city": "LA"}

Step 1 — Hash Calculation

Key 	Hash Value (example)
"name"	12345
"age"	67890
"city"	13579
________________________________________

Step 2 — Bucket Index (mod table_size)
Assume table_size = 10(size managed internally, initially small(8) and grows as needed). 
syntax:bucket_index = hash(key) % table_size

Key   	Hash Value	Bucket Index
"name"	12345	    5
"age"	67890	    0
"city"	13579	    9
________________________________________

Step 3 — Hash Table Layout

Index | Key     | Value
------------------------
  0   | "age"   | 25
  1   | None    | None
  2   | None    | None
  3   | None    | None
  4   | None    | None
  5   | "name"  | "Alice"
  6   | None    | None
  7   | None    | None
  8   | None    | None
  9   | "city"  | "LA"

________________________________________

Step 4 — Storing Values
In the hash table (buckets), the key-value pairs are stored as follows:

Bucket Index | Key       | Value
-----------------------------------
      0      | "age"    | 25
      5      | "name"   | "Alice"
      9      | "city"   | "LA"


_________________________________________

Bucket storage vs Iteration order

Buckets (hash table):

    1. Used for lookup efficiency.
    2. Keys are stored in buckets based on hash(key) % table_size.
    3. Bucket index is unrelated to insertion order.
    4. Python maintains a separate order table internally for iteration.
    5. This keeps keys in the order they were inserted.
    6. So, even if "age" is in bucket 0 and "name" in bucket 5, iterating the dictionary gives:
            for key in my_dict:
                    print(key)
            Output:
            name
            age
            city
__________________________________________

Why Python separates the two
    1. Lookup: Fast access via hash table → bucket indices matter
        (Bucket order = internal storage for speed → not visible externally)
    2. Iteration: Maintain user-expected order → insertion order table 
        (Iteration order = matches insertion → what you see when you loop through .keys() or .items())
"""

#Example 1: Creating a Dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


#Example 2: Using dict() Constructor
my_dict = dict(name="Bob", age=25, city="Los Angeles")
print(my_dict)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}


#Example 3: Accessing Values
print(my_dict["name"])  # Output: Bob
print(my_dict.get("age"))  # Output: 25
print(my_dict.get("country", "USA"))  # Output: USA (default value), here key doesn't exist but it returns default value.
print(my_dict.get("country"))  # Output: None (key doesn't exist)
print(my_dict["country"])  # Raises KeyError (key doesn't exist)

#Example 4: Adding or Updating Key-Value Pairs
my_dict["age"] = 26  # Update existing key
my_dict["country"] = "USA"  # Add new key-value pair
print(my_dict)  # Output: {'name': 'Bob', 'age': 26, 'city': 'Los Angeles', 'country': 'USA'}


#Example 5: Removing Key-Value Pairs
del my_dict["city"]  # Remove key-value pair by key
print(my_dict)  # Output: {'name': 'Bob', 'age': 26, 'country': 'USA'}

removed_value = my_dict.pop("age")  # Remove key-value pair and return the value
print(removed_value)  # Output: 26

print(my_dict)  # Output: {'name': 'Bob', 'country': 'USA'}

#Example 6: Iterating Through a Dictionary
for key in my_dict: # Iterating through keys
    print(key, my_dict[key])
# Output:
# name Bob
# country USA
for key, value in my_dict.items(): # Iterating through key-value pairs
    print(key, value)
# Output:
# name Bob
# country USA   


#Example 7: Dictionary Methods
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'country'])
values = my_dict.values()
print(values)  # Output: dict_values(['Bob', 'USA'])
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Bob'), ('country', 'USA')])


#Example 8: Nested Dictionaries
nested_dict = {
    "person": {
        "name": "Charlie",
        "age": 35
    },
    "location": {
        "city": "Chicago",
        "state": "Illinois"
    }
}
print(nested_dict)
# Output: {'person': {'name': 'Charlie', 'age': 35}, 'location': {'city': 'Chicago', 'state': 'Illinois'}}
print(nested_dict["person"]["name"])  # Output: Charlie
print(nested_dict["location"]["city"])  # Output: Chicago

#Example 9: Dictionary Comprehension, meaning creating dictionaries using a single line of code.
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


#Example 10: Merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  # Merges dict2 into dict1, overwriting existing keys
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

#Example 11: Checking if a Key Exists
print("a" in dict1)  # Output: True
print("d" in dict1)  # Output: False
print("f" not in dict1)  # Output: True


#Example 12: Clearing a Dictionary
dict1.clear()
print(dict1)  # Output: {}


#Example 13: Copying a Dictionary
original_dict = {"x": 10, "y": 20}
# Here .copy() is a shallow copy, not deep. A shallow copy means constructing a new compound object and then
# (to the extent possible) inserting references into it to the objects found in the original.
copied_dict = original_dict.copy() 
print(copied_dict)  # Output: {'x': 10, 'y': 20}
# Here, copied_dict doesn't create a new dictionary, both copied_dict and original_dict point 
# to the same object in memory. Any changes in one will affect the other.
copied_dict = original_dict 
print(copied_dict is original_dict)  # Output: False 


#Example 14: using tuples as Dictionary Keys
tuple_key_dict = {(1, 2): "Point A", (3, 4): "Point B"}
print(tuple_key_dict)  # Output: {(1, 2): 'Point A', (3, 4): 'Point B'}
print(tuple_key_dict[(1, 2)])  # Output: Point A
#----------------------
tup = {} 
tup[(1,2,4)] = 8
tup[(4,2,1)] = 10
tup[(1,2)] = 12
sum1 = 0
for k in tup: 
    sum1 += tup[k] 
print(len(tup) + sum1)
# Output: 33

#Dictonary will look like this:
#{
#  (1, 2, 4): 8,
#  (4, 2, 1): 10,
#  (1, 2): 12
#}