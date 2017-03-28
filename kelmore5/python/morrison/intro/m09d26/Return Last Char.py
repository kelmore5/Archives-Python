def lastChar(x):
    """prec: x is a string
postc: returns the last character of the string."""
    return x[-1]           ##method stub or function stub
def lastNonWhitespaceChar(x):
    """prec: x is a string
postc: returns the last non-whitespace character"""
    y = x.rstrip()
    return y[-1]           ##method stub or function stub
    
if __name__ == "__main__":
    print "*************Test for lastChar***************"
    a = "cat"
    print "The last character of \"%s\" is %s, expected: %s" % (a, lastChar(a), "t")
    a = "abc123"
    print "The last character of \"%s\" is %s, expected: %s" % (a, lastChar(a), "3")

    print "************Test for lastNonWhitespaceChar**********"
    x = "the dog     "
    print "The last non-whitespace character of \"%s\" is %s, expected: %s" % (x, lastNonWhitespaceChar(x), "g")
    x = "1234"
    print "The last non-whitespace character of \"%s\" is %s, expected: %s" % (x, lastNonWhitespaceChar(x), "4")
    x = "     pizzA"
    print "The last non-whitespace character of \"%s\" is %s, expected: %s" % (x, lastNonWhitespaceChar(x), "A")
 
