# Author:		Logan Hammond; lhammond12@student.umuc.edu
# Source File:  MathPlot.py
# Description:  Program that allows users to generate the values of fumctions
#               sin(), cos(), sqrt(), and log10() for a given input x. After
#               wich the results are displayed. 
# IDE:			AWS Cloud9

import math

print("\tWelcome to the MathPlot generator\t")

sin_plot = {}
cos_plot = {}
sqrt_plot = {}
log10_plot = {}

def main():
    while True:
    # Display menu. 
        print("\n\tSelect from the following menu...")
        print("\t\t1. Generate x, sin(x).")
        print("\t\t2. Generate x, cos(x).")
        print("\t\t3. Generate x, sqrt(x).")
        print("\t\t4. Generate x, log10(x).")
        print("\t\t5. Exit the application.")
        
        # Get input from user and display it. 
        choiceInt = int(input())
        print("\n\t\tYou selected {}".format(choiceInt))
        
        # Sentinel check. 
        if choiceInt == 5: 
            print("Thanks for trying the Mathplot generator.")
            break
            
        if choiceInt == 1:
            genSinList()
            print("\n\t\tSin(x) data generated.")
            print(sin_plot)
        elif choiceInt == 2:
            genCosList()
            print("\n\t\tCos(x) data generated.")
            print(cos_plot)
        elif choiceInt == 3:
            genSqrtList()
            print("\n\t\tSqrt(x) data generated.")
            print(sqrt_plot)
        elif choiceInt == 4:
            genLog10List()
            print("\n\t\tLog10(x) data generated.")
            print(log10_plot)
            pass
        else: 
            print("Invalid input. Please try again.")
            
    # End of main
    pass

def genSinList():
    i = -2
    j = 0
    while i < 2:
        sin_plot[j] = round(getSin(i), 2)
        i += 1/64
        j += 1
    
def genCosList():
    i = -2
    j = 0
    while i < 2:
        cos_plot[j] = round(getCos(i), 2)
        i += 1/64
        j += 1

def genSqrtList():
    i = 0
    j = 0
    while i <= 200:
        sqrt_plot[j] = round(getSqrt(i), 2)
        i += .5
        j += 1
    
def genLog10List():
    i = .5
    j = 0
    while i <= 200:
        log10_plot[j] = round(getLog10(i), 2)
        i += .5
        j += 1

def getSin(x):
    return math.sin(math.pi * x)
    
def getCos(x):
    return math.cos(math.pi * x)

def getSqrt(x):
    return math.sqrt(x)

def getLog10(x):
    return math.log10(x)

if __name__ == "__main__":
    main()
    pass
