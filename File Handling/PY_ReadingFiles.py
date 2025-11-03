"""
Reading files in python:

Reading from a file in python means accessing and retrieving
contents of a file, weather it be text, binary or formats like CSV, JSON etc.

"""

#Reading a file line by line using with statement
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes leading/trailing whitespace
# o/p:  Hello, World!


#Reading a file line by line using for loop
file = open('example.txt', 'r')
for line in file:
    print(line.strip())
file.close()  # Closes the file
# o/p:  Hello, World!


#Reading a file using readline() method
file = open('example.txt', 'r') 
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
file.close()  # Closes the file
# o/p:  Hello, World!



""" 
readline() vs reading file line by line if for loop of using with statement:

1. Memory Efficiency:
   - Using a for loop or 'with' statement reads one line at a time,
        making it more memory efficient for large files.
    - readline() also reads one line at a time, but requires
        explicit loop control, which can be less efficient in terms of code readability.
2. Code Simplicity:
   - The 'with' statement and for loop provide cleaner and more concise code.
    - readline() requires more boilerplate code to manage the loop and file closing.
3. Automatic Resource Management:
   - The 'with' statement automatically handles file closing,
        reducing the risk of file corruption or resource leaks.
    - When using readline(), you must remember to close the file manually.
4. Use Cases:
   - For simple tasks or small files, readline() can be sufficient.
    - For larger files or more complex file processing,
         using a for loop or 'with' statement is generally preferred.

"""


#Reading Binary files
with open('example_image.png', 'rb') as file: #here 'rb' stands for read binary mode
    binary_content = file.read()
    print(f"Read {len(binary_content)} bytes from the binary file.")

# Explanation: This code reads a file in binary mode ("rb") 
# and prints its content as bytes, which is necessary for handling non-text files.



# Reading specific parts of file: Sometimes, we may only need to read a 
# specific part of a file, such as the first few bytes, a specific line, 
# or a range of lines.
with open('example.txt', 'r') as file:
    part = file.read(10)  # Reads only the first 10 characters
    print(part)

# Explanation: Reading a limited number of characters is useful for quickly 
# previewing content without loading the whole file.


#Reading CSV files

# Create a CSV sample in memory
csv_data = """Year,Industry,Value
2014,Manufacturing,769400
2014,Manufacturing,48000
2014,Manufacturing,12000"""


import csv
import io
csvfile = io.StringIO(csv_data) # StringIO is used to simulate a file object, why because csv.reader expects a file-like object
csvreader = csv.reader(csvfile) #here csv.reader is the method that reads the CSV file
for row in csvreader:
    print(row)
# Explanation: This code uses the csv module to read a CSV file,
# printing each row as a list of values.



# Reading JSON files
import json
json_data = '''
{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
'''
json_object = json.loads(json_data)
print(json_object)
# Explanation: This code uses the json module to parse a JSON string,
# converting it into a Python dictionary.