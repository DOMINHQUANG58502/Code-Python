"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_06_page_33.py
Problem:
   6. Write and test a program that computes the area of a circle. This program should
request a number representing a radius as input from the user. It should use the formula
3.14 * radius ** 2 to compute the area and then output this result suitably labeled.
Solution:

"""
radius = int(input('Nhập bán kính của hình tròn: '))
print('Diện tích hình tròn là: ', 3.14 * radius ** 2)