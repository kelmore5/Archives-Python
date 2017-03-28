def sumdigits(x):
    x = 2**x
    s = list(str(x))
    s = [int(k) for k in s]
    return sum(s)

def lastten(x):
    x = range(1, x+1)
    x = [k**k for k in x]
    x = sum(x)
    s = list(str(x))
    s = s[-10:]
    s = [int(k) for k in s]
    return s

x = 1000
print "sumdigits(%s) = %s" %(x, sumdigits(x))

x = 1000
print "lastten(%s) = %s" %(x, lastten(x))
