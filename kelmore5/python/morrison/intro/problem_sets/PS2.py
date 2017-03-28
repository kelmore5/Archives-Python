##################################################################
#    
#    Author:
#    Date:
#    Assignmemnt PS2.py
#    
#############CODE YOUR FUNCTIONS HERE##############################
# 0.  Example:  
def f2c(tempF):
    """precondition:   tempF is a number
postcondition:  returns tempF converted to centigrade"""
    return 5.0/9.0*(tempF - 32)
# 1.  
def c2f(tempC):
    """precondition:   tempC is a number
postcondition:  returns tempC converted to farenheit"""
    return (5.0/(9.0*tempC))+32
#2.
def getEven(x):
    """prec: x is a nonempty list of numbers
postc:  returns the sum of the elements in the list with even index."""
    evens = [k for k in x if k % 2 == 0]
    return 0
#3.
def lastInAlpha(x):
    """prec: x is a list of strings of alpha characters
postc:  returns the string last in alphabetical order after
it has been made lower-case"""
    return "TODO"
#4. 
def verticalClimb(distance, angle):
    """precondition:  You proceed along the hypteneuse of a right
triangle for the distance distance and with angle of inclination angle, 
which is given in degrees. 
postcondition:  returns the distance you climbed vertically. """
#5. You can write a couple of functions here to test summer on. 
##here is a freebie
def noah(x):
    return x*x*x
def summer(n, f):
    """precondition: n is a nonnegative number and f is a function
whose domain includes the nonnegative integres
postcondition:  returns sum( f(k),  k = 1..n) """
    return 0
#6  Hint:  look at what happens when you write s = list(s)
def lastCharInAlpha(s):
    """precondition: s is a string of alpha characters
postcondition:   returns the last character in alphabetical order
in lower-case"""
    return "TODO"
#7  Hint: List comprension, or a use of string methods
def disenvowel(s):
    """precondition:  s is a string of lower-case characters or spaces
postcondition: returns a copy of s with all vowels removed, and 
spaces preserved.   """
    return "TODO"
#8
def headAndFoot():
    """precondition:  s is a string containing lower-case words and spaces
The string s contains no non-alpha characters.
postcondition:  For each word, capitalize the first and last letter.  
If a word is one letter, just capitalize it.  """
    return "TODO"
#9
def ordinal(s):
    """precondition:  s is a single alpha character, lower or upper case
postcondition:   returns s's position in the alphabet.  See
the test code below """
    return 0
#10
def splat(h):
    """precondition:  h is a height in meters.
postcondition:  returns the speed at which an item dropped from 
height h hits the ground.  Splat! """
    return 0

###################TEST CODE GOES HERE##############################
##Begin here! Look at your functions and develop tests before
##you create the function's code.  This is your best protection
##against crash and burn.....
print "***********************Problem 0 Test Code:***********************"
t = 212
print "f2c(%5.4fs) = %5.4f, expected: %5.4f" %(t, f2c(t), 100)
t = -40
print "f2c(%5.4fs) = %5.4f, expected: %5.4f" %(t, f2c(t), -40)
t = 32
print "f2c(%5.4fs) = %5.4f, expected: %5.4f" %(t, f2c(t), 0)
print "***********************Problem 1 Test Code:***********************"
print "***********************Problem 2 Test Code:***********************"
print "***********************Problem 3 Test Code:***********************"
print "***********************Problem 4 Test Code:***********************"
print "***********************Problem 5 Test Code:***********************"
print "***********************Problem 6 Test Code:***********************"
print "***********************Problem 7 Test Code:***********************"
print "***********************Problem 8 Test Code:***********************"
print "***********************Problem 9 Test Code:***********************"
t = "C"
print "ordinal(%s) = %s, expected: %s" %(t, ordinal(t), 3)
t = "c"
print "ordinal(%s) = %s, expected: %s" %(t, ordinal(t), 3)
print "***********************Problem 10 Test Code:**********************"

