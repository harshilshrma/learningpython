def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y


print("Calculator!")
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
print("\t1 for Addition\n\t2 for Subtraction\n\t3 for Multiplication\n\t4 for Division")
n = int(input("Enter your input: "))

if n == 1:
    print(x, "+", y, "=", x + y)
elif n == 2:
    print(x, "-", y, "=", x - y)
elif n == 3:
    print(x, "*", y, "=", x * y)
elif n == 4:
    print(x, "/", y, "=", x / y)
else:
    print("Invalid Entry!")
