"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_06_page_218.py
Problem:
6. The Turtle class includes a method named circle. Import the Turtle class, run
help(Turtle.circle), and study the documentation. Then use this method to
draw a filled circle and a half moon.
Solution:

"""
import turtle
turtle.Screen()
turtle.bgcolor("magenta")

turtle.color("yellow")
turtle.begin_fill()
turtle.circle(130,180)
turtle.end_fill()
turtle.hideturtle()