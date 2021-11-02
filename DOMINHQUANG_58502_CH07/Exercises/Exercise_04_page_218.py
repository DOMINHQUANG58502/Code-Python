"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_04_page_218.py
Problem:
4. The functions that draw polygons in the polygons module have the same pattern, varying
only in the number of sides (iterations of the loop). Factor this pattern into a more general
function named polygon, which takes the number of sides as an additional argument.
Solution:

"""


import turtle

# creating turtle pen
t = turtle.Turtle()
n = int(input("Enter the no of the sides of the polygon : "))
l = int(input("Enter the length of the sides of the polygon : "))
for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)