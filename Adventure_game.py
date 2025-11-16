print('Welcome to our spooky adventure game!!\n\nYou are going to your home in a dark night and your car had some problem on a lonely road.\nWhile you were analysing the situation another car came and stopped by to check on you.\nHe was an old man probably in his 60s.\nHe offered you a lift and you have TWO choices:\n\nACCEPT it or REJECT it\n')

choice1 = input('Enter yes or no for the answer : ').lower()

if choice1 == 'yes':
    print("He was the trinity killer and he killed you 💀 game over!!")

elif choice1 == 'no':
    print("You said no and now regretting your decision.")
    print('You came to a decision to walk to the nearest gas station , it was 15 min away via walking\n\nwalking.....................\nYou saw something like a bear but you are not sure.\n\nYou have two thoughts now:\n1) Run faster silently\n2) Walk in your usual speed ignoring the danger')

    choice2 = int(input('Enter your choice\n\n1 --> Run\n2 --> Ignore the danger and continue... : '))

    if choice2 == 1:
        print("Running..... huh huh huh... You saw the gas station.")
    elif choice2 == 2:
        print("Walking..... oops !! You heard a bear’s voice and started running ..... You survived and saw the gas station.")

    print('You want something to drink and eat now after the bear event.\nYou saw a diet coke and a redbull.')

    choice3 = int(input('1 --> Diet Coke\n2 --> Redbull\nPick your choice: '))
