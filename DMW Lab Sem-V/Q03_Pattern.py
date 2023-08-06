def starPattern(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end="")
        print()

n = int(input("Enter the number of rows: "))
starPattern(n)