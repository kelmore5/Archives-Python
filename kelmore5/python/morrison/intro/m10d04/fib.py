import sys

def fib(n):
    print "BABIES!!!"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)      #This is recursion; doing the same work
                                    #over and over again. This is slow
                                    #because it of this.
def maserati(n):
    if n == 0:
        return [-1, 0]
    if n == 1:
        return [0, 1]
    f = maserati(n-1)
    return [f[1], f[0] + f[1]]


def fib2(n):
    return maserati(n)[1]


sys.setrecursionlimit(100000)
#print fib(5)
#n = int(sys.argv[1])
#print "fib(%s) = %s" %(n, fib(n))
#for k in range(20):
#    print "fib(%s) = %s" %(k, fib(k))

n = 10000
print "fib(%s) = %s" %(n, maserati(n))
