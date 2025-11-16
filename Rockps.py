import random

options=("rock","paper","scissors")
game_running=True

def rockps_game():
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("Enter a choice(rock, paper, scissors):")
    print(f"Player choice:{player}")
    print(f"Computer choice:{computer}")

    if player==computer:
        print("It's a tie!")
    elif player=="rock" and computer=="scissors":
        print("You win!")
    elif player=="paper" and computer=="rock":
        print("You win!")
    elif player=="scissors" and computer=="paper":
        print("You win!")
    else:
        print("You lose!")


