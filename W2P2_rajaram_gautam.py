# Part II Instructions:


# This is the flower box and it should at the beginning of each assignment
# You must add comments to your code
# Program name : Wk2P2_rajaram_gautam.py
# Student Name : Rajaram Gautam
# Course : ENTD220
# Instructor : Allen Jordan
# Date : 11/14/2021
# Copy Wrong : This is my work
# You are going to enhance the prior assignment by doing the following:

print('We are trying to build simple basic calculator.')
first_number = float(input('Please input first number between 1 to 100: '))
# 1) Limit the input range from -100 to 100 for each input number
while first_number not in range(-100, 101):
    print('Your input is not between 1 to 100')
    first_number = float(input('Please input first number between 1 to 100: '))

second_number = float(input('Please input second number between 1 to 100: '))
# if second_number == 0:
# print('Cannot divide by Zero')
# 1) Limit the input range from -100 to 100 for each input number
while second_number not in range(-100, 101):
    print('Your input is not between 1 to 100')
    second_number = float(
        input('Please input second number between 1 to 100: '))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

Result = 'Cannot Divide by Zero'


def division(first_number, second_number):
    if second_number == 0:
        return Result
    else:
        return first_number/second_number


print('The sum of two numbers: ', addition)
print('The difference of two numbers: ', subtraction)
print('The product of two numbers: ', multiplication)
print('The division of first number by second number results: ',
      division(first_number, second_number))
print('Thanks for using our calculator!')

# 1) Limit the input range from -100 to 100 for each input number
# 2) Prevent dividing by zero(Do not use try-except)

# 3) Instead of hard coding values from -100 to 100, let the user enter the range

# Hints:
# Not able to push to git


# Submission Instructions:
# Make sure that you save your code in a text file in this format; W2P2_firstname_lastname.py
