# program to check if user input  numbers are equal without using any comparism operators

def checkIfSame(number1, number2):
    # use XOR operator as a^a is always 0
    if ((number1 ^ number2) != 0):
        print("Numbers are not equal")
    else:
        print("Both numbers are equal")

# taking input from user 
number1 = int(input("Enter the first number to compare : "))
number2 = int(input("Enter the second number to compare : "))

checkIfSame(number1, number2)
