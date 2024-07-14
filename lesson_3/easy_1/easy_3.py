# Starting with the string:
# Show two different ways to create a new string with 
# "Four score and " prepended to the front of the string.

# 1.
famous_words = "seven years ago..."

other_famous_words = "Four score and "

quote_1 = other_famous_words + famous_words

print(quote_1)

# 2.
a = other_famous_words.split()
b = famous_words.split()

c = " ".join(a + b)

print(c)

# LS ANSWER:
new_string = "Four score and " + famous_words
new_string = f"Four score and {famous_words}"