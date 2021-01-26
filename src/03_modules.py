"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# NOTE -- `sys.argv` is the list of commandline arguments passed to the Python program. argv represents all the items that come along via the command line input, it's basically an array holding the command line arguments of our program. 

# Print out the OS platform you're using:
# YOUR CODE HERE
print("OS Platform: ", sys.platform.capitalize())

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python version: ", sys.version[0:5])

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("OS Process ID: ", os.getpgid(0))

# Print the current working directory (cwd):
# YOUR CODE HERE
print("OS CWD: ", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("Machine Login Name: ", os.getlogin())