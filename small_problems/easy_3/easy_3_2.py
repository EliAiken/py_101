# Write a function that takes a string argument and returns a new string 
# that contains the value of the original string with all consecutive 
# duplicate characters collapsed into a single character.

def crunch(text):
    crunched_text = []
    previous_character = None
    
    for char in text:
        if char != previous_character:
            crunched_text.append(char)
            previous_character = char
    
    final_text = ''.join(crunched_text)
    return final_text

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

# LS ANSWER:

def crunch(text):
    index = 0
    crunched_text = ''

    while index < len(text):
        if index == len(text) - 1 or text[index] != text[index + 1]:
            crunched_text += text[index]

        index += 1

    return crunched_text

# Our solution builds a string named crunched_text by iterating over the 
# characters in the text argument. While iterating, we append the character 
# at the current index to crunched_text if the character it is not equal 
# to the next character. If it is equal, then do nothing.

# Note that we also need to determine whether we are dealing with the last 
# character in the original string.