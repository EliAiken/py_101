# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print('Welcome to Calculator!')
print()
number1= int(input("What's the first number? "))
number2= int(input("What's the second number? "))
print()
print(f"Your selected numbers are: {number1} and {number2}")
print()
operation = int(input("What operation would you like to perform?\n"
                      "1 = Add | 2 = Subtract | 3 = Multiply | 4 = Divide\n"))
if operation == 1:      # 1 represents addition
    output = number1 + number2
elif operation == 2:    # 2 represents subtraction
    output = number1 - number2
elif operation == 3:    # 3 represents multiplication
    output = number1 * number2
elif operation == 4:    # 4 represents division
    output = number1 / number2
print()
print(f"The result is: {output}")