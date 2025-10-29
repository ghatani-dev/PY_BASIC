"""
In Python, a string is a sequence of characters enclosed in quotes. 
It can include letters, numbers, symbols or spaces. 
Since Python has no separate character type, even a single character is treated as a string with length one. 
"""

#Example 1: Creating Strings
string1 = "Hello, World!"  # Double quotes
string2 = 'Hello, World!'  # Single quotes
print(string1)
print(string2)

#Example 2: Multi-line Strings
multi_line_string = """This is a
multi-line string."""
print(multi_line_string) #o/p: This is a
                        #     multi-line string.


#Example 3: Accessing Characters
sample_string = "Python"
print(sample_string[0])  # Output: P
print(sample_string[1])  # Output: y
print(sample_string[2])  # Output: t
print(sample_string[3])  # Output: h
print(sample_string[4])  # Output: o
print(sample_string[5])  # Output: n
# Strings are indexed starting from 0 from the left and -1 from the right.
# Note: Accessing an index out of range will cause an IndexError. 
# Only integers are allowed as indices and using a float or other types will result in a TypeError.



#Example 4: String Immutability
immutable_string = "Immutable"
# immutable_string[0] = 'i'  # This will raise a TypeError
# Strings cannot be changed after they are created.

#Example 5: String Concatenation
str1 = "Hello"
str2 = "World"
concatenated_string = str1 + ", " + str2 + "!"
print(concatenated_string)  # Output: Hello, World!

#Example 6: String Slicing
slice_string = "Hello, World!"
print(slice_string[0:5])  # Output: Hello, here 5 is the stopping index, not included
print(slice_string[7:12]) # Output: World, here 12 is the stopping index, not included
print(slice_string[:5])    # Output: Hello, from start to index 5 (not included)
print(slice_string[7:])    # Output: World!, from index 7 to end
print(slice_string[-6:])   # Output: World!, negative indexing


#Example 7: String Methods
text = "  Hello, World!  "
print(text.lower())        # Output: "  hello, world!  "
print(text.upper())        # Output: "  HELLO, WORLD!  "
print(text.strip())        # Output: "Hello, World!" (removes leading/trailing whitespace)
print(text.replace("World", "Python"))  # Output: "  Hello, Python!
print(text.split(","))     # Output: ['  Hello', ' World!  ']
print(text.find("World"))  # Output: 8 (index of first occurrence of "World")
print(text.count("o"))     # Output: 2 (number of occurrences of "o")
print(text.startswith("  He"))  # Output: True
print(text.endswith("!  "))      # Output: True
print("Length of text:", len(text))  # Output: Length of text: 17
# len() function returns the length of the string including spaces.

#Example 8: Escape Characters
escape_string = "He said, \"Hello, World!\"\nNew line starts here."
print(escape_string)
# Output: He said, "Hello, World!"
#         New line starts here. 

# Common escape characters include:
# \n : New line
# \t : Tab
# \\ : Backslash
# \' : Single quote
# \" : Double quote
# \r : Carriage return
# \b : Backspace


#Example 9: Raw Strings
raw_string = r"C:\Users\Name\Documents" # here 'r' before the string indicates a raw string
print(raw_string)
# Output: C:\Users\Name\Documents
# Raw strings treat backslashes as literal characters and do not interpret them as escape characters.

#Example 10: String Formatting
name = "Alice"
age = 30
formatted_string1 = "My name is {} and I am {} years old.".format(name, age)
formatted_string2 = f"My name is {name} and I am {age} years old."
print(formatted_string1)  # Output: My name is Alice and I am 30 years old.
print(formatted_string2)  # Output: My name is Alice and I am 30 years old.


#Example 11: String Membership
membership_string = "Hello, World!"
print("Hello" in membership_string)  # Output: True
print("World" in membership_string)  # Output: True
print("Python" in membership_string)  # Output: False

# The 'in' keyword checks if a substring exists within a string and returns a boolean value.

#Example 12: Iterating Through a String
iterate_string = "Python"
for char in iterate_string:
    print(char)
# Output:
# P 
# y
# t
# h
# o
# n
# You can loop through each character in a string using a for loop.


#Example 13: String Comparison
str_a = "apple"
str_b = "banana"
print(str_a == str_b)  # Output: False
print(str_a < str_b)   # Output: True (lexicographical comparison) means 'a' comes before 'b'
print(str_a > str_b)   # Output: False (lexicographical comparison)
# Strings can be compared using comparison operators like ==, !=, <, >, <=, >= based on lexicographical order.


#Example 14: Joining Strings
words = ["Hello", "World", "from", "Python"]
joined_string = " ".join(words)
print(joined_string)  # Output: Hello World from Python


# The join() method concatenates a list of strings into a single string with a specified separator (in this case, a space).

#Example 15: Repeating Strings
repeat_string = "Ha! " * 3
print(repeat_string)  # Output: Ha! Ha! Ha!
# The * operator can be used to repeat a string multiple times.

#Example 16: Converting Other Data Types to Strings
num = 100
float_num = 99.99
boolean_value = True
str_num = str(num) # here str() function converts other data types to string
str_float = str(float_num)
str_bool = str(boolean_value)
print(str_num)    # Output: "100"
print(str_float)  # Output: "99.99"
print(str_bool)   # Output: "True"


# The str() function is used to convert other data types (like int, float, bool) to strings.


#Example 17: String Encoding and Decoding
original_string = "Hello, World!"
encoded_string = original_string.encode("utf-8")  # Encoding to bytes
decoded_string = encoded_string.decode("utf-8")   # Decoding back to string

print("Original String:", original_string)
print("Encoded String:", encoded_string)
print("Decoded String:", decoded_string)
# Output:
# Original String: Hello, World!
# Encoded String: b'Hello, World!'
# Decoded String: Hello, World!


# Strings can be encoded to bytes and decoded back to strings using the encode() and decode() methods respectively.


#Example 18: String Formatting with Percentage Operator
name = "Bob"
age = 25
place = "Japan"
formatted_string = "My name is %s and I am %d years old from %s." % (name, age, place)
print(formatted_string)  # Output: My name is Bob and I am 25 years old from Japan.
# The % operator can be used for string formatting, where %s is a placeholder for strings and %d is a placeholder for integers.



#Example 19: Finding Substrings
main_string = "Hello, welcome to the world of Python programming."
substring = "Python"
index = main_string.find(substring) # Returns the starting index of the substring or -1 if not found
print("Substring found at index:", index)  # Output: Substring found at index: 30

# The find() method is used to locate the position of a substring within a string. It returns the index of the first occurrence or -1 if not found.



#Example 20: String Justification
text = "Hello"
left_justified = text.ljust(10, '-')   # Left justify with '-' padding
right_justified = text.rjust(10, '*')  # Right justify with '*'
centered = text.center(10, '=')         # Center with '=' padding
print("Left Justified:", left_justified)     # Output: Left Justified:
print("Right Justified:", right_justified)   # Output: Right Justified: *****Hello
print("Centered:", centered)                 # Output: Centered: ==Hello===
# The ljust(), rjust(), and center() methods are used to justify strings with specified padding characters.