import random
def maximum(x):
    """prec: x is a nonempty list of numbers.
post: returns largest numbero n the list."""
    out = x[0]
    for k in x[1:]:
        if k > out:
            out = k
    return out

def maximum2(x):
    x.sort()
    return  x[-1]

def minimum(x):
    """prec: x is a nonempty list of numbers.
post: returns smallest numbero n the list."""
    out = x[0]
    for k in x[1:]:
        if k < out:
            out = k
    return out

def minimum2(x):
    x.sort()
    return  x[0]

def product(x):
    """prec: x is a list of numbers
postc: returns the product of the list"""
    if x == []:
        return 1
    return x[0]*product(x[1:])

def productFroot(x):
    """prec: x is a list of numbers
postc: returns the product of the list"""
    p = 1
    for k in x:
        p *= k
    return p

mt = []
for k in range(20):
    mt.append(random.randint(0,10))
print mt
print "The maximum is %s" % maximum(mt)
print mt
print "The maximum is %s" % maximum2(mt)
print mt
print "The minimum is %s" % minimum(mt)
print mt
print "The maximum is %s" % minimum2(mt)
print mt

print "The product is %s" % product(mt)
print mt
print "The product is %s" % productFroot(mt)
print mt

