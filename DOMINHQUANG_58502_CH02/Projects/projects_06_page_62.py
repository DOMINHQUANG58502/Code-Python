"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_06_page_62.py
Problem:
5. An object’s momentum is its mass multiplied by its velocity. Write a program
that accepts an object’s mass (in kilograms) and velocity (in meters per second) as
inputs and then outputs its momentum.

Solution:

"""
mass=float(input("Enter the object's mass: "))
velocity=float(input("Enter the object's velocity: "))

KE = (1/2)* mass * velocity ** 2
print("The object's kinetic energy is ", KE)