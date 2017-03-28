#Project Euluer Problem 5

import math

divisors = [11,12,13,14,15,16,17,18,19,20]

def checkDivisible(n):
    for x in divisors:
        if n % x != 0:
            return False
    return True

num = 20
maxNum = 1

for x in divisors:
    maxNum *= x
    
print(maxNum)

while num < maxNum:
    if checkDivisible(num):
        break
    num += 20
    
print(num)
