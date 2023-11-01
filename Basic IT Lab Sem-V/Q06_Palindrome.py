def checkPalindrome(num):
    originalNum, reversedNum, rem = num, 0, 0
    while num > 0:
        rem = num % 10
        reversedNum = reversedNum * 10 + rem
        num = num // 10
    if reversedNum == originalNum:
        return True
    else:
        return False


n = int(input("Enter a number to check for palindrome: "))
print(checkPalindrome(n))
