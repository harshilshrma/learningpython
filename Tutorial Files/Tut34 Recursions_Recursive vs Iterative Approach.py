# def print1(str1):
#     #print1(str1)
#     print("This is " + str1)
# print1("Harshil.")

# n! = n * n-1 * n-2 * n-3.....1
# n! = n * (n-1)!

def factorial_iterative(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.....1
    """
    fac = 1
    for i in range(n):           #i jayega 0 se n-1 tak
        fac = fac * (i+1)        #i+1 jayega 1 se n tak
    return fac

def factorial_recursive(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.....1
    """
    if n == 1 or n == 0:
        return  1
    else:
        return n * factorial_recursive(n-1)
        # 5 * factorial_recursive(4)
        # 5 * 4 * factorial_recursive(3)
        # 5 * 4 * 3 * factorial_recursive(2)
        # 5 * 4 * 3 * 2 * factorial_recursive(1)
        # 5 * 4 * 3 * 2 * 1 = 120

number = int(input("Enter the number: "))
print("Using Iterative method, it's factorial is:", factorial_iterative(number))
print("Using Recursive method, it's factorial is:", factorial_recursive(number))

# Fibonacci Series:
# 0 1 1 2 3 5 8 13 21 34 55 89

def fibonacci(m):
    if m == 1:
        return 0
    if m == 2:
        return 1
    else:
        return fibonacci(m-1) + fibonacci(m-2)

print("\nFibonacci Sequence: 0, 1, ...")
number2 = int(input("Enter the rank whose fibonacci number is desired: "))
print("At rank", number2, "the number according to the following fibonacci series is:", fibonacci(number2))