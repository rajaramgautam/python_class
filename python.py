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
# Hello

# The list() Constructor
# It is also possible to use list() constructor when creating a new list


# note the double round brackets
thislist = list(("apple", "banana", "cherry"))

print(thislist)

# Python - Access List Items
# printing the second item of the list
print(thislist[1])

# Negative Indexing means start from the end
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# in range of index last item is not included where as first is included
print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])

print(thislist[-4: -1])

# Check if item exists

if "apple" in thislist:
    print("Yes, Apple is in the list.")

# Change List Items
thislist[1] = "blackfruit"
for item in thislist:
    print(item)

# inserting items as range
thislist[1:3] = ["banana", "grapes"]
print(thislist)

# If we inserted more items than we replace, the new items will be inserted where we specified, and the remaining items will
# move accordingly

thislist[1:2] = ["orange", "plum"]

for item in thislist:
    print(item)

# replacing the second and third value by one value
thislist[1:3] = ["pomegranate"]
for item in thislist:
    print(item)


# Python - Add List Items
# Append Items
# append at last

thislist.append("papaya")

for item in thislist:
    print(item)

# Insert Items
# Insert item at a specified index

print("Checking Insert")

thislist.insert(2, "Dragon Fruit")
for item in thislist:
    print(item)

# Extend List
# To append elements from another list to the current list, we use extend() method
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

for item in thislist:
    print(item)

# Add any iterable
# extend() method cab add any iterable object (tuples, sets, dictionaries etc.)

thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist)

# Removing Specified Item remove() method
thislist.remove("apple")
print(thislist)

# pop() method removes the specified index.
thislist.pop(2)
print("After Popping")
print(thislist)

# del keyword removes the specified index:
del thislist[-1]

print("printing after delete")
print(thislist)

# deleting entire list
# del thislist

# printing after deleting list

# print(thislist)

# clear() method empties the list
thislist.clear()

print(thislist)

# Python - Loop Lists
# for loop

thislist = ["apple", "banana", "cherry"]

for item in thislist:
    print(item)

for i in range(5):
    print(i)

# while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
# List Comprehension offer the shortest syntax for looping through lists:
[print(x) for x in thislist]

# List Comprehension example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("newlist")
print(newlist)

newlist2 = [x for x in range(10)]
print(newlist2)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ["hello" for x in fruits]

print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# Python - Sort Lists
# Sort List Alphanumerically sort()

print(fruits)

fruits.sort()

print(fruits)

fruits.sort(reverse=True)

print(fruits)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 83, 21]
thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort
# By default sort() method is case insensitive, resulting in all capital letters being sorted before lower case letters

thislist = ["banana", "orange", "Cherry", "Kiwi"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:

thislist.sort(key=str.lower)
print(thislist)

# Reverse Order
# reverse() method reverse the current sorting of the elements regardless of the alphabet.
thislist.reverse()
print(thislist)
# Let me see if I can push now.

# Python - Copy Lists
# copy()
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Another way to make a copy is to use the built-in method list()
mylist = list(thislist)
print(mylist)


# Python - Join Lists
# Join Two Lists
# By using + operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one

for x in list2:
    list1.append(x)

print(list1)

# Or we can use the extend() method, which purpose is to add elements from one list to another list:
list1.extend(list2)
print(list1)

# Python Tuples
mytuple = ("apple", "banana", "cherry")

# Tuple is ordered and unchangeable. It allows duplicates in its items.

print(mytuple)

for item in mytuple:
    print(item)

# Tuple Length
print(len(mytuple))

# Creating Tuple with One Item
# To create a tuple with only one item, we have to add a comma after item, otherwose Python will not recognize it as a tuple
this_not_tuple = ("apple")
print(type(this_not_tuple))

this_is_tuple = ("apple",)
print(type(this_is_tuple))

# Tuple Items - Data Types

# Tuple items can be of any data type:

# Tuple can contain different data types:

# From Python's perspective, tuples are defined as objects with the data type 'tuple':

# The tuple() Constructor

# It is also possible to use the tuple() constructor to make a tuple

# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Python - Access Tuple Items

# We can access tuple items by referring to the index number, inside square brackets:

print(thistuple[0])

# Negative Indexing
# Negative indexing means start from the end.

print(thistuple[-1])

# Range of Indexes:

# Check if Item Exists

if "apple" in thistuple:
    print("Yes, apple is ther in tuple.")

# Python - Update Tuples
# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuple are unchangeable, or immutable as it also called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list bak into a tuple

x = thistuple
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


# Add tuple to a tuple.
# You are allowed to add tuples, so if you want to add one item, (or many), create a new tuple with the items(s),
# and add it to the existing tuple:
y = ("orange",)
thistuple += y

print(thistuple)


# Python - Unpack Tuples

# Unpacking a Tuple

fruits = ("apple", "banana", "cherry")

# But, in python, we are also allowed to extract the values back into variables. This is called "unpacking":
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variabke name and the values
# will be assigned to the variable as a list:

fruits_1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits_1

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until
# the number of values left matches the number of variables left.

(green, *tropic, red) = fruits_1

print(green)
print(tropic)
print(red)

# Python - Loop Tuple

# You can loop through the tuple items vy using a for loop.
thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)
    
# Loop through the index numbers

# You can also loop through the tuple items by referring tp their index number.
# Use the range() and len() functions to create a suitable iterable.
