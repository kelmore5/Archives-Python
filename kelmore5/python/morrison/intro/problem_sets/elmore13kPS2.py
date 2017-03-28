##################################################################
#    
#    Author: Kyle Elmore
#    Date: 10/3/11
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
    return (9.0*tempC)/5.0 + 32
#2.
def getEven(x):
    """prec: x is a nonempty list of numbers
postc:  returns the sum of the elements in the list with even index."""
    evens = [k for k in x if k%2 == 0]
    return sum(evens)
#3.
def lastInAlpha(x):
    """prec: x is a list of strings of alpha characters
postc:  returns the string last in alphabetical order after
it has been made lower-case"""
    x = [k.lower() for k in x]
    x.sort()
    return x[-1]
#4. 
def verticalClimb(distance, angle):
    """precondition:  You proceed along the hypteneuse of a right
triangle for the distance distance and with angle of inclination angle, 
which is given in degrees. 
postcondition:  returns the distance you climbed vertically. """
    import math
    return distance*math.sin(math.radians(angle))
    
#5. You can write a couple of functions here to test summer on. 
##here is a freebie
def noah(x):
    return x*x*x
def square(x):
    return x*x
def inverse(x):
    if x == 0:
        return "Divide by zero error"
    return 1/x
def squareroot(x):
    if x < 0:
        return "Error"
    return x**.5
def summer(n, f):
    """precondition: n is a nonnegative number and f is a function
whose domain includes the nonnegative integers
postcondition:  returns sum( f(k),  k = 1..n) """
    rangeint = range(1,n+1)
    function = [f(k) for k in rangeint]
    rangeint = sum(rangeint)
    function = sum(function)
    return rangeint + function
#6  Hint:  look at what happens when you write s = list(s)
def lastCharInAlpha(s):
    """precondition: s is a string of alpha characters
postcondition:   returns the last character in alphabetical order
in lower-case"""
    s = list(s)
    s = [k.lower() for k in s]
    s.sort()
    return s[-1]
#7  Hint: List comprension, or a use of string methods
def disenvowel(s):
    """precondition:  s is a string of lower-case characters or spaces
postcondition: returns a copy of s with all vowels removed, and 
spaces preserved.   """
    s = [k for k in s if k != "a" and k != "e" and k != "i" and k != "o" and k != "u"]
    return "".join(s)
#8
def headAndFoot(s):
    """precondition:  s is a string containing lower-case words and spaces
The string s contains no non-alpha characters.
postcondition:  For each word, capitalize the first and last letter.  
If a word is one letter, just capitalize it.  """
    if len(s) == 0:
        pass
    else:
        x = len(s)
        s = s.split(" ")
        y = s.pop(0)
        s = " ".join(s)
        y = list(y)
        y[0] = y[0].upper()
        y[-1] = y[-1].upper()
        y = "".join(y)
        y += " %s" %headAndFoot(s)
        return y[0:x]
#9
def ordinal(s):
    """precondition:  s is a single alpha character, lower or upper case
postcondition:   returns s's position in the alphabet.  See
the test code below """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.find(s.lower())+1
#10
def splat(h):
    """precondition:  h is a height in meters.
postcondition:  returns the speed at which an item dropped from 
height h hits the ground.  Splat! """
    return 9.81*(((2*h)/9.81)**.5)

###################TEST CODE GOES HERE##############################
##Begin here! Look at your functions and develop tests before
##you create the function's code.  This is your best protection
##against crash and burn.....

print "***********************Problem 0 Test Code:***********************"
t = 212
print "f2c(%5.4f) = %5.4f, expected: %5.4f" %(t, f2c(t), 100)
t = -40
print "f2c(%5.4f) = %5.4f, expected: %5.4f" %(t, f2c(t), -40)
t = 32
print "f2c(%5.4f) = %5.4f, expected: %5.4f" %(t, f2c(t), 0)

