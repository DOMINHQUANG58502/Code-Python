"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_03_page_85.py
Problem:
3. Write a loop that counts the number of space characters in a string. Recall that the
space character is represented as ' '.

Solution:

"""
str=input("Enter the string: \n")
spaces=0
for i in range(0,len(str)):
  if(str[i]==' '):
    spaces=spaces+1
print("The number of spaces are: ",spaces)
