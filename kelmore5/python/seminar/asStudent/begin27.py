def sumLoop():                 #This functionn will sum numbers from 1 to n
    n = input("Please input the number to sum to:  ")
    x = 1                       #set the start to 1
    sumN = 0                    #set the beginning sum to 0

    #while loops keep going until the condition inside the parenthesis
    #isn't true

    while(x <= n):              #while x is less than or equal to n
        sumN += x               #add x to the sum
        x += 1                  #add 1 to x
    print(sumN)                 #print the sum to the screen

#main function: the ting that wlil run wen the file is run

if __name__ == "__main__":      #main function, the thing that will run
    sumLoop()
