#If statements
n = int(input("Number? "))
if n < 0:
    print("The absolute value of", n, "is", -n)
else:
    print("The absolute value of", n, "is", n)

#elif
a = 0
while a < 10:
    a += 1
    if a > 5:
        print(a, ">", 5)
    elif a <= 3:
        print(a, "<=", 3)
    else:
        print("Neither test was true.")

#high/low
number = 7
guess = -1

print("Guess the number!")
while guess != number:
    guess = int(input("is it..."))
    if guess == number:
        print("Hooray! You guess it right!")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big.")

#Even
#Always want to put else
number = float(input("Tell me a number:"))
if number % 2 == 0:
    print(int(number), "is even.")
elif number % 2 == 1:
    print(int(number), "is odd.")
else:
    print(number, "is very strange.")

#Average
count = 0
sum = 0.0
number = 1

print("Enter 0 to exit the loop")
while number != 0:
    number = float(input("Enter a number: "))
    if number != 0:
        count += 1
        sum += number
    if number == 0:
        print("The average was:", sum/count)

#Sum greater than 100
sum = 0.0
print("Enter two numbers to sum: ")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the sconed number: "))
sum = number1 + number2
if sum > 100:
    print("That is a big number!")
else:
    print("That number's small.")

#Defining Functions; a.k.a programmers are LAZY
a = 23
b = -23
if a < 0:
    a = -a
if b < 0:
    b = -b
if a == b:
    print("The absoute values of", a, "and", b, "are equal")
else:
    print("The absolute values of", a, "and", b, "are different")

a = 23
b = -23

def absolute(n):
    if n < 0:
        return -n
    return n

if absolute(a) == absolute(b):
    print("The absolute values of", a, "and", b, "are equal")
else:
    print("The absolute values of", a, "and", b, "are different")

#Examples
def hello():
    print("Hello")

def area(width, height):
    return width * height

def welcome(name):
    print("Welcome", name)

hello()
hello()

welcome("Fred")
w = 4
h = 5
print("Width =", w, "\nheight =", h, "\narea =", area(w, h))

#Scope
a = 4

def scope():
    a = 17
    print("In scope, a =", a)

scope()
print("a =", a)

#Temperature
def options():
    print("Options: ")
    print(" 'p' print options")
    print(" 'c' convert from Celsius")
    print(" 'f' convert from Fahrenheit")
    print(" 'q' quit the program")

def celsiusToFahrenheit(temp):
    return 9.0 / 5.0 * temp + 32

def fahrenheitToCelsius(temp):
    return (temp - 32) *5.0/9.0

choice = "p"
while choice != "q":
    if choice == "c":
        temp = float(input("Celsius temperature: "))
        print("Fahrenheit:", celsiusToFahrenheit(temp))
        choice = input("option: ")
    elif choice == "f":
        temp = float(input("Fahrenheit temperature: "))
        print("Celsius:", fahrenheitToCelsius(temp))
        choice = input("option: ")
    elif choice == "p":
        options()
        choice = input("option: ")

#Rewrite area of square to do circle too

#Infinte:
def welcome():
    print("Welcome!")
    welcome()

#Recursion
def mult(a, b):
    if b == 0:
        return 0
    rest = mult(a, b-1)
    value = a + rest
    return value
print("3 * 2 = ", mult(3, 2))

#countdown
def countdown(n):
    print(n)
    if n > 0:
        return countdown(n-1)

countdown(5)

#Lists
month = int(input("What month (1-12)? "))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

if 1 <= month <= 12:
    print("The month is", months[month-1])

#Functions
demolist = ["life", 42, "the universe", 6, "and", 9]
print("demolist = ",demolist)
demolist.append("everything")
print("after 'everything' was appended demolist is now:")
print(demolist)
print("len(demolist) =", len(demolist))
print("demolist.index(42) =", demolist.index(42))
print("demolist[1] =", demolist[1])
 
# Next we will loop through the list
for c in range(len(demolist)):
    print("demolist[", c, "] =", demolist[c])
 
del demolist[2]
#or demolist.remove("universe")
print("After 'the universe' was removed demolist is now:")
print(demolist)
if "life" in demolist:
    print("'life' was found in demolist")
else:
    print("'life' was not found in demolist")
 
if "amoeba" in demolist:
    print("'amoeba' was found in demolist")
 
if "amoeba" not in demolist:
    print("'amoeba' was not found in demolist")
 
another_list = [42,7,0,123]
another_list.sort()
print("The sorted another_list is", another_list)

#Huge List Function
menu_item = 0
namelist = []
while menu_item != 9:
    print("--------------------")
    print("1. Print the list")
    print("2. Add a name to the list")
    print("3. Remove a name from the list")
    print("4. Change an item in the list")
    print("9. Quit")
    menu_item = int(input("Pick an item from the menu: "))
    if menu_item == 1:
        current = 0
        if len(namelist) > 0:
            while current < len(namelist):
                print(current, ".", namelist[current])
                current = current + 1
        else:
            print("List is empty")
    elif menu_item == 2:
        name = input("Type in a name to add: ")
        namelist.append(name)
    elif menu_item == 3:
        del_name = input("What name would you like to remove: ")
        if del_name in namelist:
            # namelist.remove(del_name) would work just as fine
            item_number = namelist.index(del_name)
            del namelist[item_number]
            # The code above only removes the first occurrence of
            # the name.  The code below from Gerald removes all.
            # while del_name in namelist:
            #       item_number = namelist.index(del_name)
            #       del namelist[item_number]
        else:
            print(del_name, "was not found")
    elif menu_item == 4:
        old_name = input("What name would you like to change: ")
        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input("What is the new name: ")
            namelist[item_number] = new_name
        else:
            print(old_name, "was not found")
 
print("Goodbye")

#Memory test
## This program runs a test of knowledge
 
# First get the test questions
# Later this will be modified to use file io.
def get_questions():
    # notice how the data is stored as a list of lists
    return [["What color is the daytime sky on a clear day? ", "blue"],
            ["What is the answer to life, the universe and everything? ", "42"],
            ["What is a three letter word for mouse trap? ", "cat"]]
 
# This will test a single question
# it takes a single question in
# it returns True if the user typed the correct answer, otherwise False
 
def check_question(question_and_answer):
    # extract the question and the answer from the list
    # This function take a list with two elements, a question and an answer.  
    question = question_and_answer[0]   
    answer = question_and_answer[1]
    # give the question to the user
    given_answer = input(question)
    # compare the user's answer to the testers answer
    if answer == given_answer:
        print("Correct")
        return True
    else:
        print("Incorrect, correct was:", answer)
        return False
 
# This will run through all the questions
def run_test(questions):
    if len(questions) == 0:
        print("No questions were given.")
        # the return exits the function
        return
    index = 0
    right = 0
    while index < len(questions):
        # Check the question
        #Note that this is extracting a question and answer list from the lists of lists.
        if check_question(questions[index]): 
            right = right + 1
        # go to the next question
        index = index + 1
    # notice the order of the computation, first multiply, then divide
    print("You got", right * 100 / len(questions),\
           "% right out of", len(questions))
 
# now let's get the questions from the get_questions function, and
# send the returned list of lists as an argument to the run_test function.
 
run_test(get_questions())
