# Instructions
# Part I Instructions:

# This is the flower box and it should be at the beginning of each assignment
# You must add comments to your code
# Program name : Wk2P1_firstname_lastname.py
# Student Name : Rajaram Gautam
# Course : ENTD220
# Instructor : Allen Jordan
# Date : 11/14/2021
# Copy Wrong : This is my work

# You are going to create the following:

# A simple calculator to accept two numbers and print the addition, subtraction, multiplication and division of the two numbers.
# You are required to store each input number in a separate variable.
print('We are trying to build simple basic calculator.')
first_number = float(input('Please mention me your first number. '))
second_number = float(input('Please mention me your second number. '))

# Hints
# 1) You should also store each calculation in a variable
# 2) You will get an error if you divide by zero, you will address this problem next assignment
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = round(first_number/second_number, 2)

print('The sum of two numbers is', addition)
print('The difference of two numbers is', subtraction)
print('The product of two numbers is', multiplication)
print('The division of first number by second number results in', division)

print('Thanks for using our calculator!')


# Submission Instructions:
# Make sure that you save your code in a text file in this format. Check your file after the upload to see if they are readable. You can paste your code in the student submission text area.

# W2P1_firstname_lastname.py
