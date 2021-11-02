"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_03_page_132.py
Problem:
3. Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.
Solution:

"""
code = raw_input("Enter the coded text: ")
distance = input("Enter the distance value: ")
plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - distance - \
                      (ordValue -ord'a')-1
    plainText += chr(cipherValue)
print plainText