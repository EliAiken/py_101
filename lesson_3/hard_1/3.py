# Given the following similar sets of code, what will each code snippet print?

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# ------------------------------------------------------------------------------- #

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# ------------------------------------------------------------------------------- #

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# LS ANSWER:
# In all three scenarios, the variables one, two, and three inside the 
# mess_with_vars function are local to the function. They are not the 
# same as the variables one, two, and three defined outside the function. 
# This is known as variable shadowing, where the local variables inside the 
# function overshadow the variables outside the function with the same names.

# A) Since variables one, two, and three in the mess_with_vars function are local, 
# reassigning them does not affect the original lists.

# B) Again, the local variables in the mess_with_vars function are being reassigned, 
# but this doesn't change the original lists. 

# C) In this case, the mess_with_vars function modifies the content of the lists directly. 
# Since lists in Python are mutable and passed by reference, the changes are reflected 
# outside the function.
# Output:
    # one is: ['two']
    # two is: ['three']
    # three is: ['one']