# Build a program that displays when the user will retire and how many 
# years she has to work till retirement.

def get_age():
    global age
    age = int(input("What is your age? "))

def get_retire_age():
    global retire_age
    retire_age = int(input("At what age would you like to retire? "))

def will_retire():
    print(f"It's 2024. You will retire in {2024 + (retire_age - age)}.")
    print(f"You only have {(retire_age - age)} years of work to go!")

def main():
    get_age()
    get_retire_age()
    will_retire()

main()