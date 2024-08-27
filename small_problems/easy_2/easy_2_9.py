# Build a program that randomly generates and prints Teddy's age. To 
# get the age, you should generate a random number between 20 and 100, 
# inclusive.

import random

def get_name():
    print("What is your name?")
    global name
    name = input()
    if not name:
        name = "Teddy"

def teddy():
    age = random.randint(20, 100)       # randint() is inclusive for both the start and stop
    print(f'{name} is {age} years old!')

def main():
    get_name()
    teddy()

main()