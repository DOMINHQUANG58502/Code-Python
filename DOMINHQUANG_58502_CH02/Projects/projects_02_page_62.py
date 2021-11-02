"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_02_page_62.py
Problem:
2. You can calculate the surface area of a cube if you know the length of an edge.
Write a program that takes the length of an edge (an integer) as input and prints
the cube’s surface area as output.
Solution:

"""
surface = int(input("Nhập cạnh của khối lập phương: "))
result = 6 *surface*surface
print(" Diện tích hình lập phương là:",result)