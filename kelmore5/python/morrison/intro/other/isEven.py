def isEven(x):
    if x == 0:
        return False
    elif x % 2 == 0:
        return True
    else:
        return False

print "Test Code"
x = 5
print "isEven(%s), %s, expected: %s" %(x, isEven(x), "False")
x = 0
print "isEven(%s), %s, expected: %s" %(x, isEven(x), "False")
x = 4
print "isEven(%s), %s, expected: %s" %(x, isEven(x), "True")
