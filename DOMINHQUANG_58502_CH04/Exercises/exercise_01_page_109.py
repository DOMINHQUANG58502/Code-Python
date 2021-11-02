"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_01_page_109.py
Problem:
1. Write the encrypted text of each of the following words using a Caesar cipher with
a distance value of 3:
a. python
b. hacker
c. wow
Solution:

"""
text = input("Nhập 1 đoạn kí tự: ")
distance = int(input("Nhập giá trị: "))
Plaintext = ""
for ch in text:
    ordvalue = ord(ch)
    cirphervalue = ordvalue - distance
    if cirphervalue < ord('a'):
        cirphervalue = ord('z') - (distance - (ord('a') - ordvalue -1 ))
        Plaintext += chr(cirphervalue)
print(Plaintext)