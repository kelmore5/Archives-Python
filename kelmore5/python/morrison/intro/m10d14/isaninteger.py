def isAnInteger(s):
    s = s.strip()
    k = 0
    if s[k] in "+-":
        k +=1
    elif not s[k].isdigit():
        return False
    while k < len(s):
        if not s[k].isdigit():
            return False
    return True

s = "dog"
print isAnInteger(s)

s = "457"
print isAnInteger(s)
