#Project Euluer Problem 12

def countFactors(n):
    temp = 1
    count = 0
    while temp * temp < n:
        if n % temp == 0:
            if temp * temp == n:
                count +=1
            else:
                count += 2
        temp += 1
    return count
    
count = 1
num = 3
i = 2

while count <= 500:
    i += 1
    num += i
    count = countFactors(num)

print(num)
