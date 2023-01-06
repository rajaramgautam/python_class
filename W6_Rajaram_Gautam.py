# Instructions
# This is the flower box and it should at the beginning of each assignment

# You must add comments to your code
# Program name : Wk6_Rajaram_Gautam.py
# Student Name : Rajaram Gautam
# Course : ENTD220
# Instructor : Allen Jordan
# Date : 12/09/2021
# Copy Wrong : This is my work
# You are going to enhance the prior assignment by doing the following
# 1) Use list to create a menu
menu = ['add', 'sub', 'mult', 'div']
# 2) Create a function the will return the results of the four operations in a dictionary allInOne(n1,n2)
# Sample output
# 1) Add two numbers
def add(n1, n2):
    add_result = n1+n2
    return add_result

# 2) Mult two number
def mult (n1, n2):
    mult_result = n1 * n2
    return mult_result

# 3) Divide
def div(n1, n2):
    Result = 'Cannot Divide by Zero'
    if n2 == 0:
        return Result
    else:
        return n1/n2

# 4) Scalc
def sub(n1, n2):
    sub_result = n1 -n2

    return sub_result

# 5) all in one ..
def allinone(n1, n2):
    result = {"add":add(n1, n2), "sub":sub(n1, n2), "mult":mult (n1, n2), "div":div(n1, n2)}
    return result
    
# 6) …

res = allinone(5,2)

res


# res=allInOne(5,2)

# The results will be return in this format;

# res is dictionary {"add":7, "sub":3, "mult":10, "div":2.5}



# from res, you are going to print

print(f"5 + 2 = {res['add']}")
print(f"5 - 2 = {res['sub']}")
print(f"5 * 2 = {res['mult']}")
print(f"5 / 2 = {res['div']}")


# 5 + 2 = 7

# 5 - 2 = 3

# 5 * 2 = 10

# 5 / 2 = 2.5

# Submission Instructions:
# Make sure that you save your code in a text file in this format;

# W6_firstname_lastname.py