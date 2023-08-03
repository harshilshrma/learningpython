# # # Exercise 4
# # # Pattern Printing
# # # Input = Integer n
# # # Boolean = True or False
# # #
# # # True n=5
# # # *
# # # **
# # # ***
# # # ****
# # #
# # # False n=5
# # # ****
# # # ***
# # # **
# # # *
# #

#MY SOLUTION
A = 5
B = 1

number_of_lines = int(input("Enter the number of lines that you want in your star system (from 1 to 10): "))
while True:
    if number_of_lines > 10 or number_of_lines < 1:
        print("INVALID ENTRY!\nTHE ENTERED NUMBER IS OUT OF RANGE!\nTERMINATING THE PROGRAM...")
        print("\t\t\t\t\t\t***** Astrologer's Stars *****")
        break
    if number_of_lines == 1:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break

    if number_of_lines == 2:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*\n**")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("**\n*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break

    if number_of_lines == 3:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*\n**\n***")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("***\n**\n*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break

    if number_of_lines == 4:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*\n**\n***\n****")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("****\n***\n**\n*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break

    if number_of_lines == 5:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*\n**\n***\n****\n*****")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("*****\n****\n***\n**\n*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break

    if number_of_lines == 6:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*\n**\n***\n****\n*****\n******")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("******\n*****\n****\n***\n**\n*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break

    if number_of_lines == 7:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*\n**\n***\n****\n*****\n******\n*******")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("*******\n******\n*****\n****\n***\n**\n*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break

    if number_of_lines == 8:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*\n**\n***\n****\n*****\n******\n*******\n********")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("********\n*******\n******\n*****\n****\n***\n**\n*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break

    if number_of_lines == 9:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*\n**\n***\n****\n*****\n******\n*******\n********\n*********")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("*********\n********\n*******\n******\n*****\n****\n***\n**\n*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break

    if number_of_lines == 10:
        number_input = int(input("QUICK QUESTION: (This will determine the orientation of your star system!)\n"
                                 "\tThere are two numbers 'A' & 'B'. Which one do you think is greater in value?\n"
                                 "\tIf you think it's 'A': Press 1 or,\n\tIf you think it's 'B': Press 2\n\t"
                                 "Enter your choice: "))
        if number_input == 1:
            condition_1 = A > B
            print("This is", condition_1, "- Wow!")
            print("Because you guessed right (a=5 & b=1), you will get a correct star system.\n")
            print("*\n**\n***\n****\n*****\n******\n*******\n********\n*********\n**********")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        elif number_input == 2:
            condition_2 = A < B
            print("This is", condition_2, "- Oops!")
            print("Because you guessed wrong (a=5 & b=1), you will get an upside down star system.\n")
            print("**********\n*********\n********\n*******\n******\n*****\n****\n***\n**\n*")
            print("\nThank you for using this program!")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break
        else:
            print("Invalid value!\nTERMINATING THE PROGRAM...")
            print("\t\t\t\t\t\t***** Astrologer's Stars *****")
            break


#VIDEO SOLUTION1
# print("How Many Row You Want To Print")
# one= int(input())
# print("Type 1 Or 0")
# two = int(input())
# new =bool(two)
# if new == True:
#     for i in range(1,one+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new ==False:
#     for i in range(one,0,-1):
#         for j in range(1,i+1):
#             print("*", end=" ")
#         print()
# two = 1 or 0
# new = bool(two)
# print(new)

#VIDEO SOLUTION2
# a = int(input("please add number of line you want to print"))
# b = bool(int(input("please add 0 for False")))
#
#
# def star(a, b):
#     if b == True:
#         c = 1
#         while c <= a:
#             print(c * "*")
#             c = c + 1
#     else:
#         while a > 0:
#             print(a * "*")
#             a = a - 1
#
#
# star(a, b)