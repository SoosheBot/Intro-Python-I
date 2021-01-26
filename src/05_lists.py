# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
(x.append(4))
print("Change: ", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print("Add y list to x list: ", x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print("Add items from 1st-3rd index in y list to x list: ", x + y[1:3])

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
y.insert(2, 99)
print("99: ", x + y[1:4])

# Print the length of list x
# YOUR CODE HERE
print("Length: ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print("Times 1000: ", [num * 1000 for num in x])