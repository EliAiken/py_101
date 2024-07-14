# Build a program that asks the user to enter the length
# and width of a room, in meters, then prints the room's
# area in both square meters and square feet.

def prompt(message):
    print(f"==> {message}")

prompt("Welcome to Room Area Calculator")
prompt("What is the length (in meters) of the room you want to measure?")
length = int(input())
prompt("What is the width (in meters) of the room you want to measure?")
width = int(input())
prompt(f'These are the measurements: {length} x {width} meters')
confirm = input("Is that correct? (y/n) ")
while confirm == 'y':
    result = length * width
    prompt(f'Your room area is {result} sq meters')
    prompt(f'Your room area is also {result * 10.7639:.2f} sq feet')
    break
while confirm != 'y':
    prompt("I'm sorry. Could you please re-confirm the measurements?")
    prompt("What is the length (in meters) of the room you want to measure?")
    length = int(input())
    prompt("What is the width (in meters) of the room you want to measure?")
    width = int(input())
    prompt(f'These are the measurements: {length} x {width} meters')
    confirm = input("Is that correct? (y/n) ")
    result = length * width
    prompt(f'Your room area is {result} sq meters')
    prompt(f'Your room area is also {result * 10.7639:.2f} sq feet')

# :.2f ensures that the output is formatted to two (here^) decimal places

# Launch School Answer:

# length = float(input("Enter the length of the room in meters: "))
# width = float(input("Enter the width of the room in meters: "))

# area_in_meters = length * width
# area_in_feet = area_in_meters * 10.7639

# print(f"The area of the room is {area_in_meters:.2f} "
#       f"square meters ({area_in_feet:.2f} square feet).")