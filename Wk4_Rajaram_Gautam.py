# Instructions
# This is the flower box and it should at the beginning of each assignment

# You must add comments to your code
# Program name : Wk4_Rajaram_Gautam.py
# Student Name : Rajaram Gautam
# Course : ENTD220
# Instructor : Allen Jordan
# Date : 11/25/2021
# Copy Wrong : This is my work
"""
You are going to enhance the prior assignment by implementing exceptions

***** You need to tell me where you implemented the exception and why. *****
Show me 2 test cases that will trap the errors
Sample output

Use the same sample output from prior assignment
Submission Instructions:
Make sure that you save your code in a text file in this format;

W4_firstname_lastname.py
"""
"""
# Test Case 0: I will try to open my last week assignment file which is in my cureent working directory. If I give wrong file name
try:
    f = open('Wk3_RajaramGautam.py')

except FileNotFoundError:
    print('This message for file not found error. Please make sure the file name is correct.')"""

# Test Case 1 : While program is running, end user may press ctrl + c, to abort my program. So I put KeyboardInterrupt as one case of except.


# Test Case 2: While running Wk3_Rajaram_Gautam.py by importing it, which is in current working directory. It will throw us an error if we give string values to
# lower or higer range number and even for first number and second number in range of (-100, 101). Since all my input by end users needs to be numeric, there is
#  more likely chance that they may input string as input, so I used ValueError to sort out that problem on my code.

try:
    import Wk3_Rajaram_Gautam

except KeyboardInterrupt:
    print(' KeyboardInterrupt :- The program is aborted by end user using ctrl + c command.')

except ValueError:
    print('ValueError: While Entering Numeric Values, ensure its not a string.')
