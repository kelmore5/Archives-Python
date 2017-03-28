##################################################################
#    
#    Author: Kyle Elmore
#    Date: 9/20/11
#    Assignmemnt PS1.py
#    
##################################################################
## 0.  Example:  Create code that asks a user for a temperature
## in degrees Centigrade and retuns the temperature in degrees Farenheit.
print "Problem 0 Solution:\n"
degreesC = input("Enter a temperature in degrees Centigrade:  ")
print "The temperature", degreesC, "degrees Centigrade is", 1.8*degreesC + 32, "degrees Farenheit.\n"

## 1.  Create code that asks a user for a volume in cubic centimeters
## and which returns the volume in cubic inches.
print "Problem 1 Solution:\n "
cubicCm = input("Enter a volume in cubic centimeters to convert to cubic inches: ")
print "The volume", cubicCm, "cubic centimeters in cubic inches is", cubicCm/2.54**3, "cubic centimeters."

## 2.  Create code that prints out a 10X10 square of stars  Make it
## simple and as short as possible.
print "Problem 2 Solution:\n "
print "Here is a 10x10 square of stars:  "
print """* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *"""

## 3.  Create code that asks the user to type in a string and which
## tells how many times the leters x, y and z occur in the string.  Make this
## case-insenstive, i.e. both a and A should count to the total of As.
print "Problem 3 Solution:\n "
string = raw_input("Enter a string:  ")
x = string.count("x") + string.count("X")
y = string.count("y") + string.count("Y")
z = string.count("z") + string.count("Z")

print "You entered %s" % x
print "The number of letter x's in %s is:  %s" %(string,x)
print "The number of letter y's in %s is:  %s" %(string,y)
print "The number of letter z's in %s is:  %s" %(string,z)

## 4.  Create a piece of code that asks a user to enter a file name 
## with an extension (example:  cows.txt) and which reports the name
## of the file and the extenion.   You may assume the user will only
## enter a valid name of the form name.
## Here is a sample dialogue.
## 
## Enter a filename:  cows.txt
## The name of the files is cows
## The extension of the file is txt
print "Problem 4 Solution:\n "
filenameext = raw_input("Enter a filename with its extension:  ")
filename = filenameext.split(".")[0]
extension = filenameext.split(".")[1]
print "The name of the file is:  %s" %filename
print "The extension of the file is:  %s" %extension


## This code will keep asking the user for strings and it puts them
## onto a list named items.  Do not worry about why this code works;
## you will merely be using the list named items it creates and 
## populates
##.
## Uncomment the code in the next few lines to begin work in the next 
## two questions.
items = []
current = "x"
while current != "":
    current = raw_input("Enter a string; to end just hit ENTER:  ")
    if current != "":
        items.append(current)

## 5.  Assuming the user enters at least 4 items that are all lower-case
## words, write code to find and report the second item in alphabetical order.
print "Problem 5 Solution:\n "
## Hint: look up Python list methods; there is a way so sort a list.
items.sort()
print "The second item in your list in alphabetical order is:  %s" %items[1]

## 6.  Assuming the user enters only lower-case words into the list, tell
## how to find and report the words earliest and last in alphabetical order 
print "Problem 6 Solution:\n "
print "The first item in your list in alphabetical order is:  %s" %items[0]
print "The last item in your list in alphabetical order is:  %s" %items[-1]

## 7.  Have the computer ask the user for three numbers. Then
## format the numbers in a table datum row in HTML.  Example:
## Enter a number: 2.3
## Enter a number: 3.4
## Enter a number: 4.5
## <tr><td>2.3</td><td>3.4</td><td>4.5</td></tr>
print "Problem 7 Solution:\n "
firstnum = input("Enter a number to put into a table datum row in HTML:  ")
secondnum = input("Enter another number:  ")
thirdnum = input("Enter another number:  ")
print "Here is your numbers in a table datum row in HTML:  <tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(firstnum, secondnum, thirdnum)


## 8.  Have the computer ask the user for a date entered in the form
## mm/dd/yyyy.  Have it reply, specifying the month, day and year
##  as integers.
##  Hint: learn about rfind.
##
## Example dialog
## Enter a date as mm/dd/yyyy:  5/5/2001
## The month is 5.
## The day is 5.
## The year is 2001.
## type(month) = <type 'int'>
## type(day) = <type 'int'>
## type(year) = <type 'int'>
print "Problem 8 Solution:\n"
date = raw_input("Enter a date in mm/dd/yyyy format:  ")
month = int(date[:date.find("/")])
day = int(date[date.find("/")+1:date.rfind("/")])
year = int(date[date.rfind("/")+1:])
print "The month is %s." %month
print "The day is %s." %day
print "The year is %s." %year





