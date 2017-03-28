def license(x, y):
    if x < 17 and y[0] <= "M":
        return "You are not eligile for an NJ driver's license and you are in the first half of the alphabet."
    if x >= 17 and y[0] <= "M":
        return "You are eligile for an NJ driver's license and you are in the first half of the alphabet."
    if x < 17 and y[0] > "M":
        return "You are not eligile for an NJ driver's license and you are in the second half of the alphabet."
    else:
         return "You are eligile for an NJ driver's license and you are in the second half of the alphabet."

x = input("Enter you're age:  ")
y = raw_input("Enter you're last name:  ")
print license(x, y)
