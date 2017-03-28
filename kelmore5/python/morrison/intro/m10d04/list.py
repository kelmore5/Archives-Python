def printList(x):
    if x == []:
        return 
    first = x[0]
    rest = x[1:]
    print first
    printList(rest)
    

def printListBackwards(x):
    if x == []:
        return 
    first = x[0]
    rest = x[1:]
    printListBackwards(rest)
    print first

x = range(10)
printList(x)
y = ["a", "b", "c"]
printListBackwards(y)
