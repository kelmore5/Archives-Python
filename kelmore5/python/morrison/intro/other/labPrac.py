import math
##The smart way to do this:
#   Get problems 1 and 2.  It's a 3. Take a bite of the others, nice B.
#   Attempt one of 3 or 4.  You are in great shape if you do this!
#   Number 5 is a bit of a twit.  But it can give you a superman 5.  
##fairly easy
def vowelMole(x):
    """prec: x is a string
postc: returns a string with all all vowels (except y) in order in 
the string.  Case must be preserved."""
    x = [k for k in x if k == "a" or k == "e" or k == "i" or k == "o" or k == "u"]
    return "".join(x)
#fairly easy. Get Problems 1 and 2 and you have a 3 (B-)
def biggestSine(listOfFloats):
    """prec: x is a list of floats.  
postc:  returns the largest sine of the list of floats"""
    import math
    x = listOfFloats
    x = [math.sin(k) for k in x]
    x.sort()
    return x[-1]
#medium: the first three earn a 4.  that's an A-
def fib(n):
    """prec: n is a non-negative integer.
post: returns the nth fibonacci number.  F'rinstance,
f(0) = 0, f(1) = 1, f(2) = 1, f(3) = 2, each f(n) = sum(f of its two 
predecessors  You may use a loop or recursion, but recursion is 
mucho slower."""
    return 0
#medium:  1,2,4 make a 4. A-
def sinSum(n, x):
    """prec: n is a non-negative integer, x is a float.
post: returns sin(x) + sin(2*x) + sin(3*x) + ..... sin(n*x)
"""
    return 0
#medium:  1,2,5 make a 4. A-
def lard(bacon, meat):
    """meat is a string, bacon is a single character.  
postc: return a list that "lards" the bacon through the meat. for
example, lard("a", "bcd") returns the list
["abcd", "bacd", "bcad", "bacd"]"""
    return []
#challenging:  Get this and have a 5 if you get two others!
#problems you pick.  That's a solid A+. Ingenious solutions
#are described on letter of rec.
def findAllAnagrams(someString):
    """"finds all anagarams on a string with distinct characters.
It returns them in a list.  HINT: Use lard and recursion!"""
    someString = list(someString)
    
    return []

if __name__ == "__main__":
    word = "panoply"
    print "vowelMole(%s) = %s, expected: ao" %(word, vowelMole(word))
    word = "This is a test. It is only a test."
    print "vowelMole(%s) = %s, expected: iiaeIioae" %(word, vowelMole(word))
    word = "amanaplanacanalpanama"
    print "vowelMole(%s) = %s, expected: aaaaaaaaaa" %(word, vowelMole(word))
    listOfFloats = [0, .785, -.785]
    print "biggestSine(%s) = %s, expected: .707" %(listOfFloats, biggestSine(listOfFloats))
    x = [.521, .4, 0] 
    print "biggestSine(%s) = %s, expected: .5" %(x, biggestSine(x))
    x = [3.142, 4.3, 5.1] 
    print "biggestSine(%s) = %s, expected: 0" %(x, biggestSine(x))
    n = 5
    print "fib(%s) = %s, expected: 5" %(n, fib(n))
    n = 12
    print "fib(%s) = %s, expected: 144"% (n, fib(n))
    n = 15
    print "fib(%s) = %s, expected: 610"% (n, fib(n))
    n, x = 10, math.pi
    print "sinSum(%s, %s) = %s, expected: 0"% (n, x, sinSum(n, x))
    n, x = 20, math.pi*.05
    print "sinSum(%s) = %s, expected: 9.61"% (n, sinSum(n, x))
    b = "a"
    m = "bcd"
    print "lard(%s, %s) = %s, expected: [abcd, bacd, bcad, bcda] " %(b, m, lard(b, m))    
    x = "abc"
    print "findAllAnagrams(%s) = %s, expected: [abc, cab, bca, cba, acb, bac]"%(x, findAllAnagrams(x))
    x = "abcdefgh"
    print "len(findAllAnagrams(%s)) = %s, expected: 40320"%(x, len(findAllAnagrams(x)))
