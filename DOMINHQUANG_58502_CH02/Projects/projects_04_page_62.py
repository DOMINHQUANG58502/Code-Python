"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_04_page_62.py
Problem:
4. Write a program that takes the radius of a sphere (a floating-point number) as
input and then outputs the sphere’s diameter, circumference, surface area, and
volume.
Solution:

"""
import math
radius = float(input("Radius = "))
diameter = radius * 2
circumference = diameter * math.pi
surfaceArea = 4 *math.pi *radius * radius
volume = 4/3 *math.pi *radius *radius* radius
print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface area : ", surfaceArea)
print("Volume ", volume)
