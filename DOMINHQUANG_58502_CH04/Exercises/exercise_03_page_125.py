"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_03_page_125.py
Problem:
3. Assume that a file contains integers separated by newlines. Write a code segment
that opens the file and prints the average value of the integers.
Solution:
"""
fname = open("myfile2.txt",'r')
count = 0
sum = 0

for line in fname:
    sum += int(line.strip())
    count += 1
if count == 0:
    average = 0
else:
    average = sum /count
print("The average is : ", average)

