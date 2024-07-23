import random
import os

def play_rps():
    while True:
        os.system('clear')
        display_scoreboard()
        print()
        prompt(f"Pick your move: {", ".join(VALID_CHOICES)}")

        choice = input().strip().lower()
        if choice in SHORTENED_CHOICES:
            choice = SHORTENED_CHOICES[choice]
        else:
            while choice not in VALID_CHOICES:
                prompt("That is not a valid choice. Try again")
                choice = input().strip().lower()
                choice = SHORTENED_CHOICES.get(choice, choice)

        computer_choice = random.choice(VALID_CHOICES)

        display_choices(choice, computer_choice)

        result = display_winner(choice, computer_choice)

        keep_score(result)

        next_round()

        if score["p_wins"] == 3 or score["c_wins"] == 3:
            os.system('clear')
            display_scoreboard()
            print()
            best_of_five()
            keep_playing = play_again()
            if keep_playing is False:
                break

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

score = {
    "p_wins": 0,
    "c_wins": 0,
    "Ties": 0
    }

def prompt(message):
    print(f">>> {message} <<<")

def display_choices(player, computer):
    print(f"Your Choice > {player.upper()} vs "
        f"{computer.upper()} < Computer Choice")

def display_winner(player, computer):
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

def next_round():
    if score["p_wins"] < 3 and score["c_wins"] < 3:
        prompt("Press Enter to play the Next Round")
        input()

def keep_score(result):
    if result == "p_wins":
        score["p_wins"] += 1
        print(f"Player Score > {score["p_wins"]} | {score["c_wins"]} "
            "< Computer Score")
    elif result == "c_wins":
        score["c_wins"] += 1
        print(f"Player Score > {score["p_wins"]} | {score["c_wins"]} < "
            f"Computer Score  -  Ties: {score["Ties"]}")
    else:
        score["Ties"] += 1
        print(f"Player Score > {score["p_wins"]} | {score["c_wins"]} < "
            f"Computer Score  -  Ties: {score["Ties"]}")

def best_of_five():
    if score["p_wins"] == 3:
        prompt("Game Over - You won this Best-"
            "Out-of-Five! Congrats!")
        score["p_wins"] = 0
        score["c_wins"] = 0
        score["Ties"] = 0
    if score["c_wins"] == 3:
        prompt("Game Over - You lost this Best-Out-of-Five. "
            "Better luck next time!")
        score["p_wins"] = 0
        score["c_wins"] = 0
        score["Ties"] = 0

def play_again():
    while True:
        prompt("Do you want to play again? (y/n)")
        answer = input().strip().lower()
        if answer in ['y', 'yes']:
            return True
        if answer in ['n', 'no']:
            prompt("Thanks for playing! Have a nice day!")
            return False
        prompt("Please enter 'y' or 'n' to continue.")

def display_scoreboard():
    print(f"Player Score > {score["p_wins"]} | {score["c_wins"]} "
        f"< Computer Score  -  Ties: {score["Ties"]}")

prompt("Welcome to Eli's Rock, Paper, Scissors, Lizard, Spock "
    "Best-Out-of-Five Tournament Game!")
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
print()
print("""*Pro Tip* > Use abbreviated choices as well to make your moves!
Accepted abbreviations:
    r = rock
    p = paper
    s = scissors
    l = lizard
    sp = spock""")
print()
prompt("Ready to play? Press Enter to continue")
input()
play_rps()