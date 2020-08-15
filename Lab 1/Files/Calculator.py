# Author:		Logan Hammond; lhammond12@student.umuc.edu
# Source File:  Calculator.py
# Description:  Program that prompts user too calculate sum, 
#               difference, mod, product, or quotient of two input 
#               integers. 
# IDE:			AWS Cloud9

# Print menu. 
print("What calculation do you want to perform?")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
print("5) Modulus")

# Receive necessary inputs and necessary variables initialized. 
choice = int(input("Choice: "))
choice_str = ""
first_num = int(input("Enter first integer: "))
second_num = int(input("Enter second integer: "))
result = 0

# Compute result given previous user input. 
if choice == 1:
    choice_str = "sum"
    result = first_num + second_num
if choice == 2:
    choice_str = "difference"
    result = first_num - second_num
if choice == 3:
    choice_str = "product"
    result = first_num * second_num
if choice == 4:
    choice_str = "quotient"
    result = first_num / second_num
if choice == 5:
    choice_str = "modulus"
    result = first_num % second_num

# Print result. 
print("The {} of {} and {} is {}.".format(choice_str, first_num, 
                                        second_num, result))