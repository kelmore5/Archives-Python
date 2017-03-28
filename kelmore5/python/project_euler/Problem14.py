#Project Euluer Problem 14

numberRange = range(1,1000000)

def countCollatzNums(n):
	count = 0
	print(n)
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n +1
		if n in numberRange:
			numberRange.remove(n)
		count += 1
	return count

largestCount = 0
i = 0

while i < len(numberRange):
	temp = countCollatzNums(numberRange[i])
	if temp > largestCount:
		largestCount = temp
	i += 1
        
print(temp, largestCount)
