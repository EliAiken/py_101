import random
import os
import sys

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

SHORTENED_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def prompt(message):
    print(f">>> {message} <<<")

def display_winner(player, computer):
    print(f"Your choice > {player.upper()} vs "
           f"{computer.upper()} < Computer Choice")
    if player_wins(player, computer):
        prompt("You Win!")
        return "p_wins"
    if player == computer:
        prompt("It's a Tie!")
        return "Ties"
    prompt("Computer Wins!")
    return "c_wins"

def player_wins(player, computer):
    return computer in WINNING_COMBOS[player]

def keep_score():
    if RESULT == "p_wins":
        score["p_wins"] += 1
        print(f"Player Score > {score["p_wins"]} | {score["c_wins"]} "
              "< Computer Score")
    elif RESULT == "c_wins":
        score["c_wins"] += 1
        print(f"Player Score > {score["p_wins"]} | {score["c_wins"]} < "
              "Computer Score")
    else:
        print(f"Player Score > {score["p_wins"]} | {score["c_wins"]} < "
              "Computer Score")

    if score["p_wins"] == 3:
        prompt("You are the winner of this best out of five! Congrats!")
        score["p_wins"] = 0
        score["c_wins"] = 0
    if score["c_wins"] == 3:
        prompt("You lost this best out of five. Better luck next time!")
        score["p_wins"] = 0
        score["c_wins"] = 0

def play_again():
    while True:
        prompt("Do you want to play again? (y/n)")
        answer = input().strip().lower()
        if answer in ['y', 'yes']:
            break
        if answer in ['n', 'no']:
            prompt("Thanks for playing! Have a nice day!")
            print("""
    _______           _______                     ______
---'   ____)      ---'   ____)____           ---'   ____)____
      (_____)               ______)                    ______)
      (_____)               _______)                __________)
      (____)               _______)                (____)
---.__(___)        ---.__________)            ---.__(___)

      """)
            sys.exit()
        else:
            prompt("Please enter 'y' or 'n' to continue.")

score = {
    "p_wins": 0,
    "c_wins": 0,
    "Ties": 0
}

prompt("Welcome to Eli's Rock, Paper, Scissors, Lizard, Spock "
       "Best Out of Five Tournament Game!")
print("""
    _______           _______                     ______
---'   ____)      ---'   ____)____           ---'   ____)____
      (_____)               ______)                    ______)
      (_____)               _______)                __________)
      (____)               _______)                (____)
---.__(___)        ---.__________)            ---.__(___)

      """)
prompt("Below are the rules:")
print("""1. Rock beats Scissors and Lizard
2. Paper beats Rock and Spock
3. Scissors beats Paper and Lizard
4. Lizard beats Spock and Paper
5. Spock beats Rock and Scissors
6. The first player to get 3 wins is the winner!""")
prompt("Ready to play? Press Enter to continue")
input()

while True:
    os.system('clear')
    prompt(f"Pick your move: {", ".join(VALID_CHOICES)}")

    choice = input().strip().lower()
    if choice in SHORTENED_CHOICES:
        choice = SHORTENED_CHOICES[choice]
    else:
        while choice not in VALID_CHOICES:
            prompt("That is not a valid choice. Try again")
            choice = input().strip().lower()
            if choice in SHORTENED_CHOICES:
                choice = SHORTENED_CHOICES[choice]

    computer_choice = random.choice(VALID_CHOICES)

    RESULT = display_winner(choice, computer_choice)

    keep_score()

    play_again()