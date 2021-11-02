"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_02_page_72.py
Problem:
2. Write a code segment that displays the values of the integers x, y, and z on a single
line, such that each value is right-justified with a field width of 6.
Solution:

"""
x= int(input("nhap x"))
y= int(input("nhap y"))
z= int(input("nhap z"))
print("%6s" % x,"%6s" % y,"%6s" %z)

