"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_10_page_132.py
Problem:
10. Write a script named dif.py. This script should prompt the user for the names
of two text files and compare the contents of the two files to see if they are the
same. If they are, the script should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file that differ from each
other. The input loop should read and compare lines from each file. The loop
should break as soon as a pair of different lines is found.
Solution:

"""
file1 = input("Enter name of first file to compare: ")
file2 = input("Enter name of second file to compare: ")

f1 = open(file1, 'r')
f2 = open(file2, 'r')

f1lines = f1.readlines()
f1.close()
f2lines = f2.readlines()
f2.close()

def compare_lines():
    lineCount = 0
    while lineCount != len(f1lines):
        if f1lines[lineCount] == f2lines[lineCount]:
            lineCount += 1
            if lineCount == len(f1lines):
                print("Yes")
        if f1lines[lineCount] != f2lines[lineCount]:
            print("No")
            print(f2lines[lineCount])