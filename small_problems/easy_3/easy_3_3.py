# Write a function that takes a short line of text and prints it within a box.

def print_in_box(text):
    print(f"""
+--------------------------------------------+
|                                            |
|                   {text}                    |
|                                            |
+--------------------------------------------+
""")
    
print_in_box('hello')

# LS ANSWER:

def print_in_box(message):
    horizontal_rule = f'+-{"-" * len(message)}-+'
    empty_line = f'| {" " * len(message)} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)

print_in_box('To boldly go where no one has gone before.')

# 1. len(message) returns the length of the message we want to print.
# 2. "-" * len(message) returns a string of N hyphens, where N is the 
# the length of the message we want to print.
# 3. We then prepend +- to the beginning of the hyphens.
# 4. Finally, we append -+ to the end of the hyphens.

# In Python, the * operator is used for multiplication when working 
# with numbers. However, when used with strings, it repeats a string 
# a given number of times.