import random

def prompt(string):
    print(f'>>>{string}<<<')

def player_roll():
    prompt(' Roll the dice? y/n ')
    choice = input()
    if choice == 'y':
        global roll
        roll = random.randint(1,13)
        return roll
    
def computer_roll():
    global comp_roll
    comp_roll = random.randint(1,13)
    return comp_roll

def result():
    prompt(f' You rolled {roll} ')
    prompt(f' Computer rolled {comp_roll} ')
    if roll > comp_roll:
        prompt(' You win! ')
    else:
        prompt(' You lose! ')

player_roll()
computer_roll()
result()