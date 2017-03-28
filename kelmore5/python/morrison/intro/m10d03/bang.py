import sys
def bang(n):
    return 1 if n == 0 else n*bang(n - 1)

sys.setrecursionlimit(10002)
print bang(5)
print bang(100)
print bang(900)
