"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_04_page_182.py
Problem:
4. Explain what happens when the following recursive function is called with the value
4 as an argument:
def example(n):
   if n > 0:
        print(n)
        example(n - 1)
Solution:
    4
    3
    2
    1
"""
def example(n):
   if n > 0:
        print(n)
        example(n - 1)
