# What do you expect to happen when the greeting variable is referenced 
# in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

# MY ANSWER: It will throw an error because the if statement has to be False
# for the variable `greeting` to be assigned to "hello world", but it will be True
# in the case of this program. Thus, the call to print(greeting) will not have a
# defined variable to print and will raise the error.

# LS ANSWER:
# In Python, referencing an uninitialized variable will result in a NameError being 
# raised. This is because the if block is not executed due to the False condition, 
# and hence, the greeting variable is never initialized.