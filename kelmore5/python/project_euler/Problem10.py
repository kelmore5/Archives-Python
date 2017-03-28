#Project Euluer Problem 10

#Can be done faster using Sieve of Eratosthenes

def isPrime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
    
numSum = 0

for x in range(1,2000000):
    if(isPrime(x)):
        numSum += x
    
print(numSum)
