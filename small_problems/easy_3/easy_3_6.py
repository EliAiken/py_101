# Madlibs is a simple game where you create a story template with "blanks" 
# for words. You, or another player, then construct a list of words and 
# place them into the story, creating an often silly or funny story as a result.

# Create a simple madlib program that prompts for a noun, a verb, an adverb, 
# and an adjective, and injects them into a story that you create.

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter and adverb: ")

print(f"""
Have you ever heard of the crazy {adjective} {noun}?
The {noun} hates Taco Tuesdays because they always put peppers in his tequila.
On said Tuesdays, the {noun} {verb}s {adverb} to get his revenge on the bartender.
Hopefully, we will get to see the {adjective} {noun} {verb} {adverb} today!
""")