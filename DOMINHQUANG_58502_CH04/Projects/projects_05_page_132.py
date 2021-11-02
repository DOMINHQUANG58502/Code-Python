"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_05_page_132.py
Problem:
5. A bit shift is a procedure whereby the bits in a bit string are moved to the left or
to the right. For example, we can shift the bits in the string 1011 two places to
the left to produce the string 1110. Note that the leftmost two bits are wrapped
Copyright 2019 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.
Copyright 2019 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. WCN 02-200-203
133
Projects
around to the right side of the string in this operation. Define two scripts,
shiftLeft.py and shiftRight.py, that expect a bit string as an input. The script
shiftLeft shifts the bits in its input one place to the left, wrapping the leftmost bit
to the rightmost position. The script shiftRight performs the inverse operation.
Each script prints the resulting string.

Solution:

"""

def shiftLeft(bitstring):
    bitstring = bitstring[1:]+bitstring[0]
    return bitstring

bits = input("Enter a string of bits: ") #Get the input from user

#call the shiftLeft method which returns the value


leftShift = shiftLeft(bits) # that is stored in leftShift


print()
