import os
import os.path
##################################################################
#    
#    Author:
#    Date:
#    Assignmemnt PS3.py
#    
#############CODE YOUR FUNCTIONS HERE##############################
# 0.  Example:  
def f2c(tempF):
    """precondition:   tempF is a number
postcondition:  returns tempF converted to centigrade"""
    return 5.0/9.0*(tempF - 32)
# 1.  
def biggestWord(someString):
    """precondition:   someString is a string
postcondition: returns the biggest word (contiguous string of 
non-whitespace charcters) in someString"""
    return ""
#2.
def tableRow(x):
    """precondition:   x is a list of any python objects
postcondition: returns a string containing an HTML table row
of the objects. Cast each to a string so things print nicely and so
Python doesn't hiss. """
    return "" 
#3.
def absolutePath(x):
    """precondition:   x is a file name (string)
postcondition:  returns the absolute path of the file if it
exiss in the cwd and the Python graveyard object None otherwise."""
    return "TODO"
#4.  Hint:  use recursion. This is easy to do if the list is empty.  Then
#    break the list into the first element and the rest of the list.
def sumFrom(n, x):
    """precondition:   n is a positive integer and x is a list of integers.
postcondition:   returns a sublist of x that sums to n if it exists, or
False otherwise.
"""
#5. 
def lookForLove(word, dir):
    """precondition:   word is a string and dir is a directory.
postcondition: This checks all of the regular files (not directories)
in the directory dir for the presence of the string word.  It returns
a list of those containing it."""
    return []
#6  
def oiler(n):
    """precondition:   n is an integer
postcondition: returns the sum of the integers 1-n which 
are divisible by 2 or 3 but not 5"""
#7  Hint: List comprension, or a use of string methods
def isPrime(n):
    """precondition:   n is a nonzero integer
postcondition:  returns False if n is 1 or -1, True if n or -n is
prime, and False otherwise"""
    return None
#8
def primeFactorization(n):
    """precondition:   n is an integer, n > 0
postcondition:  returns a list of prime integers whose product is n"""
#9
def notDone(s):
    """precondition:   
postcondition: """
    return 0
#10
def notDone(h):
    """precondition:   
postcondition: """
    return 0

###################TEST CODE GOES HERE##############################
##Begin here! Look at your functions and develop tests before
##you create the function's code.  This is your best protection
##against crash and burn.....
print "***********************Problem 0 Test Code:***********************"
t = 212
print "f2c(%s) = %s, expected: %s" %(t, f2c(t), 100)
t = -40
print "f2c(%s) = %s, expected: %s" %(t, f2c(t), -40)
t = 32
print "f2c(%s) = %s, expected: %s" %(t, f2c(t), 0)
print "***********************Problem 1 Test Code:***********************"
x = "Computer Abcdefgh Science, pizza, and Droids are awesome!"
print "biggestWord(%s) = %s, expected: %s" %(x, biggestWord(x), "Computer")
print "***********************Problem 2 Test Code:***********************"
x = [2,3,4,5]
print "tableRow(%s) = %s, expected:  %s" % (x, tableRow(x), "<tr><td>2</td><td>3</td><td>4</td><td>5</td></tr>")
print "***********************Problem 3 Test Code:***********************"
print "***********************Problem 4 Test Code:***********************"
print "***********************Problem 5 Test Code:***********************"
print "***********************Problem 6 Test Code:***********************"
print "***********************Problem 7 Test Code:***********************"
print "***********************Problem 8 Test Code:***********************"
print "***********************Problem 9 Test Code:***********************"
print "***********************Problem 10 Test Code:**********************"

