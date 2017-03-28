#Project Euler Problem 2

numSum = 0
a = 1
b = 1
fibo = 0

while b < 4000000:
    if b % 2 == 0:
        numSum += b
    b += a
    a = b - a
        
print(numSum)