# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

print(list(reversed(numbers)))
print(numbers[::-1])

# LS ANSWER:
reversed_numbers = numbers[::-1]
reversed_numbers = list(reversed(numbers))