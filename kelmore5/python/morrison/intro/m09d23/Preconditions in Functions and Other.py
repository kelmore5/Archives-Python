import math
def hypot(a,b):
    """precondition: a, b are numbers
postcondition: returns the length of the hypotenuse of a right triangle
with legs of length a and b."""
    return (a**2 + b**2)**(.5)
def thirdSide(a, b, theta):
    """precondition: a, b, and theta are numbers.
a and b are the side lengths of a triangle, and theta is an angle in
radians.
postcondition: returns the length of the third side"""
    return math.sqrt(a*a + b*b - 2*a*b*math.cos(theta))
