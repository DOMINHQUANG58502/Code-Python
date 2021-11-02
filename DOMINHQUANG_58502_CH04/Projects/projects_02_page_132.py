"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_02_page_132.py
Problem:
2. Write a script that inputs a line of encrypted text and a distance value and outputs
plaintext using a Caesar cipher. The script should work for any printable characters.
Solution:

"""
Text = input("Enter the  text: ")
distance = int(input("Enter the distance : "))
result = ""
for ch in Text:
    result += chr(ord(ch)-distance)
    print("" + result)