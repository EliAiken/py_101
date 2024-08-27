# The or operator returns a truthy value if either or both of its 
# operands are truthy, a falsy value if both operands are falsy. The 
# and operator returns a truthy value if both of its operands are truthy, 
# and a falsy value if either operand is falsy. This works great 
# until you need only one of two conditions to be truthy, the so-called 
# exclusive or, also known as xor (pronounced "ECKS-or").

def xor(value1, value2):
    if (value1 and not value2) or (value2 and not value1):
        return True
    else:
        return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)