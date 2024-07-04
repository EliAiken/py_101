# Program receives input from user for integer greater than 0
# Program asks user if they want to print sum or product of 
# all numbers between 1 and provided integer, inclusive

def compute_sum(number):
    return sum(range(1, number + 1))

def compute_product(number):
    result = 1
    for num in range(1, number + 1):
        result *= num
    return result

print("Please enter an integer greater than 0:")
prompt_1 = int(input())

print("Enter 's' to compute the sum, or 'p' to compute the product.")
prompt_2 = input()

if prompt_2 == 's':
    print(f"The sum of the integers between 1 and {prompt_1} "
      f"is {compute_sum(prompt_1)}.")
elif prompt_2 == 'p':
    print(f"The product of the integers between 1 and {prompt_1} "
      f"is {compute_product(prompt_1)}.")