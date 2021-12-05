# Instructions
# This is the flower box and it should at the beginning of each assignment
# You must add comments to your code
# Program name : Wk5_rajaram_gautam.py
# Student Name : Rajaram Gautam
# Course : ENTD220
# Instructor : Allen Jordan
# Date :12/05/2021

# You are going to enhance the prior assignment by doing the following
# 1) Move all the functions into Mylib.py
# Ans :- Separate MyLib.py file has been created and put in the current working directory with all the functions created in previous execises. It will act as module now.

# 2) Use import to include Mylib into the code
import MyLib

# 3) Test the code and make sure that the prior code is still working
import MyLib
MyLib.big_function_new()
# Functions tested in Jupyter Notebook for its operation.
"""4) Add the following function into Mylib
scalc(p1)
p1 will be a string like this "N1, N2, operator"
 examples
scalc("20,30,*")
the result will be 600
scalc("50,20,+")
the result will be 70
scalc("50,20,-")
the result will be 30

scalc("60,20,/")
the result will be 30
"""
### Added in Mylib.py and tested for operation in jupyter notebook
import MyLib
MyLib.scalc("20,30,*")
import MyLib
MyLib.scalc("50,20,+")
import MyLib
MyLib.scalc("50,20,-")
import MyLib
MyLib.scalc("60,20,/")

"""use string functions to parse the first number, the second number, and the operator from the input string.
use the prior functions (add, subtract, divide and multiply ) to do the calculations.
"""