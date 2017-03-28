def postive(x):
    if x >= 0 and x <= 100:
        return True
    else:
        return False

x = -1
print "postive(%s) = %s, expected: %s" %(x, postive(x), "False")
x = 0
print "postive(%s) = %s, expected: %s" %(x, postive(x), "True")
x = 100
print "postive(%s) = %s, expected: %s" %(x, postive(x), "True")
x = 101
print "postive(%s) = %s, expected: %s" %(x, postive(x), "False")
