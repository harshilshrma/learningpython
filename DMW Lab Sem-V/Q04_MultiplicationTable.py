def multiplicationTabele(n):
    for i in range (1, 11):
        print(n,"x",i,"=",n*i)

n = int(input("Enter a number to generate its multiplication table: "))
multiplicationTabele(n)