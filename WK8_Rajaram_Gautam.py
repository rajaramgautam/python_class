# Instructions
# This is the flower box and it should at the beginning of each assignment

# You must add comments to your code
# Program name : Wk7_rajaram_gautam.py
# Student Name : Rajaram Gautam
# Course : ENTD220
# Instructor : Allen Jordan

# file = open('WK7_Rajaram_Gautam.py', 'r')

# print (file.read())


with open("text.txt", "w") as out_file:
    class wrfile:
        out_file.write('We are trying to build simple basic wrfile.')

        # Enter the first number
        first_number = (input('Please input first number : '))
        out_file.write(first_number)
        

        # Enter the second number
        second_number = (input('Please input second number : '))
        out_file.write(second_number)

        # Choose the operator for scalc 
        operator = (input('Please choose operator for scalc like (*, /, +, -) : '))
        out_file.write(operator)
        
        first_number = float(first_number)
        second_number = float(second_number)

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
            lstring[0] = wrfile.first_number
            lstring[1] = wrfile.second_number
            lstring[2] = wrfile.operator
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
            result = {"add":wrfile.add(wrfile.first_number, wrfile.second_number), "sub":wrfile.sub(wrfile.first_number, wrfile.second_number), "mult":wrfile.mult(wrfile.first_number, wrfile.second_number), "div":wrfile.div(wrfile.first_number, wrfile.second_number)}
            return result
        def quit():
            print("The program is closed now.")

        def main_menu():
            print("Welcome to Using wrfile. Choose Option for me to perform.")

            choice = input("""
                    1. ADD TWO NUMBERS
                    2. MULTIPLY TWO NUMBERS
                    3. DIVIDE TWO NUMBERS
                    4. RUN scalc
                    5. Run AllInOne Dictionary
                    0. Quit
                    Please make a selection 1, 2 , 3, 4, 5 and O """)
            if choice == '1':
                result =  wrfile.add(wrfile.first_number, wrfile.second_number)
                print(f'Your entries are: {wrfile.first_number} and {wrfile.second_number}')
                print(f'The result of: {wrfile.first_number} + {wrfile.second_number} : {result}')
                
                out_file.write(f'Your entries are: {wrfile.first_number} and {wrfile.second_number}')
                out_file.write(f'The result of: {wrfile.first_number} + {wrfile.second_number} : {result}')

            elif choice == '2':
                result = wrfile.mult(wrfile.first_number, wrfile.second_number)

                print(f'Your entries are: {wrfile.first_number} and {wrfile.second_number}')
                print(f'The result of: {wrfile.first_number} * {wrfile.second_number} : {result}')
                
                out_file.write(f'Your entries are: {wrfile.first_number} and {wrfile.second_number}')
                out_file.write(f'The result of: {wrfile.first_number} * {wrfile.second_number} : {result}')

            elif choice == '3':
                result = wrfile.div(wrfile.first_number, wrfile.second_number)

                print(f'Your entries are: {wrfile.first_number} and {wrfile.second_number}')
                print(f'The result of: {wrfile.first_number} / {wrfile.second_number} : {result}')
                
                out_file.write(f'Your entries are: {wrfile.first_number} and {wrfile.second_number}')
                out_file.write(f'The result of: {wrfile.first_number} / {wrfile.second_number} : {result}')

            elif choice == '4':


                result =  wrfile.scalc("wrfile.first_number,wrfile.second_number,wrfile.operator")

                print(f'Your entries are: {wrfile.first_number}, {wrfile.second_number} and {wrfile.operator}')
                print(f'The result of: {wrfile.first_number} {wrfile.operator} {wrfile.second_number} : {result} ')

                out_file.write(f'Your entries are: {wrfile.first_number}, {wrfile.second_number} and {wrfile.operator}')
                out_file.write(f'The result of: {wrfile.first_number} {wrfile.operator} {wrfile.second_number} : {result} ')



            elif choice == '5':

                result =  wrfile.AllInOne(wrfile.first_number, wrfile.second_number)

                print(f'Your entries are: {wrfile.first_number} and {wrfile.second_number}')
                print(f'The result of all addition, subtraction, multiplication and division: {result}')

                out_file.write(f'Your entries are: {wrfile.first_number} and {wrfile.second_number}')
                out_file.write(f'The result of all addition, subtraction, multiplication and division: {result}')
            elif choice == '0':
                print('The program has been closed as per your request.')
                
                out_file.write('The program has been closed as per your request.')
                return quit()


            else:
                print('You must enter the valid option')
                
                out_file.write('You must enter the valid option')
                wrfile.main_menu()
               
        
            
            
    wrfile.main_menu()  
    
file = open('text.txt', 'r')

print (file.read())