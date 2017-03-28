import sys

outPipe = open("Resuls.finkelstein", "a")
n = input("Enter a number:  ")
iter = 1
total = 0

while(iter <= n):
    total += iter**2
    iter +=1
print total
outPipe.write("The sum of squares is to %s is %s\n" %(n, total))
