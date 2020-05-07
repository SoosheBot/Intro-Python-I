"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
b = slice(1,2)
print("Prints 4: ", a[b])

# Output the second-to-last element: 9
c = slice(4,5)
print("Prints 9: ", a[c])

# Output the last three elements in the array: [7, 9, 6]
d = slice(3,6)
print("Prints 7,9,6: ", a[d])

# Output the two middle elements in the array: [1, 7]
e = slice(2,4)
print("Prints 1,7: ", a[e])

# Output every element except the first one: [4, 1, 7, 9, 6]
print("Prints 4,1,7,9,6: ", a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print("Prints 2,4,1,7,9: ", a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
x = slice(7,12)
print("Prints 'world': ", s[x])