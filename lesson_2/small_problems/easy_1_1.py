# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def is_it_odd(number):
    if abs(number) % 2 == 0:
        return False
    else:
        return True
    
# Test Cases #    
print(is_it_odd(2))
print(is_it_odd(3))