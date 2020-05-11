"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

#MY NOTES -- r, w --> read, write. .close() closes the file, 'with open() as __' opens the file

# YOUR CODE HERE
# Code for printing to a file 
with open('/Users/Mahadevi/Documents/CS7/python1/Intro-Python-I/src/foo.txt', 'r') as file:
    print(file.read())
    file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('/Users/Mahadevi/Documents/CS7/python1/Intro-Python-I/src/foo.txt', 'w') as file:
    print(file.write('We demand...a SHRUBBERY'))
    file.close()

with open('/Users/Mahadevi/Documents/CS7/python1/Intro-Python-I/src/foo.txt', 'r') as file:
    print(file.read())
    file.close()