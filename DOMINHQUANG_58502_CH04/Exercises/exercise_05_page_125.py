"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_05_page_125.py
Problem:
5. Write a code segment that prompts the user for a filename. If the file exists, the
program should print its contents on the terminal. Otherwise, it should print an
error message.
Solution:
"""
from os.path import exists
fileName = input("Enter a file name: ")
if not exists(fileName):
    print("Error: the file does not exist!")
else:
    inputFile = open(fileName, 'r')
    print(inputFile.read())
