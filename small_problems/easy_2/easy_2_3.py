# Create a function that takes two arguments, multiplies them together, 
# and returns the result.

def multiply(num1, num2):
    return (int(num1) * int(num2))      # My function can accept integers
                                        # or strings and get an appropriate
print(multiply(5, 3) == 15)             # result.
print(multiply('5', '10') == 50)

# LS ANSWER:

def multiply(num1, num2):
    return num1 * num2