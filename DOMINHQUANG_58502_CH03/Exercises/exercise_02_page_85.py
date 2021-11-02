"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_02_page_85.py
Problem:
2. Assume that x refers to a number. Write a code segment that prints the number’s
absolute value without using Python’s abs function

Solution:

"""
number = int(input("Nhập số vào đây: "))
if number > 0:
    print("Gía trị tuyệt đối của số vừa nhập là ", number)
else:
    print("Gía trị tuyệt đối của số vừa nhập là ",-number)