# Function and method calls can take expressions as arguments. Suppose we 
# define a function named rps as follows, which follows the classic rules 
# of the rock-paper-scissors game, but with a slight twist: in the event 
# of a tie, it just returns the choice made by both players.

def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
    
# What does the following code output?

print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# MY ANSWER: Paper

# LS ANSWER: Paper

# The outermost call determines the result of comparing 
# rps(rps("rock", "paper"), rps("rock", "scissors")) against rock. 
# That means that we must evaluate the two separate calls, rps("rock", "paper") 
# and rps("rock", "scissors"), and combine them by calling rps on their results. 
# Those innermost expressions return "paper" and "rock", respectively. 
# Calling rps on those two values returns "paper", which, when evaluated 
# against "rock", returns "paper".