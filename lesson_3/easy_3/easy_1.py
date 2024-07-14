# Write two different ways to remove all of the elements from the following list:

numbers = [1, 2, 3, 4]

numbers.clear()

print(numbers)

# LS ANSWER:
numbers.clear()

# OR

while numbers:
   numbers.pop()

# Note that the following solution will set numbers to an 
# empty list, but it doesn't clear the original list. That's 
# fine if you know there are no other references to the list.

#       numbers = []