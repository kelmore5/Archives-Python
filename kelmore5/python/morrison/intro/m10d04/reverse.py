def reverse(s):
    if len(s) == 0:
        return s
    first = s[0]
    rest = s[1:]
    return reverse(rest) + first

def austin(s):
    r = s[::-1]
    return r

print reverse("nelson12i")
print austin("nelson12i")

    
