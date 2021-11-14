#Roberto Roman
#11-09-21

#Problem 2
#Write a Python function to check whether a number is in a given range.
#Use range(1,10). Print whether the number is in or not in the range.

import math
def check_range(r):
#Using if statements for the range
    if r in range(1,10):
        print("Number", r, "is in range")
    else:
        print(r, "is not in range") #If not in range type print
#users enters number
num = int(input("Insert a number"))
check_range(num)