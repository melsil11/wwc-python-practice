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

# Note that the input function automatically converts the inputted values into strings. For the pet_age variable, we inputted a number. But the input function processed it as a string, and the value concatenated with the strings without error.

# Constructor Functions
# In Session 1, we practiced concatenation when a variable is assigned an integer or float value. Since we cannot concatenate an integer or a float with a string, we demonstrated how to specify the type using the str() function.

# Let's explore this concept further...

# Using a str(), int(), or float() function constructs a string, integer, or float type. This is known as casting, and these functions are called constructor functions.

# Create a variable called "rice", or your favorite food, and assign an integer value to it.
# Next print a brief sentence using concatenation and the str() function to print the value of the variable.

rice = 2
print("I would like " + str(rice) + " order(s) of rice, please.")

# Construct an integer using the int() function.
a = 3.14
print(int(a))

b = "3"
print(int(b))

# Practice:
kitty = 23.56
print(int(kitty))
# Construct a float using the float() function.
c = 3
print(float(c))

d = "3"
print(float(d))

# Practice:
kitty_cat = 23
print(float(kitty_cat))
# Construct a string using the str() function.

e = 3
print(str(e))

# practice

# Construct a string using the str() function.

e = 3
print(str(e))

f = 3.0
print(str(f))

# practice
cat1 = 100 
print(str(cat1))

# Create a variable and assign an integer value to it.
# Check the type of the variable.
# Then print the value inside the variable as a string by using the str() function.

cats = 100
print(type(cats))
print(str(cats))

# Note that we did not actually change the type of the value assigned to the "cats" variable.
# If we print type(cats), we see the value within the variable is still an integer.

print(type(cats))

# Create a variable "cats_str" that constructs a string from the "cats" variable.
cats = 100
cats_str = str(cats)
print(cats_str)
print(type(cats_str))

# Practice:
dogs = 100 
dogs_str = str(dogs)
print(dogs_str)
print(type(dogs_str))

# Putting it together 

# The following example wraps up several of the concepts we learned today: defining functions, input functions, casting and constructor functions, and concatenation.


# Define a function "average_two_numbers".
# Collect two numbers from the user and specify the type as float.
# Create a variable to calculate the average of the two numbers.
# Print a statement that concatenates the two numbers and the average.

def average_two_numbers():
  print("Please input two numbers. The program will average the numbers.")
  user_number1 = int(input("Enter your first number: "))
  user_number2 = int(input("Enter your second number: "))
  average = (user_number1 + user_number2) / 2
  print("The average of " + str(user_number1) + " and " + str(user_number2) + " is " + str(average) + ".")

if __name__ == '__main__':
  average_two_numbers()

#   Practice 
def average_two_numbers():
  print("Please input two numbers. The program will average the numbers. ")
  user_num1 = int(input("Enter your first number: "))
  user_num2 = int(input("Enter second number: "))
  average = (user_num1 + user_num2) / 2
  print("The average of " + str(user_num1) + " and " + str(user_num2) + " is " + str(average) + ".")


if __name__ == '__main__':
  average_two_numbers()