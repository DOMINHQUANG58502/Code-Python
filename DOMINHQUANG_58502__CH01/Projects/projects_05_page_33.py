"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_05_page_33.py
Problem:
5. Modify the program of Project 4 to compute the area of a triangle. Issue the
appropriate prompts for the triangle’s base and height, and change the names of
the variables appropriately. Then, use the formula .5 * base * height to compute the area. Test the program from an IDLE window.
Solution:

"""
height = int(input('Enter height of triangle: '))
base = int(input('Enter base of triangle: '))
print('The area of a triangle =',.5 * base * height)