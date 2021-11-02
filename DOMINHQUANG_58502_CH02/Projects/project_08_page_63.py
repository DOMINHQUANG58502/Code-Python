"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_08_page_63.py
Problem:
8. Light travels at 3 *108
 meters per second. A light-year is the distance a light beam
travels in one year. Write a program that calculates and displays the value of a
light-year.
Solution:

"""
# compute the result
rate = 3 * 10 ** 8
seconds = 365 * 24 * 60 ** 2
distance = rate * seconds
#display the result
print("Light travels",distance,"meters in a year")
