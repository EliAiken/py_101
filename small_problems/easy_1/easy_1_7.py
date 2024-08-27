# Function takes 2 strings as arguments
# Function determines length of the 2 strings
# Function concatenates strings in this order:
# shorter + longer + shorter

def short_long_short(str_1, str_2):
    if len(str_1) < len(str_2):
        return str_1 + str_2 + str_1
    else:
        return str_2 + str_1 + str_2

print(short_long_short('hello', 'bye'))
print(short_long_short('the', 'gorilla'))