print('We are trying to build simple basic calculator.')

# Enter the first number
first_number = float(input('Please input first number : '))

# Enter the second number
second_number = float(input('Please input second number : '))

# Choose the operator for scalc 
operator = (input('Please choose operator for scalc like (*, /, +, -) : '))


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
    


def scalc(p):
    lstring=p.split(",")
    lstring[0] = first_number
    lstring[1] = second_number
    lstring[2] = operator
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
    result = {"add":add(first_number, second_number), "sub":sub(first_number, second_number), "mult":mult(first_number, second_number), "div":div(first_number, second_number)}
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
        result =  add(first_number, second_number)
        print(f'Your entries are: {first_number} and {second_number}')
        print(f'The result of: {first_number} + {second_number} : {result}')
    
    elif choice == '2':
        result = mult(first_number, second_number)
        
        print(f'Your entries are: {first_number} and {second_number}')
        print(f'The result of: {first_number} * {second_number} : {result}')
    
    elif choice == '3':
        result = div(first_number, second_number)
        
        print(f'Your entries are: {first_number} and {second_number}')
        print(f'The result of: {first_number} / {second_number} : {result}')
    
    elif choice == '4':
     

        result =  scalc("first_number,second_number,operator")
        
        print(f'Your entries are: {first_number}, {second_number} and {operator}')
        print(f'The result of: {first_number} {operator} {second_number} : {result} ')
        
  
    elif choice == '5':
        
        result =  AllInOne(first_number, second_number)
        
        print(f'Your entries are: {first_number} and {second_number}')
        print(f'The result of all addition, subtraction, multiplication and division: {result}')
   
    elif choice == '0':
        return quit()
    
    else:
        print('You must enter the valid option')
        main_menu()
main_menu()        