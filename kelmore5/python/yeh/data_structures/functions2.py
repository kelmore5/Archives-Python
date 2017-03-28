def numDigits(integer):
	return int(math.log(math.fabs(integer), 10))+1

numDigitsLambda = lambda integer : int(math.log(math.fabs(integer), 10))+1

def isFixedPoint(f, value):
	return f(value) == value

isFixedPointLambda = lambda f,value : f(value) == value

filter(lambda x: x > 5, [3,5,6,7,9]) #= 6, 7, 9

def scale(vector, scalar):
	result = []
	for n in vector:
		result += n*scalar
	return result

def scale2(vector, scalar):
	return map(lambda n: n*scalar, vector)

scaleLambda = lambda vector, scalar: map(lambda n: n*scalar, vector)

def longest(words):
	return generalMax(lambda s1, s2: len(s1) > len(s2) : words)

def generalMax(compare, array):
	highest = array[0]
	for a in array[1:]:
		if(compare(a, highest)):
			highest = a
	return highest

def stringMap(f, a):
	string = ""
	for b in a:
		string+= f(b)
	return string

reduce(lambda x,y : (x,y), [4,5,6,7], 90) #= ((((90, 4), 5),6),7)

def PI(nums):
	return reduce(lambda x,y: x*y, nums)

PILambda = lambda nums: reduce(lambda x,y: x*y, nums)
	
reduce(lambda x,y: [y]+x, [1,2,3,4], []) #=[4,3,2,1]

def count(key, lst):
	total = 0
	for n in lst:
		if key==n:
			total+=1
	return total

def cont(key, lst):
	return reduce(lambda next, curr: curr+(next==key), lst, 0)

countLmabda = lambda key, lst: reduce(lambda next, curr: curr +(next==key), lst, 0)
