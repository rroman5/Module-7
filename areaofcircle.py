#Roberto Roman
#11-09-2021

#Problem 1
#Write a function area_of_circle(r) which returns the area of a circle of radius r

import math
def area_of_circle(r):
    area_of_circle = r * r * math.pi
    return area_of_circle

if __name__ == "__main__":
    radius = int(input("Enter radius"))
    result = area_of_circle(radius)


#result = area_of_circle
print ("The area if the circle is", result)