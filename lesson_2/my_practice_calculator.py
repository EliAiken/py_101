# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)         # <-- Bug in the code, don't know how to make this
    except ValueError:          # work with the function
        return True
    
    return False

prompt('Welcome to Calculator!')
print()
number1= int(input("What's the first number? "))
while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1= int(input("What's the first number? "))
number2= int(input("What's the second number? "))
while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2= int(input("What's the second number? "))
print()
prompt(f"Your selected numbers are: {number1} and {number2}")
print()
operation = int(input("What operation would you like to perform?\n"
                      "1 = Add | 2 = Subtract | 3 = Multiply | 4 = Divide\n"))
while operation not in [1, 2, 3, 4]:
    prompt('You must choose 1, 2, 3, or 4')
    operation = int(input("What operation would you like to perform?\n"
                      "1 = Add | 2 = Subtract | 3 = Multiply | 4 = Divide\n"))
match operation:
    case 1:
        output = number1 + number2
    case 2:
        output = number1 - number2
    case 3:
        output = number1 * number2
    case 4:
        output = number1 / number2

print()
prompt(f"The result is: {output}")