# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))

# MY ANSWER: This will print True as the nan_value variable is equal 
# to the value of float("nan").

# LS ANSWER: The output is False. nan -- not a number -- is a special 
# numeric value that indicates that an operation that was intended to 
# return a number failed. Python doesn't let you use == to determine 
# whether a value is nan.

# Bonus Question

# How can you reliably test if a value is nan?

# To test whether the value is nan, you can use the math.isnan() function

import math

nan_value = float("nan")

print(math.isnan(nan_value))