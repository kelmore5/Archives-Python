#Project Euluer Problem 7

def isPrime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
    
count = 2
num = 3
end = 10001

while count < end:
    num += 2
    if isPrime(num):
        count += 1
    
print(num)

