# Write a function that takes one argument, a positive integer, and 
# returns a string of alternating '1's and '0's, always starting with 
# a '1'. The length of the string should match the given integer.

def stringy(num):
    result = ""
    for idx in range(num):
        digit = '1' if idx % 2 == 0 else '0'
        result += digit

    return result


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

print(stringy(7))

# LS ANSWER:

# The solution makes use of a for loop in combination with range to 
# loop the specified number of times. At every iteration of the loop, 
# the solution checks whether the index position is even. If so, the 
# solution appends a '1' to the initially empty result string. Otherwise, 
# it appends '0'.

# number = '1' if idx % 2 == 0 else '0'

# is equivalent to:

# if idx % 2 == 0:
#     number = '1'
# else:
#     number = '0'