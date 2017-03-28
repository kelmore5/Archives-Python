def age(x):
    if x < 0:
        return "Hey Joker!"
    elif x > 0 and x < 18:
        return "You are a minor."
    else:
        return "Are you registered to vote?"

#x = 17
#print "age(%s) = %s, expected: %s" %(x, age(x), "You are a minor.")
#x = 18
#print "age(%s) = %s, expected: %s" %(x, age(x), "Are you registered to vote?")
#x = 19
#print "age(%s) = %s, expected: %s" %(x, age(x), "Are you registered to vote?")
#x = -1
#print "age(%s) = %s, expected: %s" %(x, age(x), "Hey Joker!")
