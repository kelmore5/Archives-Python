## $ python gopher.py word file
## It replies "The file .... contains word """
## or "the file ... does not contain word """

import sys
import os.path
if len(sys.argv) != 2:
    print "This requires two arguments, fool!"
    exit()
word = sys.argv[1]
file = sys.argv[2]
inPipe = open(file, "r")
if word in inPipe:
    return "The word %s is in %s." %(word, file)
    exit()
else:
    return "The word %s is not in %s." %(word, file)
    exit()

import sys
donor = sys.argv[1]
word = sys.argv[2]
lineNumber = 0
inPipe = open(donor, "r")
for k in inPipe:
    lineNumber += 1
    if (word in k.split()):
        print "%s found in file %s on line %s" %(word, donor, lineNumber)
        sys.exit
print "%s is not in file %s" %(word, donor)
