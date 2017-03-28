def pig(x):
    if x[0] != "a" or x[0] != "e" or x[0] != "i" or x[0] != "o" or x[0] != "u" or x[0] != "y": 
        x = x[1:] + x[0] + "ay"
        return x
    else:
        pass

x = raw_input("Enter a word:  ")
print pig(x)
