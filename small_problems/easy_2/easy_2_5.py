# Write a program that prompts the user for two positive numbers 
# (floating-point), then prints the results of the following operations 
# on those two numbers: addition, subtraction, product, quotient, floor 
# quotient, remainder, and power. Do not worry about validating the input.

def prompt(words):
    print(f' ==> {words}')

def compute(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '//':
            return num1 // num2
        case '%':
            return num1 % num2
        case '**':
            return num1 ** num2
        
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f'{num1} {operator} {num2}'
    result = compute(num1, num2, operator)
    prompt(f'{operation} = {result}')