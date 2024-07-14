# How can you determine whether a given string ends with an exclamation mark (!)? 
# Write some code that prints True or False depending on whether the string ends 
# with an exclamation mark.

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def string_true(string):
    if string.endswith("!"):
        return True
    else:
        return False
    
print(string_true(str1))
print(string_true(str2))


# LS ANSWER:
print(str1.endswith("!"))  # True
print(str2.endswith("!"))  # False