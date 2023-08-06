def factorial(n):
    if n < 0:
        return "Not Defined"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact

inp = int(input("Enter a number to find its factorial: "))
print(inp,"! =",factorial(inp))
