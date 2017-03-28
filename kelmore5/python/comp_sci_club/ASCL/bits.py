##################################################################
#    
#    Author: Kyle Elmore
#    Date: 12/19/11
#    Grade: Junior
#    School: North Carolina School of Science and Mathematics
#    American Computer Scence League: Intermediate Division
#    
##################################################################

def matchBinary():
    inputBits = []
    bits = []
    output = []
    bitLongHand = ""
    shortHand = raw_input("Type the short hand version of the bit string and press enter:  ")
    bitsNumber = input("Type the number of bits to follow and press enter:  ")
    shortHand = list(shortHand)
    while(bitsNumber > 0):
        inputBits.append(raw_input("Type the bit string to compare to the short hand and press enter:  "))
        bitsNumber -= 1
    bits = [list(k) for k in inputBits]
    for k in bits:
        while("*" in shortHand):
            for k in bits:
                k.pop(shortHand.index("*"))
            shortHand.pop(shortHand.index("*"))
    bits = ["".join(k) for k in bits]
    shortHand = "".join(shortHand)
    while(shortHand in bits):
        output.append(inputBits[bits.index(shortHand)])
        inputBits.pop(bits.index(shortHand))
        if shortHand in bits:
            bits.pop(bits.index(shortHand))
    if(output == []):
        return "None"
    return output
    
print matchBinary()
