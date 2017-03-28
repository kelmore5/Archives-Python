#Project Euluer Problem 9

def findTriplet(n):
    for x in range(1,1001):
        for y in range(1,1001):
            for z in range(1,1001):
                if x*x == y*y + z*z and x + y + z == 1000:
                    product = x*y*z
                    print(product)
                    return

findTriplet(1000)
