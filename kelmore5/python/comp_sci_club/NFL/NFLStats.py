##################################################################
#    
#    Author: Kyle Elmore
#    Date: 12/19/11
#    Grade: Junior
#    School: North Carolina School of Science and Mathematics
#    
##################################################################

years = []
salaries = []

def NFLStats():
    NFLStats = []
    years = []
    salaries = []
    annualSalaries = []
    differenceGameSalaries = []

    inPipe = raw_input("Enter the filename and extension of the text file with the players' contract years and salaries (The file must be in the same folder as this program):  ")
    print "The answers to the problems are stored in the file 'NFL_Stats.txt' as well as printed below: "
    outPipe = open("NFL_Stats.txt", "w")
    mainfile = open(inPipe, "r").read()
    mainfile = list(mainfile)
    for k in mainfile:
        if k.isdigit() != True and k != ".":
            mainfile[mainfile.index(k)] = "n"
    mainfile = "".join(mainfile)
    mainfile = mainfile.split("n")
    
    for k in mainfile:
        if isadigit(k) == True:
            NFLStats.append(k)
    
    n = 0
    if NFLStats[0] == "1.":
        while n <= len(NFLStats)-1:
            NFLStats.remove(NFLStats[n])
            n += 2

    if isanint(NFLStats[0]) == True:
    
        n = 0
        while n <= len(NFLStats)-1:
            years.append(NFLStats[n])
            n += 2
        years = [int(k) for k in years]
    
        n = 1
        while n <= len(NFLStats)-1:
            salaries.append(NFLStats[n])
            n += 2
        salaries = [float(k)*1000000 for k in salaries]

    elif isanint(NFLStats[0]) == False:

        n = 1
        while n <= len(NFLStats)-1:
            years.append(NFLStats[n])
            n += 2
        years = [int(k) for k in years]
    
        n = 0
        while n <= len(NFLStats)-1:
            salaries.append(NFLStats[n])
            n += 2
        salaries = [float(k)*1000000 for k in salaries]
    
    n = 0
    while n <= len(years)-1:
        annualSalaries.append(salaries[n]/years[n])
        n += 1
    
    averageSalary = int(round(sum(annualSalaries)/len(annualSalaries)))
    largestSalary = int(round(max(annualSalaries)))
    draftLargestSalary = annualSalaries.index(largestSalary) + 1
    annualGameSalary16 = [k/16.0 for k in annualSalaries]
    rangeGameSalary16 = int(round(max(annualGameSalary16) - min(annualGameSalary16)))
    annualGameSalary18 = [k/18.0 for k in annualSalaries]
    midrangeGameSalary18 = int(round((max(annualGameSalary18) + min(annualGameSalary18))/2))

    n = 0
    while n <= len(annualGameSalary16)-1:
        differenceGameSalaries.append(annualGameSalary16[n] - annualGameSalary18[n])
        n += 1

    averageDifferenceGameSalary = int(round(sum(differenceGameSalaries)/len(differenceGameSalaries)))

    outPipe.write("1. %s\n2. %s by #%s\n3. %s\n4. %s\n5. %s" %(averageSalary, largestSalary, draftLargestSalary, rangeGameSalary16, midrangeGameSalary18, averageDifferenceGameSalary))
    print "\n1. %s\n2. %s by #%s\n3. %s\n4. %s\n5. %s" %(averageSalary, largestSalary, draftLargestSalary, rangeGameSalary16, midrangeGameSalary18, averageDifferenceGameSalary)
    
def isadigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def isanint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

NFLStats()
