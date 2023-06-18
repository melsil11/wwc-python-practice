# Write a function that prints "Hello World!"
print ("Hello World!")
# Congratulate your self
print ("Congratulations! You wrote your first Python program")
# Print a number (interger) 
print(7)

# print a string, or series of character, as shown in the "Hello World" program
print("I love python")
print("dkjsa457387@fksd")

# print the result of a mathmatical equation.
print(22*2+1)

# STRINGS

# A string is a series of characters, which can include letters, numbers, and special characters such as exclamation points.

# We can use the following formats to print a string: 1) single quotes (one apostrophe), 2) double quotes, or 3) triple single quotes (three apostrophes).

# print('single quotes') 

# print("double quotes") 

# print('''triple single quotes''')

# when we run the following code, all print functions will print the same result "Hello World"

print('Hello world!') 
print("Hello world!") 
print('''Hello world!''')

# Here is an example of when triple single quotes (three apostrophes) could be useful.
# The quote includes a quotation in double quotes and an apostrophe for the word "You're".
print('''Stephanie says, "You're amazing!"''')

# Or we can use a backwards slash to escape an apostrophe (or double quotes).
# This example uses apostrophes around the string and a backslash before the apostrophe in "You're."
print('Stephanie says, "You\'re amazing!"')

# Multiply a string by a number (integer).
print('Hello' * 3)

# Here is an example of when triple single quotes (three apostrophes) could be useful.
# The quote includes a quotation in double quotes and an apostrophe for the word "You're".
print('''Stephanie says, "You're amazing!"''')

# Or we can use a backwards slash to escape an apostrophe (or double quotes).
# This example uses apostrophes around the string and a backslash before the apostrophe in "You're."
print('Stephanie says, "You\'re amazing!"')
# Practice
print('Tell it to me stright')
# Practice:
print(' mel says "you\'re Amazing"')
# Multiply a string by a number (integer).
print('Hello' * 3)
# HelloHelloHello
# Practice:
print('Hi' * 2)
# HiHi
# to print with spaces add a space after the word but before the closing quote
print('hello ' * 3)

# Check the character length of a string using the len() function.
print(len('Hello!'))
# Practice:
print(len('Melanie Silva'))
# it counts spaces as characters

# We can also add together, or concatenate, more than one string.
# We will be using concatenation often in future sessions.
print("Hi, " + "Stephanie" + "!") 

# Note the space after "Hi, " in this example and how the code executes.

# practice:
print('Hi, ' + 'Melanie' +'!' )
# //////////////

# Variables

# Variables are pieces of memory that store our data.

# When code runs into a variable, Python retrieves the value assigned to the variable for the function (or task) being executed.

# We create a variable by using an equal sign to assign a value.

# Create a variable called "name" and assign your first name as the value.
# Then print the variable.
# Reminder to put your name value in quotes since it is a string.
name = 'Stephanie'
print(name)

# Practice:
name = 'Melanie'
print(name)

# Variable names can be a single letter, a word, or several words separated by underscores, all in lowercase.
# Below are some examples:
w = '"w" is a single letter'
women = '"women" is a word'
women_who_code = '"women_who_code" is words shown in snake_case'

print(w) 
print(women) 
print(women_who_code)

# Create a variable and assign a value to it.
# Practice:
dog = 'winnie'
print(dog)

# Earlier we concatenated three strings together.

# We can concatenate variables with strings assuming the value inside the variable is also a string.

# If any of the data are strings, then all need to be strings. We will see in a few minutes how to concatenate an integer or float with strings using a very simple function.

# Create a variable and assign a string value to it.
# Then use a print function to concatenate strings and the variable together.
# We are going to revise our earlier code to replace our names with the variable value.
name = 'Stephanie'
print("Hi, " + name + "!")

# Practice:
name = 'melanie'
print('Hi, ' + name + '!') 

# Integers

# Integers are whole numbers. 

# Integers can be positive or negative.

# Examples: 3, 27, 28384723, -10, -234
print(12)
# Practice:
print(21)
# Create a variable and assign an integer value.
x = 10
print(x)

# Practice:
number = 21
print(number)

# Floating Point Numbers

# Floating point numbers, or floats, are numbers with decimal points.

# Floats can be positive or negative.

# Examples: 3.1415926, 1.0, 100.5, -5.5, -233.33

print(12.5)
# Practice:
print(1.12)
# Create a variable and assign a floating point number value to it.
y = 3.1415926
print(y)
z = -3232.25
print(z)
# Practice:
age = 21.5
print(age)
# Integer and floating  point numbers cannot concatenate with strings without first being converted to a string.

# To convert an integer or float to a string, we can use the str() function.
# Create a variable called "rice", or your favorite food, and assign an integer value to it.
# Next print a brief sentence using concatenation and the str() function to print the value of the variable.
rice = 2
print("I would like " + str(rice) + " order(s) of rice, please.") 

# Hint: Note the space after "like" and before "order(s)".
# Practice:
apples = 3
print('i want ' + str(apples) + ' apples')

# Type Function
# We can quickly check the data type of the value that is assigned to a variable using the type() function.
integer1 = 314
print(type(integer1)) 

float1 = 3.14
print(type(float1)) 

string1 = "Excellent work, everyone!"
print(type(string1))
# Practice:
number = 21
print(type(number))
float1 = 21.5
print(type(float1))
strings = " I love python"
print(type(strings))

# Arithmetic Operators

# + addition
# - subtraction
# * multiplication
# / division
# // integer division -use if needed the resulting number to be an interger
# % remainder
# ** exponentiation
# - negation

print(11+22+33+44)
print(100 * 55)

num1 = 2
num2 = 3
print(num1 + num2) # addition
print(num1 - num2) # subtraction
print(num1 * num2) # multiplication
print(num1 / num2) # division

# practice
# Practice:
numb1 = -1
numb2 = 3
print(numb1 - numb2)
