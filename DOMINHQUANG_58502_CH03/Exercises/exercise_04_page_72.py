"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_04_page_72.py
Problem:
4. Write a loop that outputs the numbers in a list named saelaries. The outputs should be
formatted in a column that is right-justified, with a fild width of 12 and a precision of 2.
Solution:

"""
n = int(input("Số phần tử của list: "))
salaries = []
for i in range(n):
    salaries.append(float(input()))
for i in salaries:
    print("%12s" % "%0.2f" % i)

