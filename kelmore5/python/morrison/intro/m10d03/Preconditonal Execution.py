def halfOfAlphabet(x):
    """prec:  x is an alpha string
postc:  returns "in the first half" if x is in the first half of the
alphabet; otherwise "in the second half" """
    #whole expression is one of two terms - first half or second half
    #depending on string x
    return "in the first half" if x.lower() < "m" else "in the second half"

s = "morrison"
print "%s is %s of the alphabet" %(s, halfOfAlphabet(s))

s = "Aardvark"
print "%s is %s of the alphabet" %(s, halfOfAlphabet(s))

s = "hi"
print "%s is %s of the alphabet" %(s, halfOfAlphabet(s))

s = "mike"
print "%s is %s of the alphabet" %(s, halfOfAlphabet(s))
