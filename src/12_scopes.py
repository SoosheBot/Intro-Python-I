# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x
    x = 99
    print("x is now: ", x) #local variable 
change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
#we have to add 'global x' inside the def change_x() function
print(x)


# This nested function has a similar problem.


def outer():
    y = 120
    # print("outer y: ", y)
    def inner():
        y = 999
        print("inner y: ", y)
    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? <---- we add a print y above the 'inner()'
    # Note: Google "python nested function scope".

outer()
