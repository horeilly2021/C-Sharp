# Question 2 viva questioning

# Variable "name" uses function "input" to ask for players name
name = input("Larry: What's ye name, Hunter?\n")
# prints if Larry can pronouce the players name
print("Larry: Is '{}' a name I can pronounce?".format(name))
# ^.format method assigns variable "name" to "print" function

# Variable "is_valid_length" tests if variable "name" is between 1 and 9 characters (inclusive)
is_valid_length = 1 <= len(name) <= 9
# ^uses "len" function to test if the length of "name" is in range (1,9)
print("It has a length of {} which is between 1 to 9 characters? {}!".format(len(name), is_valid_length))
# ^.format method assings the length of the variable "name" and the variable "is_valid_length" to the "print" function

# Variable "is_valid_start" tests if variable "name" starts with a letter of the alphabet (a,z)
is_valid_start = name[0].isalpha()
# ^uses .isalpha method to see if the first index of "name" (name[0]) is between (a,z)
print("It starts with an alphabet? {}".format(is_valid_start))
# ^.format method assigns variable "is_valid_start" to the "print" function

# Initialsies variable "is_one_word" to false
is_one_word = False
# uses "if" statement to check whether "name" has a space (" ") in it
if(name.find(" ")==-1):
    # ^.find method returns "-1" is no space detected in "name"
    is_one_word = True
    # ^variable "is_one_word" set to true if .find methods returns -1
print("It is a single word? {}".format(is_one_word))
# ^.format method assigns variable "is_one_word" to "print" function

# Variable "is_valid_name" tests if previous functions ("is_valid_length", "is_valid_start", "is_one_word") are True
is_valid_name = is_valid_length and is_valid_start and is_one_word
print("Larry: I can pronounce this name --- {}".format(is_valid_name))
# ^.format method assigns "is_valid_name" to the "print" function