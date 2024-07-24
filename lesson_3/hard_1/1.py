# Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# My ANSWER: No. The first() function will return 'prop1': "hi there" and the
# second() function will return None as the return statement is on a different
# line than the dictionary. Thus the return statement in second() is returning
# None with the dictionary then being written on the next line down. Essentially,
# second() doesn't even do anything with the dictionary because the return statement
# terminates the program.

# LS ANSWER: 
# These functions do not return the same thing. The function first() returns the 
# expected value of { prop1: "hi there" }, but second() returns None without throwing 
# any errors.

# In Python, if there's nothing after a return statement, the function will return None. 
# The indented block after the return statement in second function is unreachable and 
# doesn't affect the return value.