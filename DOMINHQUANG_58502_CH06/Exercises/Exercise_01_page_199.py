"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_01_page_199.py
Problem:
1. Write the code for a mapping that generates a list of the absolute values of the numbers in a list named numbers
Solution:

"""
test = [5, -6, 7, -8, -10]
print("The original list: " + str(test))
res = list(map(abs, test))
print(" value list : " + str(res))


