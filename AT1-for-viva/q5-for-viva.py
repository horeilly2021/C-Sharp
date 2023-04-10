# Question 5 (train) viva questioning

# Keyword "def" defines the <nullary> function "intro"
def intro():
    print("Larry: I'm Larry. I'll be your hunting instructor.")

# Keyword "def" defines <nullary> function "travel_to_camp" 
def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    # function "input" used to detect wether player presses keyboard
    input("Press Enter to travel to the Meadow...")
    print("Travelling to the Meadow...\nLarry: This is your camp. Here you'll set up your mouse trap.")

# Keyword "def" defines <nullary> function "setup_trap" that returns a <tuple>
def setup_trap() -> tuple:
    # assigning <string> variables "left_trap", "right_trap" and "no_trap" respectively
    left_trap = "High Strain Steel Trap"
    right_trap = "Hot Tub Trap"
    no_trap = "Cardboard and Hook Trap"

    print("Larry: Let's get your first trap...")
    # "input" function used to detect is player presses keyboard
    input("Press Enter to view traps that Larry is holding...")

    print("Larry is holding...\nLeft: {}\nRight: {}".format(left_trap, right_trap))
    # ^.format method assigns <string> variables "left_trap" and "right_trap" to "print" function respectively

    # variable "trap" has player pick either the "left_trap" or "right_trap" using the "input" function
    trap = input("Select a trap by typing \"left\" or \"right\": ")
    trap = trap.strip()
    # ^.strip method used to remove possible whitespace

    # "if" statement used to detect if player enters "left"
    if trap == "left":
        trap = left_trap
        # ^<string> variable "left_trap" is assigned to variable "trap"
        print("Larry: Excellent choice.\nYour \"{}\" is now set!\nLarry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!".format(left_trap))
        cheddar = 1
        # ^<integer> variable "cheddar" is set to "1"
        return trap, cheddar
        # ^returns variables <string> "left_trap" and <integer> "cheddar" using "return" statement

    # "elif" statement used to detect if player enters "right"
    elif trap == "right":
        trap = right_trap
        # ^<string> variable "right_trap" is assigned to variable "trap"
        print("Larry: Excellent choice.\nYour \"{}\" is now set!\nLarry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!".format(right_trap))
        cheddar = 1
        # ^<integer> variable "cheddar" is set to "1"
        return trap, cheddar
        # ^returns variables <string> "right_trap" and <integer> "cheddar" using "return" statement

    # "else" statement used to detect if player enters neither "left" or "right"
    else:
        trap = no_trap
        # ^<string> variable "no_trap" is assigned to variable "trap"
        print("Invalid command! No trap selected.\nLarry: Odds are slim with no trap!")
        cheddar = 0
        # ^<integer> variable "cheddar" is set to "0"
        return trap, cheddar
        # ^returns variables <string> "no_trap" and <integer> "cheddar" using "return" statement

# Keyword "def" defines the <unary> function "sound_horn" that returns a <string>
def sound_horn() -> str:
    print("Sound the horn to call for the mouse...")
    # variable "horn_input" uses "input" function to see if player wants to play
    horn_input = input("Sound the horn by typing \"yes\": ")
    if horn_input == "yes":
        return True
    else:
        return False
    # ^uses "if" statement test is player enter "yes" returning a <boolean>

# Keyword "def" defines <unary> function "basic_hunt" that takes variables "trap", "horn_input" and "cheddar" returning a <boolean>
def basic_hunt(trap: str, cheddar: int, horn_input: str) -> bool:
    # uses "if" statement to see if players has variable "cheddar" and "horn_input"
    if cheddar == 1 and horn_input == True:
        print("Caught a Brown mouse!\nCongratulations. Ye have completed the training.")
        return True
    # ^returns true using "return" statement
    #uses "elif" statement to see if player has neither "cheddar" or "horn_input"
    elif cheddar == 0 and horn_input == False:
        print("Nothing happens.")
    # uses "else" statement to see if player has either "cheddar" or "horn_input"
    else:
        print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")

# Keyword "def" defines <unary> function "end" that takes in the <boolean> "hunt_status"
def end(hunt_status: bool):
    # uses "if" statement to check if "hunt_status" is true
    if hunt_status == True:
        print("Good luck~")

# Keyword "def" defines the <nullary> function "main" that calls the previous functions
def main():
    intro()
    travel_to_camp()
    # uses "while" statement (loop) to repeat functions until false
    while True:
        trap, cheddar = setup_trap()
        horn_input = sound_horn()
        hunt_status = basic_hunt(trap, cheddar, horn_input)
        end(hunt_status)
        # variable "repeat" uses "input" function to see if player wants to continue
        repeat = input("\nPress Enter to continue training and \"no\" to stop training: ")
        # "if" statement used to respond to "repeat" variable
        if repeat == "no":
            break
            # ^uses "break" control loop statement to end "while" loop if variable "repeat" is "no"
    
    # "return" statement used to return <string> "trap"
    return trap

if __name__ == '__main__':
    main()