print "***********************Problem 1 Test Code:***********************"
t = 100
print "c2f(%s) = %s, expected: %s" %(t, c2f(t), 212)
t = -40
print "c2f(%s) = %s, expected: %s" %(t, c2f(t), -40)
t = 0
print "c2f(%s) = %s, expected: %s" %(t, c2f(t), 32)

print "***********************Problem 2 Test Code:***********************"
num = [1,2,3,4,5,6,7,8,9,10]
print "getEven(%s) = %s, expected: %s" %(num, getEven(num), 30)
num = [0,2,4,6]
print "getEven(%s) = %s, expected: %s" %(num, getEven(num), 12)
num = [1,3,5,7]
print "getEven(%s) = %s, expected: %s" %(num, getEven(num), 0)

print "***********************Problem 3 Test Code:***********************"
alpha = ["Snape", "Salazar", "Godfrey", "Potter", "Weasley", "Granger"]
print "lastInAlpha(%s) = %s, expected: %s" %(alpha, lastInAlpha(alpha), "weasley")
alpha = ["gloom", "despair", "american", "studies", "death"]
print "lastInAlpha(%s) = %s, expected: %s" %(alpha, lastInAlpha(alpha), "studies")
alpha = ["Pizza", "Hut", "is", "awesome"]
print "lastInAlpha(%s) = %s, expected: %s" %(alpha, lastInAlpha(alpha), "pizza")

print "***********************Problem 4 Test Code:***********************"
distance =  6
angle = 30
print "verticalClimb(%s, %s) = %s, expected: %s" %(distance, angle, verticalClimb(distance, angle), 3)
distance =  0
angle = 0
print "verticalClimb(%s, %s) = %s, expected: %s" %(distance, angle, verticalClimb(distance, angle), 0)
distance =  5
angle = 90
print "verticalClimb(%s, %s) = %s, expected: %s" %(distance, angle, verticalClimb(distance, angle), 5)

print "***********************Problem 5 Test Code:***********************"
num = 0
function = squareroot
print "summer(%s, %s) = %s, expected: %s" %(num, "squareroot()", summer(num, function), 0)
num = 4
function = noah
print "summer(%s, %s) = %s, expected: %s" %(num, "squareroot()", summer(num, function), 110)
num = 1
function = inverse
print "summer(%s, %s) = %s, expected: %s" %(num, "squareroot()", summer(num, function), 2)

print "***********************Problem 6 Test Code:***********************"
string = "floccinaucinihilipilification"
print "lastCharInAlpha(%s) = %s, expected: %s" %(string, lastCharInAlpha(string), "u")
string = "We shall fight for bovine freedom"
print "lastCharInAlpha(%s) = %s, expected: %s" %(string, lastCharInAlpha(string), "w")

print "***********************Problem 7 Test Code:***********************"
s = "This is a string"
print "disenvowel(%s) = %s, expected: %s" %(s, disenvowel(s), "Ths s  strng")
s = "kslkdkjf     "
print "disenvowel(%s) = %s, expected: %s" %(s, disenvowel(s), "kslkdkjf     ")
s = "     "
print "disenvowel(%s) = %s, expected: %s" %(s, disenvowel(s), "     ")
s = "aeiouaeiou"
print "disenvowel(%s) = %s, expected: %s" %(s, disenvowel(s), "")

print "***********************Problem 8 Test Code:***********************"
s = "It is dangerous to go alone so have a cookie"
print "headAndFoot(%s) = %s, expected: %s" %(s, headAndFoot(s), "IT IS DangerouS TO GO AlonE SO HavE A CookiE")
s = "a"
print "headAndFoot(%s) = %s, expected: %s" %(s, headAndFoot(s), "A")

print "***********************Problem 9 Test Code:***********************"
t = "C"
print "ordinal(%s) = %s, expected: %s" %(t, ordinal(t), 3)
t = "c"
print "ordinal(%s) = %s, expected: %s" %(t, ordinal(t), 3)

print "***********************Problem 10 Test Code:**********************"
h = 0
print "splat(%s) = %s, expected: %s" %(h, splat(h), 0)
h = 5
print "splat(%s) = %s, expected: %s" %(h, splat(h), 9.9045)

