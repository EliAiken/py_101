my_str = " Hello friends. This will be my test string for the methods! "

print(my_str.capitalize())          # capitalize first character, convert rest to lowercase
print(my_str.swapcase())            # swap all letter's cases (upper to lower, lower to upper)
print(my_str.upper())               # convert all lowercase letters to uppercase
print(my_str.lower())               # convert all uppercase letters to lowercase
print(my_str.isalpha())             # return True if all characters are alphabetic
print(my_str.isdigit())             # return True if all chars are digits
print(my_str.isalnum())             # return True if all chars are alphanumeric
print(my_str.islower())             # return True if all chars are lowercase
print(my_str.isupper())             # return True if all chars are uppercase
print(my_str.isspace())             # return True if all chars are spaces (whitespace)
print(my_str.strip())               # removes any leading and trailing whitespace
print(my_str.rstrip())              # removes any trailing whitespace
print(my_str.lstrip())              # removes any leading whitespace
print(my_str.replace('friends', 'enemies')) # replaces first element with second element
print(my_str.split(' '))            # splits the string into a list at the designated separator
print(my_str.find('n'))             # finds the first instance of the indicated element
print(my_str.rfind('t'))            # finds the last instance of the indicated element