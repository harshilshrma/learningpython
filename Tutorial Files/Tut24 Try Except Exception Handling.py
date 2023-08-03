num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

try:
    print("The sum is = ", int(num1)+int(num2))
except Exception as a:
    print(a)

print("This is a very important line.")
