import sys
import os
import os.path

if len(sys.argv) < 3:
    print "You need a donr and recipient file"
    sys.exit()

donor = sys.argv[1]
recipient = sys.argv[2]
if not os.path.exists(donor):
    print "The file %s does not exist, fool." %donor
    sys.exit()
if os.path.exists(recipient):
    choice = raw_input("Do you want to clobber %s? (y or n): " %recipient)
    if choice.lower() != "y":
        print "bailing to protect your sorry keister."
        sys.exit()
    else:
        pass
print "You are copying %s to %s" %(donor, recipient)

inPipe = open(donor, "r")
outPipe = open(recipient, "w")
glob = inPipe.read()
inPipe.close()
outPipe.write(glob)
outPipe.close()
