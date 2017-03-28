#Project Euler Problem 1

numSum = 0

for x in range(0,1000):
    if x % 3 == 0:
        numSum += x
    elif x % 5 == 0:
        numSum += x
        
print(numSum)