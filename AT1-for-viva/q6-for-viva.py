# Question 6 (shop) viva questioning

# Keyword "def" defines <unary> function "buy_cheese" that takes in the <integer> variable "gold" and returns a <tuple>
def buy_cheese(gold: int) -> tuple:

    # initialises the variable "price" to 10
    price = 10

    print("You have {} gold to spend.".format(gold))
    # ^.format used to assign variable "gold" to the "print" function
    # variable "gold_spent" uses "input" function to find out amount of cheese the player wants
    gold_spent = input("State [cheese quantity]: ")

    # uses "if" statement to detect whether user "input"s response to variable "gold_spent" is "back"
    if gold_spent == "back":
        return (0, 0)
    # ^"if" user response is "back" then variable "gold_spent" is assigned <tuple> (0,0) using "return" statement

    # code block "try-except" used to detect if there is an error when responding to "gold_spent"
    try:
        # variable "cheese_type" is assigned to first part of answer and variable "cheese_str" assigned to second
        cheese_type, cheese_str = gold_spent.lower().split()
        # ^.lower method used to convert response to "gold_spent" into lowercase
        ## ^^.split method used to split <string> "gold_spent" into two parts being variables "cheese_type" and "cheese_str"

        # <string> variable "cheese_str" converted into an <integer> assigned to <integer> variable "cheese" using "int" function
        cheese = int(cheese_str) 
    # excecutes "except" statement if error converting <string> "cheese_str" to <integer> "cheese" resulting in the "ValueError" class
    except ValueError:
        print("Sorry, did not understand.")
        return (0, 0)
        # ^returns <tuple> (0,0) using "return" statement

    # uses "if" statement to detect error in variable "cheese_type"
    if cheese_type != "cheddar":
        print("Sorry, did not understand.")
        return (0, 0)
        # ^returns <tuple> (0,0) using "return" statement

    # uses "if" statement to detect whether variable "cheese" is too low
    if cheese <= 0:
        print("Must purchase a positive amount of cheese.")
        return (0, 0)
        # ^returns <tuple> (0,0) using "return" statement

    # <integer> variable "total_price" assigned to the expression of <integer> ("cheese" * "price") (operand (* = operator) operand)
    total_price = cheese * price
    # uses "if" statement to detect whether the <integer> variable "gold" is less than the <integer> variable "total_price"
    if gold < total_price:
        print("Insufficient gold.")
        return (0, 0)
        # ^returns <tuple> (0,0) using "return" statement

    # <integer> variable "gold" decreases by <integer> variable "total_price" using shorthand assingment operator "-="
    gold -= total_price
    print("Successfully purchase {} cheddar.".format(cheese))
    return (total_price, cheese)
    # ^returns a <tuple> of variables (<integer> "total_price", <integer> "cheese") using "return" statement

    ''' <tuple> ("total_price", "cheese") returns (0,0) if fails test because no "cheese" is bought so "total_price" is 0 '''

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

# Keyword "def" defines <tenary> function "display_inventory" that takes in <integer> "gold", <integer> "cheese", <string> "trap"
def display_inventory(gold: int, cheese: int, trap: str) -> None:

    print("Gold - {}\nCheddar - {}\nTrap - {}".format(gold, cheese, trap))
    # ^.format assigns variables "gold", "cheese" and "trap" to "print" function

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

# Keyword "def" defines <nullary> function "main"
def main():

    # initialises the variable <integer> "gold", <integer> "cheese" and <string> "trap"
    gold = 125
    cheese = 0
    trap = "Cardboard and Hook Trap"

    print("Welcome to The Cheese Shop!\nCheddar - 10 gold")

    # uses "while" statement repeat until false
    while True:
        print("\nHow can I help ye?")
        # <integer> variable "choice" assigned to response of "input" function then coverted to <integer> using "int" function
        choice = int(input("1. Buy cheese\n2. View inventory\n3. Leave shop\n"))

        # uses "if" statement to detect if <integer> "choice" is 1 ("Buy cheese")
        if choice == 1:
            gold_spent, cheese_bought = buy_cheese(gold)
            # ^calls "buy_cheese" function that takes in <integer> variable "gold" and returns <tuple> of "gold_spent" and "cheese_bought"
            gold -= gold_spent
            # ^<integer> variable "gold" decreases by <integer> variable "gold_spent" using shorthand assingment operator "-="
            cheese += cheese_bought
            # ^<integer> variable "cheese" increases by <integer> variable "cheese_bought" using shorthand assingment operator "+="

        # uses "elif" statement to detect if <integer> "choice" is 2 ("View inventory")
        elif choice == 2:
            display_inventory(gold, cheese, trap)
            # ^calls "display_invetory" function that takes in arguements <integer> "gold", <integer> "cheese", <string> "trap"
        
        # uses "elif" statement to detect if <integer> "choice" is 3 ("Leave shop")
        elif choice == 3:
            break
            # ^uses "break" statement to exit loop

        # uses "else" statement to detect if <choice> isn't 1, 2 or 3
        else:
            print("Invalid choice. Please try again.")
            # ^user restarts loop
    
    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

if __name__ == '__main__':
    main()