# Question 4 viva questioning

# Keyword "def" defines the <nullary> function "intro"
def intro():
    print("Larry: I'm Larry. I'll be your hunting instructor.")

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

# Keyword "def" defines the <nullary> function "travel_to_camp" 
def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    # function "input" used to detect wether player presses keyboard
    input("Press Enter to travel to the Meadow...")
    print("Travelling to the Meadow...\nLarry: This is your camp. Here you'll set up your mouse trap.")

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

# Keyword "def" defines <unary> function "travel_to_camp" that returns a <tuple>
def setup_trap() -> tuple:
    # assigning variables "left_trap" and "right_trap" respectively
    left_trap = "High Strain Steel Trap"
    right_trap = "Hot Tub Trap"

    print("Larry: Let's get your first trap...")
    # function "input" used to detect wether player presses keyboard
    input("Press Enter to view traps that Larry is holding...")

    print("Larry is holding...\nLeft: {}\nRight: {}".format(left_trap, right_trap))
    # ^.format method assigns variables "left_trap" and "right_trap" to "print" function

    # variable "trap" has player pick either the "left_trap" or "right_trap" using the "input" function
    trap = input("Select a trap by typing \"left\" or \"right\": ")
    trap = trap.strip()
    # ^uses .strip method to remove possible whitespace

    # "if" statement used to assign selected trap to player and return <boolean>
    if trap == "left":
        trap = left_trap
        print("Larry: Excellent choice.\nYour \"{}\" is now set!\nLarry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!".format(left_trap))
        # ^.format method assigns "left_trap" to "print" function
        return True

    elif trap == "right":
        trap = right_trap
        print("Larry: Excellent choice.\nYour \"{}\" is now set!\nLarry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!".format(right_trap))
        # ^.format method assigns "right_trap" to "print" function
        return True

    else:
        print("Invalid command! No trap selected.\nLarry: Odds are slim with no trap!")
        return False
    
    # variable "cheddar" uses "if" statement to assign <integer> to "cheddar"
    cheddar
    if trap == True:
        cheddar = 1
    else:
        cheddar = 0

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

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

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

# Keyword "def" defines the <binary> function "sound_horn" that returns a <boolean>
def basic_hunt(cheddar: int, horn_input: str) -> bool:
    if cheddar == 1 and horn_input == True:
        print("Caught a Brown mouse!\nCongratulations. Ye have completed the training.")
        return True
    # ^uses "if" statement to see if players has variable "cheddar" and "horn_input"
    elif cheddar == 0 and horn_input == False:
        print("Nothing happens.")
    # ^uses "elif" statement to see if player has neither "cheddar" or "horn_input"
    else:
        print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
    # ^uses "else" statement to see if player has either "cheddar" or "horn_input"
    
    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

# Keyword "def" defines <unary> function "end" that takes in the <boolean> "hunt_status"
def end(hunt_status: bool):
    if hunt_status == True:
        print("Good luck~")
    else:
        return
    # ^uses "if" statement to check if "hunt_status" is true

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

# Keyword "def" defines the <nullary> function "main" that calls the previous functions
def main():
    intro()
    travel_to_camp()
    cheddar = setup_trap()
    horn_input = sound_horn()
    hunt_status = basic_hunt(cheddar, horn_input)
    end(hunt_status)

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass


if __name__ == '__main__':
    main()
    