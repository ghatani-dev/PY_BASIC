"""
OSModule in Python

OS module in python provides functions for interacting with the operating system.
It allows you to perform operating system dependent functionality like reading or 
writing to the file system, managing processes, and handling system-specific parameters 
and functions.

Some commonly used functions in the OS module:
1. os.getcwd() - Returns the current working directory.
2. os.listdir(path) - Returns a list of files and directories in the specified path.
3. os.mkdir(path) - Creates a new directory at the specified path.
4. os.remove(path) - Deletes the file at the specified path.
5. os.rename(src, dst) - Renames a file or directory from src to dst.

What is Current Working Directory (CWD)?
The current working directory (CWD) is the directory in which a program or script is running
and not the path where the script is located.

Meaning if you run a script located in /home/user/scripts/ from /home/user/,
the CWD will be /home/user/ and not /home/user/scripts/.
"""


import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 



# Changing the current working directory

"""
os.chdir(path) is used to change the current working directory to the specified path.
"""

new_path = '/path/to/new/directory'  # Replace with your desired path
try:
    os.chdir(new_path)
    print("Directory changed successfully to:", os.getcwd())
except FileNotFoundError:
    print("Directory not found:", new_path)
except Exception as e:
    print("Error occurred while changing directory:", e)


# Creating a Directory

"""
os.mkdir(path) creates a new directory at the specified path.
os.makedirs(path) creates all intermediate-level directories needed to contain the leaf directory.


Meaning if you want to create /home/user/newdir/subdir/, os.makedirs() will create both newdir and subdir if they do not exist,
while os.mkdir() will only create subdir if newdir already exists.
"""


import os
directory = "ujjwal"
parent_dir = "E:/CPYTHON/PY_BASIC/"
path = os.path.join(parent_dir, directory) 
os.mkdir(path)
print("Directory '% s' created" % directory)
# the os.path.join() method is used to join one or more path components intelligently.
# so path will be E:/CPYTHON/PY_BASIC/ujjwal


directory = "singh"
parent_dir = "E:/CPYTHON/PY_BASIC/"
mode = 0o666 # octal value representing the permissions to be set on the new directory.
# do we have to give permission to read, write, execute?
# Yes, the mode 0o666 gives read and write permissions to the owner, group, and others.
# what if mode is not specified?
# If the mode is not specified, the default permissions are applied based on the system's
# umask settings.
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)



# Using os.makedirs() to create intermediate directories
import os
path = "E:/CPYTHON/PY_BASIC/ujjwal/singh"
os.makedirs(path)
print("Intermediate directories created at '% s'" % path)
# This will create both 'ujjwal' and 'singh' directories if they do not exist.



## Listing Files and Directories
"""
os.listdir(path) returns a list of all files and directories in the specified path.
"""

import os
path = "E:/CPYTHON/PY_BASIC/"
files_and_dirs = os.listdir(path)
print("Files and directories in '", path, "' :")
for item in files_and_dirs:
    print(" -", item)


## Deleting directory or files using pthon

"""
os.rmdir(path) removes (deletes) the directory at the specified path.
Note: The directory must be empty to be removed.
os.remove(path) removes (deletes) the file at the specified path.
"""

import os
dir_path = "E:/CPYTHON/PY_BASIC/ujjwal/singh"
try:
    os.rmdir(dir_path)
    print("Directory '% s' removed" % dir_path)
except OSError as e:
    print("Error: % s - % s." % (e.filename, e.strerror))
    print("Directory '% s' not removed" % dir_path)

file_path = "E:/CPYTHON/PY_BASIC/example.txt"
try:
    os.remove(file_path)
    print("File '% s' removed" % file_path)
except OSError as e:
    print("Error: % s - % s." % (e.filename, e.strerror))
    print("File '% s' not removed" % file_path)



# Note: Be cautious while using os.remove() and os.rmdir() as they permanently delete files and directories.


## File permission and metadata
""" 
os.stat(path) retrieves information about the specified file or directory,
including size, last modified time, and permissions.

os.chmod(path, mode) changes the permissions of the specified file or directory.

os.chown(path, uid, gid) changes the owner and group of the specified file or directory.
"""

import os
import stat
file_path = "E:/CPYTHON/PY_BASIC/example.txt"
try:
    file_stats = os.stat(file_path)
    print("File Size:", file_stats.st_size, "bytes")
    print("Last Modified:", file_stats.st_mtime)
    print("Permissions:", oct(file_stats.st_mode)[-3:])
except OSError as e:
    print("Error: % s - % s." % (e.filename, e.strerror))
# Note: Changing file ownership using os.chown() may require administrative privileges
# and is not available on all operating systems, such as Windows.

os.chmod(file_path, 0o600)
#0o600 means:
# Owner: read and write (6)
# Group: no permissions (0)
# Others: no permissions (0)


print("Permissions of file '% s' changed to 600" % file_path)



os.chown(file_path, 1000, 1000)
# Here, 1000 is an example user ID (uid) and group ID (gid).
# You should replace them with actual uid and gid values from your system.
print("Owner and group of file '% s' changed to uid:1000 and gid:1000" % file_path)

## Other os commonly used functions are
os.name  # Returns the name of the operating system dependent module imported.
os.sep   # Returns the character used by the operating system to separate pathname components.
os.path   # A sub-module that provides functions for manipulating filesystem paths.
os.rename(src, dst)  # Renames a file or directory from src to dst.
os.walk(top, topdown=True, onerror=None, followlinks=False)  # Generates the file names in a directory tree by walking the tree either top-down or bottom-up.
os.path.exists(path)  # Checks if a specified path exists.
os.path.getsize(path)  # Returns the size of the file at the specified path.
os.path.getmtime(path)  # Returns the last modified time of the file at the specified
