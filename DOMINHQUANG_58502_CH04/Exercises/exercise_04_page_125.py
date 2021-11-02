"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_04_page_125.py
Problem:
4. Write a code segment that prints the names of all of the items in the current
working directory.
Solution:
"""
#Traversing the current directory using os.walk()
import os

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)

