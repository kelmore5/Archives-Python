import math

a = input("Enter the length of one side of the triangle:  ")
b = input("Enter the length of the other side of the triangle:  ")
theta = input("Enter the angle between the two sides of the triangle:  ")

print "You entered a = %s, b = %s, and angle theta = %s" %(a,b,theta)

c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))

print "The third side of the triangle, c, is %s:  " % c
