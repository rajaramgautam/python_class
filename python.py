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
x, y, z = "Orange", "Banana", "Cherry"

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

# Python Booleans
print(10 > 9)

# Running true condition
a = 200
b = 100

if b > a:
    print("b is greater than a.")
else:
    print("b is not greater than a.")
# The bool() function allows us to evaluate any value, and give us True
# or False in return

print(bool("Hello World"))
print(bool(37))

# Any string is true, except empty strings.
# Any string is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool(""))
print(bool(0))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
print(bool(False))

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made
# from a class with a __len__ function that returns 0 or False:


class myclass():
    def __len__(self):
        return 0


myobj1 = myclass()
print('False for myclass object')
print(bool(myobj1))

# Functions can return a Boolean


def myfunction():
    return True


print(myfunction())

# Python Operators
print("Addition")
print(10+5)
# % gives remainder
print(7 % 2)

# // gives quotient
print(7//2)

# ~ is NOT in python
# ^ is XOR in python

# Python Lists

mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[0])

# List items are ordered, changeable, and allow duplicate values.
# List items ae indexed with the first index [0], the second index [1] etc.

# List length, we use len() function to get it
# Length of the list

print(len(mylist))

# type()
# From Python's perspective, list are defined as objects with the data type 'list':
print(type(mylist))
