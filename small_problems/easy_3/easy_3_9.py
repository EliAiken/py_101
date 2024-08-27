# Given a string that consists of some words and an assortment of non-alphabetic 
# characters, write a function that returns that string with all of the 
# non-alphabetic characters replaced by spaces. If one or more non-alphabetic 
# characters occur in a row, you should only have one space in the result 
# (i.e., the result string should never have consecutive spaces).

def clean_up(text):
    clean_text = ''

    for idx, char in enumerate(text):
        if char.isalpha():
            clean_text += char
        elif idx == 0 or clean_text[-1] != ' ':
            clean_text += ' '

    return clean_text


print(clean_up("---what's my +*& line?") == " what s my line ")

print(clean_up("---what's my +*& line?"))