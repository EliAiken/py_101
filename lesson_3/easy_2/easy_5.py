# How would you verify whether the data structures assigned to 
# the variables numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers))
print(type(table))

# LS ANSWER:
# Main answer:
isinstance(numbers, list)  # True
isinstance(table, list)    # False

# This works too, but has potential issues:
type(numbers) is list      # True
type(table) is list        # False