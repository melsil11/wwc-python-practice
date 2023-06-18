# Review/Refresher

# **Comments**

# Comments help us communicate the purpose of our code. Comments are "hidden" and will not execute or print out to the user when our code runs. Comments can start with a hashtag (#). This is an example of a comment.

# **Print Function**

# The print function will "print" (or show) data to the user.
# The print function is written as print() with the data placed between the parentheses.

print()

# Examples:
print(1)
print(25.51)
print('abc123!@#')
print("hello")

# Strings (str)

# A string is a series of characters, which can include letters, numbers, and special characters.
# 'A string using single quotes (one apostrophe)'
# "A string using double quotes"
# '''A string using triple single quotes (three apostrophes)'''

# Write a function that prints "Hello world!" to the user.
print('Hello world!')

# **Variables**

# Variables are pieces of memory that store our data.
# When code runs into a variable, Python retrieves the value assigned to the variable for the function (or task) being executed. We create a variable by using an equal sign (=) to assign a value.

# w = 290,000
# women = 290,000
# women_who_code = 290,000

coding = "Yay!"
print(coding)

# **Integer (int)**

# Integers are whole numbers, no decimal points. Can be positive or negative.
# Examples: 3, 27, 28384723, -10, -234
awesome_integer = -300
print(awesome_integer)

# **Floating Point Numbers (float)**

# Floating point numbers, or floats, are numbers with decimal points. Can be positive or negative.Examples: 3.1415926, 1.0, 100.5, -5.5, -233.33
awesome_float = 3.14
print(awesome_float)



# Introduction to Functions

# We learned about several built-in Python functions in Session 1:
# *   print()
# *   len()
# *   str()
# *   type()

# Functions are blocks of code that run when called and perform a specific task. Functions are beneficial because we can reuse code for repetitive tasks.

# When defining our own functions, we begin with the "def" keyword, followed by the function name, parantheses (), and a colon (:).

# Function names can be a word or several words separated by underscores (snake_case).

#  EXAMPLES: 
# def women():
# def women_who_code():

# Indentation is very important in Python. The next line below the function definition must be indented using the tab key.

# Define a function called "main".
# Within the main function, write a print function that prints "Hello world!" to the user.
# Remember to indent the print function using the tab key on your keyboard.

def main():
  print('Hello world!')

if __name__ == '__main__':
  main()

# The above code (if __name__ ...) is telling Python which function to start with.
# This will be important when we start working with parameters and returns.
# We will practice using it in this session.


# Define a function called "new_main".
# Within the main function, write a print function that prints "Hello world!" to the user.
# Remember to indent the print function using the tab key on your keyboard.
# Practice:

def new_main():
  print("Hello World!")

if __name__ == '__main__':
  new_main()

# Define a function called "add_two_numbers".
# Create two variables and assign integer values to them.
# Print the sum of the numbers.

def add_two_numbers():
  number1 = 55
  number2 = 10
  print(number1 + number2)

if __name__ == '__main__':
  add_two_numbers()

  # Define a function called "multiply_two_numbers".
# Create two variables and assign integer values to them.
# Multiply the numbers and print the result.
# Practice:

def multiply_two_numbers():
    number_1 = 2
    number_2 = 5
    print(number_1 * number_2)

if __name__ == '__main__':
  multiply_two_numbers()


# Input Functions
# Input functions ask the user to provide information. The input function is written as input(). We will put questions formatted as strings between the parantheses.

# Create a variable "name" and assign an input function within it that asks for the user's name.
# Then print the name to the user.

name = input("What is your name? ")
print(name)

# practice

age = input("How old are you? ")
print(age)


fav_food = input("Enter your favorite food: ")
print(fav_food)

# practice

fav_dog_breed = input(" Enter your favorite dog breed: ")
print(fav_dog_breed)

# Input Functions & Concatenation
# In Session 1, we practiced concatenation by creating a variable, assigning a string value to it, and then concatenating with other strings.

# Now, we will create variables with input functions and concatenate the result using the print function.


# Create a variable and assign a string value to it.
# Then use a print function to concatenate strings and the variable together.

name = 'Stephanie'
print("Hi, " + name + "!")

name = input("What is your name? ")
print("Hi, " + name + "!")

# practice

age = input(" How old are you? ")
print("I am " + age + " years old.")

# Define a function "pet1_data"
# Create the variables "pet1_type", "pet1_name", and "pet1_age".
# Print the data results to the user.

def pet1_data():
  pet1_type = input("What type of animal is your pet? ")
  pet1_name = input("What is your pet's name? ")
  pet1_age = input("What is your pet's age (in years)? ")

  print("Your " + pet1_type + "'s name is " + pet1_name + ".")
  print(pet1_name + " is " + pet1_age + " year(s) old.")

if __name__ == '__main__':
  pet1_data()


# Define a function "pet_data"
# Create the variables "pet_type", "pet_name", and "pet_age".
# Print the data results to the user.
# Practice:
def pet_data():
    pet_type = input("What type of pet do you have? ")
    pet_name = input("What is your pets name? ")
    pet_age = input("How old is your pet? ")

    print("your " + pet_type + "'s name is " + pet_name + ".")
    print( pet_name + " is " + pet_age + " years old.")

if __name__ == '__main__':
  pet_data()

# Note that the input function automatically converts the inputted values into strings. For the pet_age variable, we inputted an number. But the input function processed it as a string, and the value concatenated with the strings without error.
