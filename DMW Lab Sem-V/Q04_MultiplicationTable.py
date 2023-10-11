def multiplicationTable(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


n = int(input("Enter a number to generate its multiplication table: "))
multiplicationTable(n)
