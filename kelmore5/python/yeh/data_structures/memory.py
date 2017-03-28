def reverse(string):
	if(len(string) == 0):
		return ""
	else:
		return string[-1] + reverse(string[:-1])

def doubleAll(string):
	if(len(string) == 0):
		return ""
	else:
		return 2*string[0] + doubleAll(string[1:])

def count(letter, string):
	if(len(string) == 0):
		return 0
	else:
		return (letter == string[0]) + count(letter, string[1:])

def mosh(string):
	if(len(string) <= 1):
		return string
	else:
		return mosh(string[1:]) + string[0] + mosh(string[1:])

def pairs(str1, str2):
	return flatmap(lambda str1: map(lambda second: str1 + second, str2), str1)

def nTuples(sList):
	if(len(sList) == 0):
		return ['']
	else:
		firstSet = sList[0]
		partials = nTuples(sList[1:])
		result = flatmap(lambda first: map(lambda rest: first + rest, partials), firstSet)
		return result

def findnTupleSum(value, sList):
	if(len(sList) == 0):
		if value == 0:
			return []
		else:		
			return None
	for i in sList[0]:
		if(findnTupleSum(value-i, sList[1:])!=None):
			return [i]+findnTupleSum(value-i, sList[1:])

def allnTupleSums(value, sList):
	if(len(sList) == 0):
		if value == 0:
			return [[]]
		else:		
			return []
	result = []
	for i in sList[0]:
		for j in allnTupleSums(value-i, sList[1:]):
			result.append([i]+j)
	return result

def findPairSum(summ, list1, list2):
	return ""

def oneplus(x):
	return x+1

def flatmap(f, src):
	image = []
	for x in src:
		image += f(x)
	return image

f2 = lambda x: [2*x]

#print reverse("embargo")
#print doubleAll('ole')
#print count('a', 'bananarama')
#print mosh('c')
#print mosh('bc')
#print mosh('abc')
#print pairs('abc', 'de')
#print nTuples(['123', 'abc', 'def'])
#print findnTupleSum(33, [[1,3,5],[8,12],[19,22,25]])
print allnTupleSums(28, [[11], [9], [8]])

#print map(oneplus, [2,5,7])

#print flatmap(f2, [1,2,3])
