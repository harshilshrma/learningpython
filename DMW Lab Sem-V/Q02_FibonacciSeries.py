def fibonacci(num):
    n1, n2, count = 0, 1, 0
    if num <= 0:
        return "Invalid Entry!"
    if num == 1:
        return n1
    if num == 2:
        return n2
    else:
        while count < num:
            print(n1)
            new = n1 + n2
            # updating value
            n1 = n2
            n2 = new
            count += 1


n = int(input("Enter the number of terms for Fibonacci Series: "))
print("The Fibonacci Sequence for", n, "number of terms:")
print(fibonacci(n))
