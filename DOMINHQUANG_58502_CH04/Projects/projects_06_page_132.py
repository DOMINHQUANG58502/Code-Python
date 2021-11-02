"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_06_page_132.py
Problem:
6. Use the strategy of the decimal to binary conversion and the bit shift left operation defined in Project 5 to code a new encryption algorithm. The algorithm
should add 1 to each character’s numeric ASCII value, convert it to a bit string,
and shift the bits of this string one place to the left. A single-space character in
the encrypted string separates the resulting bit strings
Solution:

"""
def binary_string(num):
    bit_strng="{0:b}".format(num);
    return bit_strng
#taking string as input from the user
str=input("Enter a message: ")
bit_list=[]
for i in str:
    bits=binary_string(ord(i)+1)
    bits=bits[1:]+bits[0]
    bit_list.append(bits)
output=""
print("")
for bit in bit_list:
    output+=bit+" "
print(output)