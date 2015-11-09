#Problem #1

import os
os.system("cls")


def program():
    numlist = [] #empty list
    while True:
        userinput = int(input("Pick a number between 1-5. "))    
        if userinput not in numlist:
            numlist.append(userinput)
            print(numlist)
        else:
            print("These are the numbers you have already entered. Please enter a different number.")
            for userinput in numlist:
                print(userinput)
        if userinput >= 6 : 
            print("Please enter a number between 1-5.")
        elif userinput <= 0 :
            print("Please enter a number between 1-5.") 
        
        
        
program()


