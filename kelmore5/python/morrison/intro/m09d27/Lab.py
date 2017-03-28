def mean(x):
    """precondition:  x is a numerical list
postcondition:  returns the average of the numbers is x"""
    return sum(x)/float(len(x))
def sumSquares(n):
    """precondition:  n is a nonnegative  integer
postcondition:  returns the sum of the squares of the integers 0-n"""
    n = range(n+1)
    n = [k*k for k in n]
    return sum(n)
def sumOdds(n):
    """precondition: n is a positive integer
postcondition: returns the sum of the first n odd integers"""
    return n*n
def biggestWordLength(text):
    """precondition:  text is a string
postcondition: returns the length of the longest word in x (do not worry about punctuation)"""
    return len(max(text.split(), key = len))
def biggestWord(text):
    """precondition:  text is a string
postcondition: returns the the longest word in x (do not worry about punctuation)"""
    return max(text.split(), key = len)
def biggestWord2(text):
    """precondition:  text is a string
postcondition: returns the the longest word in x (do not worry about punctuation)"""
    text = text.split()
    length = [len(k) for k in text]
    length = [k for k in length if len(k)==length.index(max(length))]
    return text[length.index(max(length))]
def biggestWord3(text):
    """precondition:  text is a string
postcondition: returns the the longest word in x (do not worry about punctuation)"""
    text = text.split()
    length = [len(k) for k in text]
    return text[length.index(max(length))]

if __name__ == "__main__":
    print "***********************Test code**************************"
    print "**********Test for mean**********"
    x = [0,1,6]
    print "The average of the numbers in %s is:  %s, expected: %s." %(x, mean(x), 2.333)
    x = [1,2,3]
    print "The average of the numbers in %s is:  %s, expected: %s." %(x, mean(x), 2)
    x = range(1,10)
    print "The average of the numbers in %s is:  %s, expected: %s." %(x, mean(x), 5)
    print "**********Test for sumSquares**********"
    n = 5
    print "The sum of the squares of the integers 0 to %s is:  %s, expected:  %s." %(n, sumSquares(n), 55)
    n = 3
    print "The sum of the squares of the integers 0 to %s is:  %s, expected:  %s." %(n, sumSquares(n), 14)
    n = 0
    print "The sum of the squares of the integers 0 to %s is:  %s, expected:  %s." %(n, sumSquares(n), 0)
    print "**********Test for sumOdds**********"
    n = 5
    print "The sum of the first %s odd integers is:  %s, expected:  %s." %(n, sumOdds(n), 9)
    n = 8
    print "The sum of the first %s odd integers is:  %s, expected:  %s." %(n, sumOdds(n), 12)
    print "********Test for biggestWordLength**********"
    text = "Fox and Socks is an awesome book."
    print "The length of the longest word in %s is:  %s, expected:  %s." %(text, biggestWordLength(text), 7)
    text = "Fox and Socks is an awesome book."
    print "**********Test for biggestWord**********"
    print "The longest word in %s is:  %s, expected:  %s." %(text, biggestWord(text), "awesome")
    text = "Fox and Socks is an awesome book."
    print "The longest word in %s is:  %s, expected:  %s." %(text, biggestWord2(text), "awesome")
    
