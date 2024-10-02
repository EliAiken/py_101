# count is a good method example that does not mutate the code

# ------------------------------------------------------------ #

# Pass-by-Value: 
# You're passing a copy of the object into the function so you can do
# whatever you want to it inside the function & it won't affect the original.

# The function only gets a copy of the object
# What you do inside the function, doesn't affect the original object

# Pass-by-Reference: 
# You're passing the object directly into the function. If you do something
# to the object inside the function, it will also change the original object
# that was passed in.

# You take the object and you give it to the function
# The object itself if being given to the function

# Pass-by-OBJECT-REFERENCE (what Python uses):
# It's always the REFERENCE to an object that is passed in
# in Python. But whether the original object passed in can be changed depends 
# on the mutability of the object passed in.

# In python, it matters what your object IS vs in other languages what your
# object DOES. (Mutable vs Immutable)

# ------------------------------------------------------------ #

# mutable ----> we CAN change --> Python gets a reference to the physical 
# address in memory
# immutable --> we CANNOT change

# ------------------------------------------------------------ #

# if the assessment is using mutable data types, look out for where the
# data is being mutated

# ------------------------------------------------------------ #

# casefold is like an international version of string.lower() method

# ------------------------------------------------------------ #

# when working with immutable data type like strings, you need to look at
# what kind of operators you are using on it (mutating vs non-mutating)
# `+=` is a mutating operation | `+` is not a mutating data type

# ------------------------------------------------------------ #

# Look Before You Leap:
# ???

# Better to ask for forgiveness than permission:
# Writing code that will have an error, but then it just deals with the error
# Example: Try/Except blocks

food_types = { 
             'protein': 'chicken',
             'carbohydrate': 'bread',
             'vegetable': 'carrot'
             }
try:
    print(food_types['fats'])
except KeyError:
    print('better error message')

print(food_types.get('fats', 'error message'))

# ------------------------------------------------------------ #

# When working with reassignment within a function, if a variable is not already initialized,
# then reassignment will throw an UnboundLocalError. The reason this happens is because even
# though a local variable could utilize a variable of the same name in the global scope, you
# cannot alter or reassign a local variable of the same name without using the `global` keyword
# first. Python will read the reassignment of the variable on the right side of the reassignment
# (the = sign) first and it will be unable to find the variable in the local scope. Thus the 
# error will be thrown:

x = 10

def my_function():
    x = x + 5   # UnboundLocalError; Python tried to find x but it was not assigned yet
    print(x)

my_function()   

# ------------------------------------------------------------ #
