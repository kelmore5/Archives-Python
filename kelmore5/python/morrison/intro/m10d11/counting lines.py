import sys
import os.path
if len(sys.argv) < 2:
    print "Usage is wc.py filename"
    sys.exit(1)
file = sys.argv[1]
ch = 0
lines = 0
words = 0
inPipe = open(file, "r")
for k in inPipe:
    ch += len(k)
    lines += 1
    k.split()
    words += len(k.split())
print "In file %s there are %s characters, %s words, and %s lines." %(file, ch, words, lines)
