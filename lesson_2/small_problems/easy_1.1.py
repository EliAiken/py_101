def is_it_odd(number):
    if abs(number) % 2 == 0:
        return False
    else:
        return True
    
# Test Cases #    
print(is_it_odd(2))
print(is_it_odd(3))