"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_07_page_182.py
Problem:
7. Explain what happens when the following recursive function is called with the
values "hello" and 0 as arguments:
def example(aString, index):
   if index == len(aString):
       return ""
    else:
       return aString[index] + example(aString, index + 1)
Solution:
return empty

"""


