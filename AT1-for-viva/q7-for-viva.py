# Question 7 (game) viva questioning

import random

# Question 3 (name) import
def is_valid_length(name: str) -> bool:
    length = 1 <= len(name) <= 9
    return length

    pass

def is_valid_start(name: str) -> bool:
    start = name[0].isalpha()
    return start

    pass

def is_one_word(name: str) -> bool:
    one_word = False
    if(name.find(" ")==-1):
        one_word = True
    return one_word

    pass

def is_valid_name(name: str) -> bool:
    if is_valid_length(name) and is_valid_start(name) and is_one_word(name):
        return True
    else:
        return False

import train
import shop

from train import main as main_train

def question_1():
    title = "Mousehunt"
    logo = '''
       ____()()
      /      @@
`~~~~~\_;m__m._>o'''

    author = 'An INFO1110/COMP9001 Student'

    credits = f'''
Inspired by Mousehunt© Hitgrab
Programmer - {author}
Mice art - Joan Stark\n'''

    print(title, logo, credits, sep="\n")

# you can make more functions here if you please
# or any global variables

def main():

    # importing information from question 1
    question_1()

    # get player name
    name = input("What's ye name, Hunter?\n") 
    if is_valid_name(name) == True:
        name = name
    else:
        name = "Bob"

    print("Welcome to the Kingdom, Hunter {}!".format(name))

    # ask player if they want to train
    print("Before we begin, let's train you up!")
    # variable "train_choice" uses "input" function to find out if player wants to "train"
    train_choice = input("Press \"Enter\" to start training or \"skip\" to Start Game: ")

    # initialise <string> variable "trap"
    trap = "Cardboard and Hook Trap"

    # "if" statement detects if player elected to "skip" training
    if train_choice != "skip":
        print("")
        # ^adds a before training sequence
        # runs "main" function from "q5 (train)"
        trap = main_train()
        # ^if user selects a trap during the training, it is assigned to the <string> variable "trap"
    else:
        trap = "Cardboard and Hook Trap"
        # ^if user elects to "skip", <string> variable "trap" is set to initial "trap"

    # initialise game variables
    gold = 125
    points = 0
    cheese = 0
    consecutive_fails = 0
    # ^used for repeating the game if no mouse caught 5 times

    # main game loop using "while" statement
    while True:
        # show action menu
        print("\nWhat do ye want to do now, Hunter {}?".format(name))
        choice = int(input("1. Exit game\n2. Join the Hunt\n3. The Cheese Shop\n"))
        # ^function "int" converts <string> input to an <integer> assigned to <integer> variable "choice"

        # exit game
        if choice == 1:
            break

        # join the hunt
        elif choice == 2:

            # hunt loop using "while" statement
            while True:
                print("Sound the horn to call for the mouse...")
                horn_choice = input("Sound the horn by typing \"yes\": ")
                horn_choice = horn_choice.strip()
                # ^.strip method used to remove possible whitespace

                if horn_choice == "yes":
                    if cheese > 0:
                        if random.random() <= 0.5:
                            print("Caught a Brown mouse!")
                            gold += 125
                            points += 115
                            cheese -= 1
                            consecutive_fails = 0
                            # ^resets consecutive fails since mouse caught
                        else:
                            print("Nothing happens.")
                            cheese -= 1
                            consecutive_fails += 1
                            # ^increases consecutive fails since no mouse caught
                    else:
                        print("Nothing happens. You are out of cheese!")
                        consecutive_fails += 1
                        # ^increases consecutive fails since no mouse caught
                    print("My gold: {}, My points: {}\n".format(gold, points))
                    if consecutive_fails >= 5:
                        continue_hunting = input("Do you want to continue to hunt? ")
                        continue_hunting = continue_hunting.strip()
                        if continue_hunting == "no":
                            break
                        else:
                            consecutive_fails = 0

                elif horn_choice == "stop hunt":
                    break

                else:
                    print("Do nothing.")
                    print("My gold: {}, My points: {}\n".format(gold, points))

        # visit cheese shop
        elif choice == 3:
            print("Welcome to The Cheese Shop!")
            print("Cheddar - 10 gold")
            while True:
                print("\nHow can I help ye?")
                print("1. Buy cheese")
                print("2. View inventory")
                print("3. Leave shop")
                shop_choice = int(input())

                if shop_choice == 1:
                    gold_spent, cheese_bought = shop.buy_cheese(gold)
                    gold -= gold_spent
                    cheese += cheese_bought
                elif shop_choice == 2:
                    shop.display_inventory(gold, cheese, trap)
                elif shop_choice == 3:
                    break
                else:
                    print("Invalid choice. Please try again.")

        # invalid choice
        else:
            print("Invalid choice. Please try again.")

    pass

if __name__ == '__main__':
    main()