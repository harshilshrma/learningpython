def checkPalindrome(n):
    originalNum, reversedNum, rem = n, 0, 0
    while (n > 0):
        rem = n % 10
        reversedNum = reversedNum*10 + rem
        n = n // 10
    if reversedNum == originalNum:
        return True
    else:
        return False

n = int(input("Enter a number to check for palindrome: "))
print(checkPalindrome(n))