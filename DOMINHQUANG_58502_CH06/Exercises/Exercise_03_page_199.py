"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_03_page_199.py
Problem:
3. Write the code for a reducing that creates a single string from a list of strings named
words
Solution:

"""
list = ['ramos', 'bravo', 'keita', 'chiesa']
from functools import reduce
print(reduce(lambda x,y:x+y,map(lambda x:x[0],list)))
