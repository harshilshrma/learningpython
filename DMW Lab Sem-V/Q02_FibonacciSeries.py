def fibonacci(n):
    n1, n2, count = 0, 1, 0
    if n <= 0:
        return "Invalid Entry!"
    if n == 1:
        return n1
    if n == 2:
        return n2
    else:
        while count < n:
            print(n1)
            nNew = n1 + n2
            #updating value
            n1 = n2
            n2 = nNew
            count += 1

n = int(input("Enter the number of terms for Fibonacci Series: "))
print("The Fibonacci Sequence for", n, "number of terms:")
print(fibonacci(n))