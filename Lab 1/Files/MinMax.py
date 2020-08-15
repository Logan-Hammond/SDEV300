# Author:		Logan Hammond; lhammond12@student.umuc.edu
# Source File:  MinMax.py
# Description:  Program that takes 5 inputs from user and prints the 
#               minimum and maximum values. 
# IDE:			AWS Cloud9

# Recieve user inputs. 
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
third_num = int(input("Enter third number: "))
fourth_num = int(input("Enter fourth number: "))
fifth_num = int(input("Enter fifth number: "))

# Identify min and max. 
min_num = str(min(first_num, second_num, third_num, fourth_num, fifth_num))
max_num = str(max(first_num, second_num, third_num, fourth_num, fifth_num))

# Print results. 
print("The minimum integer entered was {}".format(min_num))
print("The maximum integer entered was {}".format(max_num))