##################################################################
#    
#    Author: Kyle Elmore
#    Updated: 10/16/11
#    Project Euler Problems
#    
##################################################################
#1
def divisibility35(x):
	x = range(x)
	x = [k for k in x if k % 3 == 0 or k % 5 == 0]
	return sum(x)

def Fibonacci(x):
    x = range(x+1)

#13
def firsttenofsum(x):
    """postcondition: returns the first 10 digits
of the sum of a text file containing a list of numbers
seperated by enters"""
    a = open(x, "r")
    a = a.read()
    a = a.split("\n")
    a = [int(k) for k in a]
    a = sum(a)
    a = str(a)
    return a[:10]

#20
def sumFact(x):
        """precondition: x is an integer
postcondition: returns the sum of the digits of the factorial of x"""
        factorial = 1
        x = range(1,101)
        for n in x:
                factorial *= n
        factorial = str(factorial)
        factorial = list(factorial)
        factorial = [int(k) for k in factorial]
        return sum(factorial)
