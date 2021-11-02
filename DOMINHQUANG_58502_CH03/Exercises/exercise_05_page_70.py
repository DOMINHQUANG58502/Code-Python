"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_05_page_70.py
Problem:
5. Assume that the variable teststring refers to a string. Write a loop that prints
each character in this string, followed by its ASCII value

Solution:

"""
str1 = input("Please Enter your Own String : ")

for i in range(len(str1)):
    print("The ASCII Value of Character %c = %d" % (str1[i], ord(str1[i])))