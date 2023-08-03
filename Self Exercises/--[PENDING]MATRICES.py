print("\t\t**************** matriXO **************** ")
username = input("Welcome to matriXO! Please enter your name to continue: ")
print("Hey " + username.capitalize() + ", we are happy to have you here today.")
print("Which service would you like to avail?")

print("\t1. Determinant Calculator\n\t2. Inverse Calculator")
service_input = int(input("Please enter your choice: "))

while 1:
    if service_input == 1:
        print("\nDETERMINANT CALCULATOR")
        print("Okay so you want to calculate the value of a determinant, fine, we'll do that for you!")
        print("Please provide us the data of your determinant:")
        a11 = int(input("\tEnter a11: "))
        a12 = int(input("\tEnter a12: "))
        a13 = int(input("\tEnter a13: "))
        a21 = int(input("\tEnter a21: "))
        a22 = int(input("\tEnter a22: "))
        a23 = int(input("\tEnter a23: "))
        a31 = int(input("\tEnter a31: "))
        a32 = int(input("\tEnter a32: "))
        a33 = int(input("\tEnter a33: "))
        det_result = a11*((a22*a33)-(a32*a23)) - a12*((a21*a33)-(a31*a23)) + a13*((a21*a32)-(a31*a22))
        print("Value of this determinant is:", det_result)
        break

    else:
        print("INVALID ENTRY!\nABORTING SESSION...\n\t\t**************** matriXO **************** ")
        break