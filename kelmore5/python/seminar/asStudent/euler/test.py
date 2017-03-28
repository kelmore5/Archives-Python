def firsttenofsum(x):
    """postcondition: returns the first 10 digits
of the sum of a text file containing a list of numbers
seperated by enters"""
    a = open(x, "r")
    a = a.read()
    a = a.split("\n")
    a = [int(k) for k in a]
    a = sum(a)
    a = str(a)
    return a[:10]

print f("numbers.txt")

