# Question 3 (name) viva questioning

# Keyword "def" defines the <unary> function "is_valid_length" that takes in the <string> variable "name" and returns a <boolean>
def is_valid_length(name: str) -> bool:
    # variable "length" tests if the length of name is between 1 and 9 (inclusive) characters
    length = 1 <= len(name) <= 9
    # ^uses "len" function to see if the length of "name" is in range (1,9)
    # returns <boolean> assinged to "length" with "return" statement
    return length

    # statement "pass" used as a placeholder to indicate no additional code in function 
    pass

# Keyword "def" defines the <unary> function "is_valid_start" that takes in the <string> variable "name" and returns a <boolean>
def is_valid_start(name: str) -> bool:
    # variable "start" tests if "name" starts with a letter of the alphabet (a,z)
    start = name[0].isalpha()
    # ^uses .isaplha method to see if first index of "name" (name[0]) is between (a,z)
    # returns <boolean> assinged to "start" with "return" statement
    return start

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

# Keyword "def" defines the <unary> function "is_one_word" that takes in the <string> variable "name" and returns a <boolean>
def is_one_word(name: str) -> bool:
    # initialises <boolean> variable "one_word" to false
    one_word = False
    # "if" statement used to detect whether a space (" ") is in the <string> variable "name"
    if(name.find(" ")==-1):
    # ^.find methods returns "-1" if no space is detected in "name"
        one_word = True
        # ^<boolean> variable "one_word" set to true "if" .find method is -1
    # returns <boolean> assigned to "one_word" with "return" statement
    return one_word

    # statement "pass" used as a placeholder to indicate no additional code in function
    pass

# Keyword "def" defines the <unary> function "is_valid_name" that takes in the <string> variable "name" and returns a <boolean>
def is_valid_name(name: str) -> bool:
    # calls previous functions ("is_valid_length", "is_valid_start", "is_one_word") and checks if all return <boolean> true
    if is_valid_length(name) and is_valid_start(name) and is_one_word(name):
        return True
    else:
        return False
    # ^uses "if" statement check if all functions are true