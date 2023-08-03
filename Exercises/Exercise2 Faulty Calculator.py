# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 456
# Your program should take operator and the two numbers as input from the user
# and then return the result


print("Welcome to Harshil's Second Calculator!"
      "\n\tOPERATOR VALUES TO ENTER:\n\t1 for Addition\n\t2 for Subtraction\n\t3 for Multiplication\n\t4 for Division")
operation = int(input("\tEnter the operator value:"))
if 4 >= operation >= 1:
    if operation == 1:
     print("\tThis is a correct operator value! Please continue for addition.\n")
    if operation == 2:
     print("\tThis is a correct operator value! Please continue for subtraction.\n")
    if operation == 3:
     print("\tThis is a correct operator value! Please continue for multiplication.\n")
    if operation == 4:
     print("\tThis is a correct operator value! Please continue for division.\n")
else:
    print("\tINVALID OPERATOR VALUE!")

if operation == 1:
    print("Okay, now enter your first number:")
    num1 = int(input())
    print("And the second number:")
    num2 = int(input())
    if num1 == 56 and num2 == 9:
        print("Result is = 77\n********** YOU ARE BUSTED **********")
    else:
        print("Result is = ", num1+num2)
        print("Thank you for using this calculator!")

if operation == 2:
    print("Okay, now enter your first number:")
    num1 = int(input())
    print("And the second number:")
    num2 = int(input())
    print("Result is = ", num1-num2)
    print("Thank you for using this calculator!")

if operation == 3:
    print("Okay, now enter your first number:")
    num1 = int(input())
    print("And the second number:")
    num2 = int(input())
    if num1 == 45 and num2 == 3:
        print("Result is = 555\n********** YOU ARE BUSTED **********")
    else:
        print("Result is = ", num1*num2)
        print("Thank you for using this calculator!")

if operation == 4:
    print("Okay, now enter your first number:")
    num1 = int(input())
    print("And the second number:")
    num2 = int(input())
    if num1 == 56 and num2 == 6:
        print("Result is = 4\n********** YOU ARE BUSTED **********!")
    else:
        print("Result is = ", num1/num2)
        print("Thank you for using this calculator!")