############################################################
print("👾      🎊    WELCOME TO THE GAMING-ARCADE    🎊   🐇 ")
print("   ⚔️        ✂️             🎩            🎲          ")

 #

##########################################################
#importing dice game
import Dice

CHOOSE_THE_GAME_BUTTON = int(input("WELCOME!!\n" "1 --> ROCK-PAPER-SCISSORS\n" "2 --> DICE ROLL\n" "3 --> GUESS THE NUMBER??!!\n\n" "ENTER YOUR CHOICE: " ))

if CHOOSE_THE_GAME_BUTTON == 1:
    pass

elif CHOOSE_THE_GAME_BUTTON == 2:
    Dice.dice_game()

elif CHOOSE_THE_GAME_BUTTON == 3:
    pass

else:
    print("OOPS ENTERED WRONG CHOICE PLZ TRY AGAIN")
