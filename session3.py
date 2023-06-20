# Welcome to Beginner Python Study Group 2021!

# **Session 3: If/Else Statements**

# Hosted by Women Who Code Python Track

# Logical Conditions
# Before we launch into if/else statements, let's start by learning about logical conditions.

# With logical conditions, we compare two values (example: x == y). Python evaluates whether the condition is True or False. With an if/else statement, Python will take the result (True/False) and then proceed with performing whatever action the program asks it to do.

# Below is the list of logical conditions:

# == equal to
# != not equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to

# Note that there are two equal signs used for the equal logical condition. As we learned in Session 1, a single equal sign is for assigning values to variables. When comparing whether two values are equal, we will use the double equal sign.

7 <= 3
#  answer false 
'hello' != 'Hello'
# answer true 
1 + 3 == "4"
# answer false - the 4 is a string 
int(4.0) == 4
# true

# If Statements
# If statements evaluate whether a condition is True or False and then performs an action if the condition evaluates to True.

# If statements are written with the "if" keyword, followed by a conditional statement and a colon (:). The code we want to execute if the condition is True is indented underneath it.

# # If Statements

# if condition:
#   execute this code


# Example: PSuedo code 


# if your cat is hungry:

# In this example, the condition evaluates whether the cat is hungry or not. If the condition evaluates to True, then a print statement will direct the user to feed the cat.

# if kitty_cat == 'hungry':
#   print('Your cat is hungry. Please feed her.')

# Run the following code.
# If the condition evaluates to True, then the statement will print. Otherwise, nothing will print.

kitty_cat = 'hungry'
if kitty_cat == 'hungry':
  print('Your cat is hungry. Please feed her.')

  # Create a variable "name" and assign a string value to it.
# Write an if statement that prints a hello message to the user if the names match.

name = 'Stephanie'
if name == 'Stephanie':
  print('Hi, Stephanie!')

# Practice
name = 'Melanie'
if name == 'Melanie':
    print('Hi ' + name + '!')
# Create a variable "fav_food" and assign a string value to it.
# Write an if statement that prints the favorite food to the user if the values match.

fav_food = 'rice'
if fav_food == 'rice':
  print('Your favorite food is rice!')
# Practice

# Practice
fav_food = 'apples'
if fav_food == 'apples':
  print('your favorite food is apples!')

# If / Else Statements
# If statements evaluate whether a condition is True or False and then executes the code if the condition evaluates to True. If the condition evaluates to False, Python then executes the code underneath the "else:" statement.

# If statements are written with the "if" keyword, followed by a condition and a colon (:). The code we want to execute is indented underneath it.

# The else statement is written with the "else" keyword followed by a colon (:). The code we want to execute is indented underneath it.

# if condition:
#   execute this code
# else:
#   execute this code
# Example:

# if your cat is hungry:
#   feed her now
# else:
#   feed her later
# if kitty_cat == 'hungry':
#   print('Your cat is hungry. Please feed her now.')
# else:
#   print('Your cat is not hungry right now. Please feed her later.')

# Run the following code.
# If the condition evaluates to True, then user will be instructed to feed the cat now.
# Else, if the condition evaluates to False, then the user will be instructed to feed the cat later.

kitty_cat = 'hungry'
if kitty_cat == 'hungry':
  print('Your cat is hungry. Please feed her now.')
else:
  print('Your cat is not hungry right now. Please feed her later.')

  # Create a program that asks for the user's name.
# If the user's name matches the provided name, print a hello message.
# Else, print "Hmm, I was expecting someone else."

name = input('What is your name? ')
if name == 'Stephanie':
  print('Hi, Stephanie!')
else:
  print('Hmm, I was expecting someone else.')

  # Practice:
name = 'melanie'
if name == 'melanie':
  print('Hi ' + name + '!')
else:
    print('Hmm. I was expecting someone else.')


# Create a program that asks the user to select one of four possible doors.
# If the user selects the correct door, print a congratulatory message.
# Else, print a message informing the user that the incorrect door was chosen.

def door_prize_game():
  print('There is a prize behind one of four doors.')
  print('Choose one of the following doors: 1, 2, 3, or 4.')
  reward_door = "2"
  user_door = input('Enter your guess: ')
  if user_door == reward_door:
    print("Congratulations! You chose the correct door! You win a prize!")
  else:
    print("Sorry, you did not select the correct door.")

if __name__ == '__main__':
  door_prize_game()

# Practice:
def game_prize():
    print('There is a prize behind 1 of 4 doors')
    print('choose a number from 1 to 4')
    reward_door = '2'
    user_choise = input('Enter your guess:')
    if user_choise == reward_door:
        print('Congrates, you chose correct')
    else:
        print('sorry wrong door')
if __name__ == '__main__':
  game_prize()

