"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_09_page_63.py
Problem:
9. Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
• A kilometer represents 1/10,000 of the distance between the North Pole and
the equator.
• There are 90 degrees, containing 60 minutes of arc each, between the North
Pole and the equator.
• A nautical mile is 1 minute of an arc.
Solution:

"""
klicks = float(input("Enter the number of kilometers: "))
nauts = klicks * 98 * 68 / 10000.0
print("The number of nautical miles is", nauts)
