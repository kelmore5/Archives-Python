def f(x):
    z = "kerfuffle"
    print "inside f: ", dir()
    return x + 3
def g(x):
    print "inside g: ", dir()
    return x*x*x
def austintatious(moo):
    moo = moo + 1
def infidel(x):
    x[0] = 1.5
##This is the "main routine"
#print "just before the main routine, dir = ", dir()
#print "function demo"
#y = 4
#print "just after y is created, the main routine, dir = ", dir()
#print "f(%s) = %s" % (y, g(y))
#print "at the end, dir = ", dir()
#print z
cow = 14
print "cow = %s" % cow
print austintatious(cow)
print "cow = %s" % cow

nums = [2,3,4]
print "nums = %s" % nums
infidel(nums)
print "nums = %s" % nums
