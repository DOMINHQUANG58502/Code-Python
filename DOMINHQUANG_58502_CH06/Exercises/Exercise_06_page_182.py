"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_06_page_182.py
Problem:
6. Explain what happens when the following recursive function is called with the
values "hello" and 0 as arguments:
def example(aString, index):
   if index < len(aString):
     example(aString, index + 1)
     print(aString[index], end = "")
Solution:
ollehNone
"""
def example(aString, index):
   if index < len(aString):
     example(aString, index + 1)
     print(aString[index], end = "")

