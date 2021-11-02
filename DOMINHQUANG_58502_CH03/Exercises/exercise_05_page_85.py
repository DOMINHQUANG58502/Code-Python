"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_05_page_85.py
Problem:
5. Explain how to check for an invalid input number and prevent it being used in a
program. You may assume that the user enters a number.
Solution:
-nếu x > 0 thì số hợp lệ và ngược lại
"""
x = int(input("Nhập số bất kỳ vào :"))

if x > 0:
    print("x la so hop le")
else:
    print("x la so khong hop le")
