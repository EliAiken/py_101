# Print a new version of the sentence given by advice that ends just 
# before the word house. Don't worry about spaces or punctuation: 
# remove everything starting from the beginning of house to the end of the sentence.

# Expected output:
# Few things in life are as important as

advice = "Few things in life are as important as house training your pet dinosaur."

list_advice = advice.split()

print(" ".join(list_advice[0:8]))

# LS ANSWER:
print(advice.split("house")[0])
# ^^ This splits advice into 2 strings within a list, then it prints the
# first string in that list (located at index 0) which is 
# 'Few things in life are as important as '