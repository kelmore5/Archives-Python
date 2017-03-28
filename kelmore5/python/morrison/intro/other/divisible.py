def divisible(x):
    if x % 3 == 0 and x % 5 != 0:
        return True
    else:
        return False

x = 3
print "divisible(%s) = %s, expected: %s" %(x, divisible(x), "True")
x = 5
print "divisible(%s) = %s, expected: %s" %(x, divisible(x), "False")
x = 15
print "divisible(%s) = %s, expected: %s" %(x, divisible(x), "False")
