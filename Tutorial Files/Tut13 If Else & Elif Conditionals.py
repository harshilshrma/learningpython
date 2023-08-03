# var1 = 3
# var2 = 45
# var3 = int(input())
#
# if var3 > var2:
#     print("Greater")
# elif var3 == var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [5, 9, 10, 23, 45]
# print(15 in list1)
# if 15 in list1:
#     print("Yes, it's in the list.")
# else:
#     print("No, it's not in the list.\n")
#
# print(15 not in list1)
# if 15 not in list1:
#     print("Yes, it's not in the list.")
# else:
#     print("No, it's in the list.")

###QUIZ

print("Check if you are legal to drive or not.")
print("Enter your age:")
age = int(input())

if 99>=age>18:
    print("Congratulations! You are eligible to drive.\n")
if 4<=age<=17:
    print("Sorry, You are not eligible to drive.\n")
if age == 18:
    print("Sorry but you have to visit your nearest Driving Licence Authority,\nGovernment of India for special inspection.\n")
if age>99 or age<4:
    print("Invalid age!")
print("Thank you for using this engine.")

#HARRY'S SOLUTION
# print("enter your age:")
# age = int(input())
#
# if age<18:
#     print("You cant drive.")
# elif age==18:
#     print("we will think about you")
# else:
#     print("you can drive.")