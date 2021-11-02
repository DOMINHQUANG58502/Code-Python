"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_02_page_109.py
Problem:
2. Consult the Table of ASCII values in Chapter 2 and suggest how you would modify
the encryption and decryption scripts in this section to work with strings containing all of the printable characters.
Solution:
ASCII table, then take the smallest number plus the distance
minus 1. Take the number (after adding the distance) and convert it back to the character chr that will be encoded text. Take
The encoded text parses each character into digits in the same ASCII code as above. Subtract that number
displacement distance. If the number is 00, subtract the travel distance from the largest number and then add 1. Take
the number (after subtracting the space) converted to the ch character will decode the text.
"""
