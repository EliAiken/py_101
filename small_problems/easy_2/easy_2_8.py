# Write a function that returns a list that contains every other element 
# of a list that is passed in as an argument. The values in the returned 
# list should be those values that are in the 1st, 3rd, 5th, and so on 
# elements of the argument list.

def oddities(lst):
    result = []
    for idx in range(len(lst)):
        if idx % 2 == 0:
            result.append(lst[idx])

    return result

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True