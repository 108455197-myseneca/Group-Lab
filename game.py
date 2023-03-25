#!/usr/bin/env python3
#Group 6
#Group Lab 

import random
# Asking the user for their choice
userOption = input("Please choose one of the following options:(rock, paper, scissors) ")

#Assigning random choice to computer
options = ["rock", "paper", "scissors"]
computerOption = random.choice(options)

print(f"\nYou chose {userOption}, computer chose {computerOption}.\n")

#Possible Outcomes
if userOption == computerOption:
    print(f"It's a tie! Both of the players selected {userOption}")
    
elif userOption == "rock":
    if computerOption == "scissors":
        print("You win! Rock smashes scissors! ")
    else:
        print("You lose. Paper covers rock!")

elif userOption == "paper":
    if computerOption == "rock":
        print("You win! Paper covers rock!")
    else:
        print("You lose Scissors cuts paper!")

elif userOption == "scissors":
    if computerOption == "paper":
        print("You win! Scissors cuts paper!")
    else:
        print("You lose ,Rock smashes scissors!")

