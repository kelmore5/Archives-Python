def abs(x):     ## to define f(x), Boss statement (owns indented code)
    """prec: x is an integer
postc: returns x if x is positive, -x if x is negative"""
    return x if x >= 0 else -x

def abs1(x):
    """prec: x is an integer
postc: returns x if x is positive, -x if x is negative"""
    if x < 0:   ## if x < 0
        x = -x  ## x gets -x, worker statement, complete sentence
    return x
    
x = -5
print "The absolute value of %s is %s, expected: %s" %(x, abs(x), 5)
x = 5
print "The absolute value of %s is %s, expected: %s" %(x, abs(x), 5)
x = 0
print "The absolute value of %s is %s, expected: %s" %(x, abs(x), 0)

x = -5
print "The absolute value of %s is %s, expected: %s" %(x, abs1(x), 5)
x = 5
print "The absolute value of %s is %s, expected: %s" %(x, abs1(x), 5)
x = 0
print "The absolute value of %s is %s, expected: %s" %(x, abs1(x), 0)


