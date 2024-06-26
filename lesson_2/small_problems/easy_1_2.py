# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

def odd_numbers(collection):
    for i in collection:
        if i % 2 == 1:
            print(i)

odd_numbers(range(1, 100))

# Launch School Answer #
# for number in range(1, 100):
#     if number % 2 == 1:
#         print(number)

# def odd_numbers(collection):              <-- Attempt at bonus
#     return (collection[1, 100, 2])

# print(odd_numbers(list(range(1, 101))))