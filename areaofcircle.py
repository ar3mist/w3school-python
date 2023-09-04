#4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
#Sample Output :
#r = 1.1
#Area = 3.8013271108436504


#Answer

from math import pi

radius = float(input("Enter the value of the radius :"))
area = (radius*radius)*pi
print("The area of the circle is {}".format(area))