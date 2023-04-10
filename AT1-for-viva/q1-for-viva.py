# Question 1 viva questioning

# Assigning the variable "title" the title of the game
title = "Mousehunt"

# Assigning the variable "logo" to the logo of the game
logo = '''
       ____()()
      /      @@
`~~~~~\_;m__m._>o'''

# Assigning the variable "author" to the author of the game
author = 'An INFO1110/COMP9001 Student'

# Assigning the variable "credits" to the credit shown
credits = f'''
Inspired by Mousehunt© Hitgrab
Programmer - {author}
Mice art - Joan Stark'''
# ^f-string used to assign the "author" variable under "programmer"

# Function "print" used to display the variables ("title", "logo", "credits"), with paramemter (sep=) showing a new line for each variable
print(title, logo, credits, sep="\n")