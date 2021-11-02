"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_03_page_109.py
Problem:
3. You are given a string that was encoded by a Caesar cipher with an unknown distance value. The text can contain any of the printable ASCII characters. Suggest an
algorithm for cracking this code
Solution:
Parse each character in the string to the corresponding natural number.
Subtract that natural number to any number, try the values in turn
From the newly received natural number to the corresponding ascii character
If the number is 00, then subtract 127 from "steps" and add 1
"""
