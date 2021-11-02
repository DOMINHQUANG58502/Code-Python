"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_04_page_132.py
Problem:
4. Octal numbers have a base of eight and the digits 0–7. Write the scripts octalToDecimal.py and decimalToOctal.py, which convert numbers between the octal
and decimal representations of integers. These scripts use algorithms that are
similar to those of the binaryToDecimal and decimalToBinary scripts developed in Section 4-3
Solution:



"""
#input
octalNum=int(input('Enter a string of octal digits: '))
#required variables
i = 1
decimal = 0
#loop for conversion
while (octalNum != 0):
#to find remainder
rmd = octalNum % 10
octalNum //= 10
decimal += rmd * i
i *= 8
#print the results
print('\nThe integer value is ',decimal)File: decimalToOctal.py
Converts a decimal integer to a octal integer.

File: octalToDecimal.py
Converts a octal integer to a decimal integer.

#input
octalNum=int(input('Enter a string of octal digits: '))
#required variables
i = 1
decimal = 0
#loop for conversion
while (octalNum != 0):
#to find remainder
    rmd = octalNum % 10
    octalNum //= 10
    decimal += rmd * i
    i *= 8
#print the results
print('\nThe integer value is ',decimal)