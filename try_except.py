try:
    string1 = input("Enter a number: ")
    num1 = float(string1)
except:
    print("You did not enter a number!")
else:
    print("Your number: " + str(num1))

# Two Errors at a timea
try:
    string1 = input("Enter a number: ")
    num1 = float(string1)
except (ValueError, KeyboardInterrupt):
    print("You did not enter a number!")
else:
    print("Your number: " + str(num1))
# Separate Error in separate lines

try:
    string1 = input("Enter a number: ")
    num1 = float(string1)
except ValueError:
    print("You entered '" + string1 + "'")
    print("You did not enter a number.")
except KeyboardInterrupt:
    print("You used Ctrl + C to end the program.")
else:
    print("Your number: " + str(num1))
