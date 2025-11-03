"""
File Handling in Python
-----------------------

File handling refers to the process of performing operations
on a file, such as creating, opening, reading, writing and closing (CORWC)
it through programming interface.

It involves managing the data flow between the program and the file system
on the storage device, ensuring that data is handled efficiently and securely.


Why do we need file handling?
1. To store data permanently, even after the program ends.
2. To access external files like .txt., .csv, .json, etc. for data processing.
3. To automate tasks like reading configs or saving outputs.
4. To handle input/output in real world applications and tools.
5. To process large files efficiently without loading everything into memory.
"""

# Opening a file
file = open('example.txt', 'mode')  

# mode is which you want to perform operations like 'r', 'w', 'a', etc.
#If we don't specify mode, it opens in 'r' read mode by default.


# Reading from a file
file = open('example.txt', 'r')  # Opens the file in read mode  
content = file.read()  # Reads the entire file content
line = file.readline()  # Reads a single line from the file
lines = file.readlines()  # Reads all lines into a list


# Closing a file'
file = open('example.txt', 'r')
content = file.read()
file.close()  # Closes the file to free up resources


# Checking file properties
import os
file_path = 'example.txt'
if os.path.exists(file_path):
    print("File exists")
    print("File size:", os.path.getsize(file_path), "bytes")
    print("Last modified:", os.path.getmtime(file_path))
else:
    print("File does not exist")

#o/p:
#File exists
#File size: 1234 bytes
#Last modified: 1625247600.0



# Writing to a file
file = open('example.txt', 'w')  # Opens the file in write mode
file.write("Hello, World!\n")  # Writes a string to the file
file.close()  # Closes the file to free up resources


# using 'with' statement for file handling
# Instead of manually opening and closing files,
# we can use the 'with' statement which automatically handles closing the file.
# This reduces the risk of file corruption and resource leakages.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


# o/p:
# Hello, World!


# Appending to a file
with open('example.txt', 'a') as file:  # Opens the file in append mode
    file.write("Appending a new line.\n")  # Appends a new line to the file
# The file is automatically closed after the with block ends

# Deleting a file
import os
file_path = 'example.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully")
else:
    print("File does not exist")
# o/p:
# File deleted successfully