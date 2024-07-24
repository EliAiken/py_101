# What will the following two lines of code output?

print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)

# MY ANSWER: The first line will print the float 0.9. The second line
# will print True as the sum 0.3 + 0.6 = 0.9 which is the equivalent value
# of 0.9 >> 0.9 == 0.9 yields True.

# LS ANSWER: If you thought that the outputs would be 0.9 and True, 
# respectively, you were wrong. Python uses floating point numbers 
# for all numeric operations. Most floating point representations 
# used on computers lack a certain amount of precision, and that can 
# yield unexpected results like these.

0.8999999999999999
False

# One way around the problem is to use the math.isclose function:

import math

print(0.3 + 0.6)
print(math.isclose(0.3 + 0.6, 0.9))