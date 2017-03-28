#Project Euluer Problem 3

num = 600851475143
temp = 2

while temp * temp <= num:
    if num % temp == 0:
        num /= temp
    else:
        temp += 1

print(num)
