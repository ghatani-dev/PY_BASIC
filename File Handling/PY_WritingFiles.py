"""
Writing Files in Python
-----------------------

Writing to a file means saving data produced by your program so it can be accessed
even after the program finishes running.


Modes for Writing Files:
1. 'w' - Write mode: Opens a file for writing. If the file already exists,
   it will be overwritten. If it doesn't exist, a new file will be created.
2. 'a' - Append mode: Opens a file for writing, but does not overwrite
   existing content. New data is added to the end of the file.
3. 'x' - Exclusive creation mode: Creates a new file, but fails with FileExistsError if the
   file already exists.
4. 'b' - Binary mode: Used in conjunction with other modes (like 'wb' or 'ab')
   to write binary data (like images or audio files).
5. 't' - Text mode: Default mode for writing text files (like 'wt' or 'at').
6. '+' - Update mode: Opens a file for both reading and writing (like 'r+' or 'w+').
7. encoding - Specifies the encoding when writing text files (like encoding='utf-8').
8. newline - Controls how newlines are handled in text files (like newline='\n' or newline='\r\n').

"""


# Overwrite an existing file
with open('example.txt', 'w', encoding='utf-8') as file:  # 'w' mode for writing
    file.write("Created using write mode.\n")
    file.write("Second Line.\n")

with open ('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
# o/p: example.txt now contains "Created using write mode.
#       Second Line."



# Append to an existing file
with open('example.txt', 'a', encoding='utf-8') as file:  # 'a' mode for appending
    file.write("Appended Line 1.\n")
    file.write("Appended Line 2.\n")

with open ('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
# o/p: example.txt now contains "Created using write mode.
#       Second Line.
#       Appended Line 1.
#       Appended Line 2."


# Create only if it does not exist
try:
    with open('newfile.txt', 'x', encoding='utf-8') as file:  # 'x' mode for exclusive creation
        file.write("This file was created using exclusive creation mode.\n")
except FileExistsError:
    print("File 'newfile.txt' already exists.")


with open ('newfile.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
# o/p: If newfile.txt did not exist, it now contains
#       "This file was created using exclusive creation mode."


# Writing multiple lines
# Sometimes you need to write several lines at once instead of one by one. 
# Python provides two common approaches: writelines() for lists of strings and join() 
# for building a single text block.
with open('example.txt', 'w', encoding='utf-8') as file:  # 'w' mode for writing
    file.writelines([
        "Line 1: Created using writelines.\n",
        "Line 2: Another line.\n",
        "Line 3: Yet another line.\n"
    ])

with open ('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
# o/p: example.txt now contains "Line 1: Created using writelines.
#       Line 2: Another line.
#       Line 3: Yet another line.".

# Explanation: writelines() writes each string in the list directly. 
# It does not add newlines automatically you must include \n in each string yourself.

# Writing using join() method: join + single write (often cleaner)
lines = [   
            "Join Line 1",
            "Join Line 2",
            "Join Line 3"
        ]

with open('example.txt', 'w', encoding='utf-8') as file:  # 'w' mode for writing
    file.write("\n".join(lines) + "\n")

with open ('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
# o/p: example.txt now contains "Join Line 1
#       Join Line 2
#       Join Line 3