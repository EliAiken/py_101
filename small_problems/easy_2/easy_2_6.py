# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.

def penultimate(words):
    word_list = words.split(' ')
    return word_list[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

# LS ANSWER:
def penultimate(words):
    words_list = words.split()
    return words_list[-2]