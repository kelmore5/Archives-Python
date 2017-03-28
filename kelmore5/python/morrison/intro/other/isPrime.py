def isPrime(n):
    k = 2
    while k*k <= n:
        if n% k == 0:
            return False
        k += 1
    return True

def smallestFactor(n):
    k = 2
    while k*k <= n:
        if n% k == 0:
            return k
        k += 1
    return n

def primeFactor(n):
    ret = []
    i = smallestFactor(n)
    while (i != n):
        ret.append(i)
        n = n/i
        i = smallestFactor(n)
    ret.append(i)
    return ret

def primeFactors(n):
    ret = []
    while(isPrime(n/smallestFactor(n)) == False):
         ret.append(smallestFactor(n))
         n = n/smallestFactor(n)
    return ret

def primeFactor2(n):
    ret = []
    while (n > 1):
        i = smallestFactor(n)
        ret.append(i)
        n = n/i
    return ret

def primeFactors3(n)
    i = smallestFactor(n)
    if (i == n):
        return [i]
    else:
        return primeFactors3(n/i) + [i]

def primeFactors4(n):
    if n == 1:
        return []
    s = smallestFactor(n)
    return[s] + primeFactors4(n/s)

print isPrime(997)
