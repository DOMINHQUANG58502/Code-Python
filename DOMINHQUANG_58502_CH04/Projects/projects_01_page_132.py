"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_01_page_132.py
Problem:
1. Write a script that inputs a line of plaintext and a distance value and outputs an
encrypted text using a Caesar cipher. The script should work for any printable
characters.
Solution:

"""
message = input("Enter a message: ")
distanceValue = int(input("Enter distance value: "))
result = ""
for x in message:
    result += chr(ord(x)+distanceValue)
    print(""+result)