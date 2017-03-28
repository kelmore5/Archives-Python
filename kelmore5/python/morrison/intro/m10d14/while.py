import random
secretNumber = random.randint(1,10)
guess = input("Enter your guess for a number 1 through 10:  ")
while(guess != secretNumber):
      guess = input("Enter another guess, dunerhead:  ")
print "Hooray, finally got it right!!!"
