# first program on python
print("Hello World. I am learning python. I will try to allocate at least an hour a day for it.")


# use of indentation in python try to use at least one space for indentation 
# for same block of code, please remain constant on number of indentation
if 5 > 2:
    print("5 is greater than 2")
    
# python variables
# python has no command for declaring a variable
x = 5 
y = 7
z = "Hello, I am 36." 
print(x*y)
print(z)

# Comments
# Commenting on python is done by #

# multi lines commenting by using string with three quotation marks as python will ignore unassigned string
"""
Unassigned string will be ignored by python interpreter.
So on running it, python does not care.
"""

# getting the data type of the variable we use type() function

print(type(x))
print(type(z))

# Variables names are case sensitive since Python is case sensitive programming language
# A varaible name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha numeric characters and underscores
# Variable names are case-sensitive (name1. Name1 and NAME1 are different variables)

# Python Variables - Assign Multiple Values
x , y, z = "Orange", "Banana", "Cherry"

print(x)
print(y) 
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

age = 36
name = "Rajaram"

print(name, age)

# Global Vriables
# Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# To create a global variable inside a function, we can us the global keyword.

age = '36'

def myage():
    age = '37'
    print("My age is " + age)

myage()

print("My age in real is " + age)

    