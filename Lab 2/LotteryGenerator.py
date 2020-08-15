# Author:		Logan Hammond; lhammond12@student.umuc.edu
# Source File:  LotteryGenerator.py
# Description:  Program that allows users to generate 3 or 4 digit lottery
#               numbers. 
# IDE:			AWS Cloud9

import random 

print("**** Welcome to the Pick-3, Pick-4 lottery number generator ****")

while True: 
    choiceInt = None
    
    # Display menu. 
    print("\n\tSelect from the following menu: ")
    print("\t\t1. Generate 3-Digit Lottery number")
    print("\t\t2. Generate 4-Digit Lottery number")
    print("\t\t3. Exit the Application")
    
    # Get input from user and display it. 
    try:
        choiceInt = int(input())
        print("You selected {}.".format(choiceInt))
    except(ValueError): 
        print("Invalid input. Please try again.")
        
    # Sentinel check. 
    if(choiceInt == 3):
        print("Thanks for trying the Lottery Application.")
        break
        
    # Choice logic. Generates the digits and displays them to user.  
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    if(choiceInt == 1):
        print("The following 3-digit lottery number was generated:\
        {}{}{}".format(num1, num2, num3))
    elif(choiceInt == 2):
        print("The following 3-digit lottery number was generated:\
        {}{}{}{}".format(num1, num2, num3, num4))
    else: 
        print("Invalid input. Please try again.")
        
    pass
