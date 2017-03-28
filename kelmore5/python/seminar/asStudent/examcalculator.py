def examMin(currentGrade, wantedGrade, examPercent, maxExam):
    examPercent *= .01
    zeroExam = currentGrade*(1-examPercent)
    minExam = (wantedGrade - zeroExam)/examPercent
    maxGrade = zeroExam + 100*examPercent
    if minExam > maxExam:
        print "Sucks to suck"
        return "The highest grade you could get if you made 100 is: ", maxGrade
    else:
        return "The minimum exam grade you can get is: ", minExam

if __name__ == "__main__":
    target = raw_input("Enter the grade you want. (A, B, C, ALT): ")
    target = target.upper()
    if target == "A":
        targetG = 90
    elif target == "B":
        targetG = 80
    elif target == "C":
        targetG = 70
    elif target == "ALT":
        targetG = raw_input("Enter the numerical value you want: ")
    else:
        print "Wrong input. Please read the directions again"
    current = input("Enter your current grade (ex. 90)")
    worth = input("Enter the percentage of your grade your exam is worth" )
    extra = input("Enter the maximum possible grade on the exam: ")
    
    print examMin(current, targetG, worth, extra)
