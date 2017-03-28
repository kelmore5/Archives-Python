def square(x):
    return x*x
def noah(x):
    return x*x*x
def oppositeSide(a, b, theta):
    #do law of cosines
    import math
    return math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(theta)))
    
if __name__ == "__main__":
    a = 7
    print "The cube of %s is %s and the cube of %s is %s" %(a, square(a), a, noah(a))
