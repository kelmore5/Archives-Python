#Project Euluer Problem 6

numRange = range(1,101)
numSum = 0
numSquare = 0

for x in numRange:
    numSum += x
    numSquare += (x*x)
    
print(numSum * numSum - numSquare)
