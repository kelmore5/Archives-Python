def triangle(char, size):
    if size == 0:
        return
    triangle(char, size - 1)
    print char*size

def triangle2(char, size):
    if size == 0:
        return
    print char*size
    triangle2(char, size - 1)


triangle("*", 10)
print "**************on acid***************"
triangle2("&", 12)
