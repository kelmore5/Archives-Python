x = "<tr>"
x2 = "</tr>"
y = "<th>"
y2 = "</th>"
z = "<td>"
z2 = "</td>"

print '<table class = "center-table">'
print x,y,"x",y2,x2
print x,z,"0",z2,x2
print x,z,"1"

print '''<table class = "center-table">
<tr><th>x</th><th>x*x</th></tr>
<tr><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td></tr>
<tr><td>2</td><td>4</td></tr>
<tr><td>3</td><td>9</td></tr>
<tr><td>4</td><td>16</td></tr>
<tr><td>5</td><td>25</td></tr>
<tr><td>6</td><td>36</td></tr>
<tr><td>7</td><td>49</td></tr>
</table>'''

print "<tr><td>%s</td><td>%s</td></tr>"

