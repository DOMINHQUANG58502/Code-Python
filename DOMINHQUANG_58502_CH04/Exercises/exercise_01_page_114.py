"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_01_page_114.py
Problem:
1. Translate each of the following numbers to decimal numbers:
a. 110012
b. 1000002
c. 111112
Solution:
"""
#a. 11001
bitString = "11001"
decimal = 0
exponent = len(bitString) - 1

for digital in bitString:
    decimal = decimal + int(digital) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)

#b. 100000
bitString = "100000"
decimal = 0
exponent = len(bitString) - 1

for digital in bitString:
    decimal = decimal + int(digital) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)
#c. 11111
bitString = "11111"
decimal = 0
exponent = len(bitString) - 1

for digital in bitString:
    decimal = decimal + int(digital) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)