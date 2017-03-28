#Project Euluer Problem 4

def checkPalindrome(num):
    stringify = str(num)
    pos = 0
    while pos <= len(stringify)/2:
        if stringify[pos] != stringify[(len(stringify)-1-pos)]:
            return False
        pos += 1
    return True

num1 = 999
num2 = 999
product = num1 * num2

largestPalindrome = 0

x = 0

while num1 > 900:
    while num2 > 900:
        check = num1*num2
        if checkPalindrome(check):
            if check > largestPalindrome:
                largestPalindrome = check
            else:
                break
        num2 -=1
    num2 = 999
    num1 -= 1
print(largestPalindrome)
