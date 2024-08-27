# Write a function that takes a number as an argument. If the argument 
# is a positive number, return the negative of that number. If the 
# argument is a negative number, return it as-is.

def negative(number):
    if number <= 0:
        return number
    else:
        return number // -1   # I originally put -abs(number) as my answer for this line

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

print(negative(5))      # True


# LS ANSWER:

def negative(number):
    return -abs(number)