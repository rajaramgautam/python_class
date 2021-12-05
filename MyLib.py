# Importing all functions from previous assignments
def big_functions():

    # 1) Create a function for each math operation (add, div, mult, sub)

    user_input = num1 = float(
        input('Please input first number between -100 to 100: '))
# 1) Limit the input range from -100 to 100 for each input number
    while num1 not in range(-100, 101):
        print('Your input is not between -100 to 100')
        num1 = float(input('Please input first number between -100 to 100: '))

    num2 = float(input('Please input second number between -100 to 100: '))

# 1) Limit the input range from -100 to 100 for each input number
    while num2 not in range(-100, 101):
        print('Your input is not between -100 to 100')
        num2 = float(input('Please input second number between -100 to 100: '))

    def add(num1, num2):
        add_result = num1 + num2
        return add_result

    Result = 'Cannot Divide by Zero'

    def div(num1, num2):
        if num2 == 0:
            return Result
    # if num2 == 0:
    # print('Cannot divide by Zero')
        else:
            div_result = num1 / num2
            return div_result

    def mult(num1, num2):
        mult_result = num1 * num2
        return mult_result

    def sub(num1, num2):
        sub_result = num1 - num2
        return sub_result

    print('The sum of two numbers: ', add(num1, num2))
    print('The difference of two numbers: ', sub(num1, num2))
    print('The product of two numbers: ', mult(num1, num2))
    print('The division of first number by second number results: ',
          div(num1, num2))
    print('Thanks for using our calculator!')


# input_value = (input("Do you like to continue, please press 'y' for YES and 'n' for NO? ").lower()


# 3) create a function IsinRange() to test a value between two ranges like this;
# Here is the spec in pseudo code

    lr = int(input('Enter your Lower range: '))
    hr = int(input('Enter your Higher range: '))
    n = int(input('Enter your number: '))

    def IsinRange(lr, hr, n):
        if n >= lr and n <= hr:
            return print('The number you entered is within a range you set.')
        else:
            return print('Please check the numbers and try again.')
    IsinRange(lr, hr, n)

# 2) The application will run forever, you will ask the user to continue or not.


print("We are trying to build simple calculator.")


def big_function_new():
    big_functions()

    input_again = input("Do you like to use again? ").lower()

    while input_again == 'y':
        big_functions()
        input_again = input("Do you like to use again? ").lower()

        # print('Your input is valid. Please rerun the program with valid input.')
    print("Thank you for using calculator.")
    
def scalc(p):

      lstring=p.split(",")

      if lstring[2]=="*":

         res= int(lstring[0]) * int(lstring[1])

      if lstring[2]=="+":

        res= int(lstring[0]) + int(lstring[1])
      if lstring[2]=="-":

         res= int(lstring[0]) - int(lstring[1])

      if lstring[2]=="/":

        res= int(lstring[0]) / int(lstring[1])  
        

      return res
 

