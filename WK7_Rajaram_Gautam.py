# Instructions
# This is the flower box and it should at the beginning of each assignment

# You must add comments to your code
# Program name : Wk7_rajaram_gautam.py
# Student Name : Rajaram Gautam
# Course : ENTD220
# Instructor : Allen Jordan

class Calculator:
    print('We are trying to build simple basic calculator.')

    # Enter the first number
    first_number = float(input('Please input first number : '))

    # Enter the second number
    second_number = float(input('Please input second number : '))

    # Choose the operator for scalc 
    operator = (input('Please choose operator for scalc like (*, /, +, -) : '))
    
    def __init__(self, first_number, second_number, operator):
        self.first_number = first_number
        self.second_number = second_number
        self.operator = operator
        
    
      


    # defining add 
    def add(first_number, second_number):
        return first_number + second_number

    # defining sub 
    def sub(first_number, second_number):
        return first_number - second_number

    # defining mult 
    def mult(first_number, second_number):
        return first_number * second_number


    Result = 'Cannot Divide by Zero'

    # defining div
    def div(first_number, second_number):
        if second_number == 0:
            return Result
        else:
            return first_number/second_number

    # definning scalc
    def scalc(p):
        lstring=p.split(",")
        lstring[0] = Calculator.first_number
        lstring[1] = Calculator.second_number
        lstring[2] = Calculator.operator
        if lstring[2]== "*":
            result =  float(lstring[0]) * float(lstring[1])
            return result

        if lstring[2]== "+":
            result =  float(lstring[0]) + float(lstring[1])
            return result 

        if lstring[2]== "-":
            result = float(lstring[0]) - float(lstring[1])
            return result

        if lstring[2]== "/":
            result = float(lstring[0]) / float(lstring[1])
            return result



    def AllInOne(first_number, second_number):
        result = {"add":Calculator.add(Calculator.first_number, Calculator.second_number), "sub":Calculator.sub(Calculator.first_number, Calculator.second_number), "mult":Calculator.mult(Calculator.first_number, Calculator.second_number), "div":Calculator.div(Calculator.first_number, Calculator.second_number)}
        return result
    def quit():
        print("The program is closed now.")

    def main_menu():
        print("Welcome to Using Calculator. Choose Option for me to perform.")

        choice = input("""
                1. ADD TWO NUMBERS
                2. MULTIPLY TWO NUMBERS
                3. DIVIDE TWO NUMBERS
                4. RUN scalc
                5. Run AllInOne Dictionary
                0. Quit
                Please make a selection 1, 2 , 3, 4, 5 and O """)
        if choice == '1':
            result =  Calculator.add(Calculator.first_number, Calculator.second_number)
            print(f'Your entries are: {Calculator.first_number} and {Calculator.second_number}')
            print(f'The result of: {Calculator.first_number} + {Calculator.second_number} : {result}')

        elif choice == '2':
            result = Calculator.mult(Calculator.first_number, Calculator.second_number)

            print(f'Your entries are: {Calculator.first_number} and {Calculator.second_number}')
            print(f'The result of: {Calculator.first_number} * {Calculator.second_number} : {result}')

        elif choice == '3':
            result = Calculator.div(Calculator.first_number, Calculator.second_number)

            print(f'Your entries are: {Calculator.first_number} and {Calculator.second_number}')
            print(f'The result of: {Calculator.first_number} / {Calculator.second_number} : {result}')

        elif choice == '4':


            result =  Calculator.scalc("Calculator.first_number,Calculator.second_number,Calculator.operator")

            print(f'Your entries are: {Calculator.first_number}, {Calculator.second_number} and {Calculator.operator}')
            print(f'The result of: {Calculator.first_number} {Calculator.operator} {Calculator.second_number} : {result} ')


        elif choice == '5':

            result =  Calculator.AllInOne(Calculator.first_number, Calculator.second_number)

            print(f'Your entries are: {Calculator.first_number} and {Calculator.second_number}')
            print(f'The result of all addition, subtraction, multiplication and division: {result}')

        elif choice == '0':
            print('The program has been closed as per your request.')
            return quit()
            

        else:
            print('You must enter the valid option')
            Calculator.main_menu()
Calculator.main_menu()  