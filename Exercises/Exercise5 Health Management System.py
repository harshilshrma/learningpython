def getdate():
    import datetime
    return datetime.datetime.now()

print("\t\t\t\t\t\t***** HEALTH MANAGEMENT SYSTEM *****")
print("\t\t\t\t\t\t\t\t\t  Welcome!\nHere you can log or retrieve, exercise and diet data of John, Sam and Steve.")
print("\n\tINSTRUCTIONS for User Input: If you are John  - Press 1 and click 'Enter'\n"
      "\t\t\t\t\t\t\t\t If you are Sam   - Press 2 and click 'Enter'\n"
      "\t\t\t\t\t\t\t\t If you are Steve - Press 3 and click 'Enter'")
username = int(input("\tPlease enter a valid User Input Number: "))

while True:
    if username == 1:
        print("\nHey John, Welcome back!\n\nSo, what do you want to do right now?"
              "\n\tIf you want to make a new entry, Press 1"
              "\n\tOr, if you just want to have a look at your data, Press 2.")
        log_retrieve = int(input("Enter your choice: "))

        if log_retrieve == 1:
            print("\nIn which file do you want to add a new entry?"
                  "\n\tFor Exercise File, Press 1, or,"
                  "\n\tFor Diet File, Press 2.")
            file_choose = int(input("Enter your choice: "))

            if file_choose == 1:
                print("\nFine, so you want to add a new entry in your Exercise File.")
                entry1 = input("Enter the exercise that you want to add: ")
                f1 = open("../Tutorial Files/john_exercise.txt", "a")
                f1.write(str(getdate()) + " - " + entry1.capitalize() + "\n")
                f1.close()
                print("\nDone! Your entry has been made in the Exercise File.")
                print("\n\nThank you for using this program!\nWe hope to see you soon.")
                break
            if file_choose == 2:
                print("\nFine, so you want to add a new entry in your Diet File.")
                entry2 = input("Enter the food item that you want to add: ")
                f2 = open("../Tutorial Files/john_diet.txt", "a")
                f2.write(str(getdate()) + " - " + entry2.capitalize() + "\n")
                f2.close()
                print("\nDone! Your entry has been made in the Diet File.")
                print("\n\nThank you for using this program!\nWe hope to see you soon.")
                break
            else:
                print("INVALID ENTRY")
                break

        if log_retrieve == 2:
            print("\nWhich file do you want to see?\n\tFor Exercise File, Press 1, or,\n\tFor Diet File, Press 2.")
            file_choose = int(input("Enter your choice: "))

            if file_choose == 1:
                print("\nOkay, here is your Exercise File:\n")
                f3 = open("../Tutorial Files/john_exercise.txt")
                print(f3.read())
                f3.close()
                print("Thank you for using this program!\nWe hope to see you soon.")
                break
            if file_choose == 2:
                print("\nOkay, here is your Diet File:\n")
                f4 = open("../Tutorial Files/john_diet.txt")
                print(f4.read())
                f4.close()
                print("Thank you for using this program!\nWe hope to see you soon.")
                break
            else:
                print("INVALID ENTRY")
                break

        else:
            print("INVALID ENTRY")
            break


    if username == 2:
        print("\nHey Sam, Welcome back!\n\nSo, what do you want to do right now?"
              "\n\tIf you want to make a new entry, Press 1"
              "\n\tOr, if you just want to have a look at your data, Press 2.")
        log_retrieve = int(input("Enter your choice: "))

        if log_retrieve == 1:
            print("\nIn which file do you want to add a new entry?"
                  "\n\tFor Exercise File, Press 1, or,"
                  "\n\tFor Diet File, Press 2.")
            file_choose = int(input("Enter your choice: "))

            if file_choose == 1:
                print("\nFine, so you want to add a new entry in your Exercise File.")
                entry1 = input("Enter the exercise that you want to add: ")
                f1 = open("../Tutorial Files/sam_exercise.txt", "a")
                f1.write(str(getdate()) + " - " + entry1.capitalize() + "\n")
                f1.close()
                print("\nDone! Your entry has been made in the Exercise File.")
                print("\n\nThank you for using this program!\nWe hope to see you soon.")
                break
            if file_choose == 2:
                print("\nFine, so you want to add a new entry in your Diet File.")
                entry2 = input("Enter the food item that you want to add: ")
                f2 = open("../Tutorial Files/sam_diet.txt", "a")
                f2.write(str(getdate()) + " - " + entry2.capitalize() + "\n")
                f2.close()
                print("\nDone! Your entry has been made in the Diet File.")
                print("\n\nThank you for using this program!\nWe hope to see you soon.")
                break
            else:
                print("INVALID ENTRY")
                break

        if log_retrieve == 2:
            print("\nWhich file do you want to see?\n\tFor Exercise File, Press 1, or,\n\tFor Diet File, Press 2.")
            file_choose = int(input("Enter your choice: "))

            if file_choose == 1:
                print("\nOkay, here is your Exercise File:\n")
                f3 = open("../Tutorial Files/sam_exercise.txt")
                print(f3.read())
                f3.close()
                print("Thank you for using this program!\nWe hope to see you soon.")
                break
            if file_choose == 2:
                print("\nOkay, here is your Diet File:\n")
                f4 = open("../Tutorial Files/sam_diet.txt")
                print(f4.read())
                f4.close()
                print("Thank you for using this program!\nWe hope to see you soon.")
                break
            else:
                print("INVALID ENTRY")
                break

        else:
            print("INVALID ENTRY")
            break


    if username == 3:
        print("\nHey Steve, Welcome back!\n\nSo, what do you want to do right now?"
              "\n\tIf you want to make a new entry, Press 1"
              "\n\tOr, if you just want to have a look at your data, Press 2.")
        log_retrieve = int(input("Enter your choice: "))


        if log_retrieve == 1:
            print("\nIn which file do you want to add a new entry?"
                  "\n\tFor Exercise File, Press 1, or,"
                  "\n\tFor Diet File, Press 2.")
            file_choose = int(input("Enter your choice: "))

            if file_choose == 1:
                print("\nFine, so you want to add a new entry in your Exercise File.")
                entry1 = input("Enter the exercise that you want to add: ")
                f1 = open("../Tutorial Files/steve_exercise.txt", "a")
                f1.write(str(getdate()) + " - " + entry1.capitalize() + "\n")
                f1.close()
                print("\nDone! Your entry has been made in the Exercise File.")
                print("\n\nThank you for using this program!\nWe hope to see you soon.")
                break
            if file_choose == 2:
                print("\nFine, so you want to add a new entry in your Diet File.")
                entry2 = input("Enter the food item that you want to add: ")
                f2 = open("../Tutorial Files/steve_diet.txt", "a")
                f2.write(str(getdate()) + " - " + entry2.capitalize() + "\n")
                f2.close()
                print("\nDone! Your entry has been made in the Diet File.")
                print("\n\nThank you for using this program!\nWe hope to see you soon.")
                break
            else:
                print("INVALID ENTRY")
                break

        if log_retrieve == 2:
            print("\nWhich file do you want to see?\n\tFor Exercise File, Press 1, or,\n\tFor Diet File, Press 2.")
            file_choose = int(input("Enter your choice: "))

            if file_choose == 1:
                print("\nOkay, here is your Exercise File:\n")
                f3 = open("../Tutorial Files/steve_exercise.txt")
                print(f3.read())
                f3.close()
                print("Thank you for using this program!\nWe hope to see you soon.")
                break
            if file_choose == 2:
                print("\nOkay, here is your Diet File:\n")
                f4 = open("../Tutorial Files/steve_diet.txt")
                print(f4.read())
                f4.close()
                print("Thank you for using this program!\nWe hope to see you soon.")
                break
            else:
                print("INVALID ENTRY")
                break

        else:
            print("INVALID ENTRY")
            break

    else:
        print("INVALID ENTRY")
        break



"""

Video's Solution

# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


#bhai ye rha program
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")
print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)
  
"""

