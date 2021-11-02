"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_04_page_85.py
Problem:
4. Assume that the variables x and y refer to strings. Write a code segment that prints
these strings in alphabetical order. You should assume that they are not equal.
Solution:
"""

my_str = "a b c d e"

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
   print(word)
