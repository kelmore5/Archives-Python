import sys
quarry = sys.argv[1]
inPipe = open("nicate.html", "r")
stuff = inPipe.read()
if quarry in stuff:
    print "the fie contains the string", quarry
