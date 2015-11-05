import os
os.system("cls")

#Problem #1
#Users are the worst- they are always forgetting how to use the software properly. 

#Write a program that barks at the user every time they enter in the same input twice. 
#You must use a while loop to continually ask the user for input, 
#and you must use a for loop to iterate through the list of user inputs





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


