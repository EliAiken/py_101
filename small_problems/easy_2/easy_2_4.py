# Using the multiply function from the "Multiplying Two Numbers" 
# exercise, write a function that computes the square of its argument 
# (the square is the result of multiplying a number by itself).

def multiply(num1, num2):
    return num1 * num2

def square(number):
    return multiply(number, number)

print(square(5) == 25)
print(square(-8) == 64)


def power(base, exponent):
    result = 1
    for i in range(exponent):
        result = multiply(result, base)

    return result

print(power(2, 3) == 8)

# LS ANSWER:

def multiply(num1, num2):
    return num1 * num2

def square(number):
    return multiply(number, number)

# Our implementation relies on the previous exercise's multiply function. 
# The return value of multiply is the result of multiplying the arguments 
# together, so we just pass it the same number twice. The result is the 
# squared value.