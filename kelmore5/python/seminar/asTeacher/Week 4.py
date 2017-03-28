months = ["January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November",
          "December"]
month = int(input("What month is it? (1-12)"))

if 1 <= month <= 12:
    print("The month is,", months[month-1])
