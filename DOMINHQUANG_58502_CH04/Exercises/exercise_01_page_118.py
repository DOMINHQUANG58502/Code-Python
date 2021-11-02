"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_01_page_118.py
Problem:
1. Assume that the variable data refers to the string "Python rules!". Use a string
method from Table 4-2 to perform the following tasks:
a. Obtain a list of the words in the string.
b. Convert the string to uppercase.
c. Locate the position of the string "rules".
d. Replace the exclamation point with a question mark.
Solution:
"""
#a. Obtain a list of the words in the string.
data = "Python rules!"            # OUTPUT

tokens = data.split(" ")          # ['Python','rules!']

print(tokens)
#b. Convert the string to uppercase.
upperCaseData = data.upper()             # PYTHON RULES!

print(upperCaseData)
#c. Locate the position of the string "rules".

iIndexPos = data.index("rules")          #  7

print(iIndexPos)
# d. Convert the string to uppercase.
data.replace('!', '?')



