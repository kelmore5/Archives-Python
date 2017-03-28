def f(x):
    return x*x
def g(x):
    return x*x*x

### How can we do the same thing a specified number of times?
n = 10
for k in range(10):
    print "Hello"

##Construct an HTML table of values

print "<table>"
print "<tr><th>x</th><th>x<sup>2</sup></th><th>x<sup>3</sup></th></tr>"
for k in range(1, 21):
    print "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(k, f(k), g(k))
print "</table>"
