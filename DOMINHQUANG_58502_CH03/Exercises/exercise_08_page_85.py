"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_08_page_85.py
Problem:
8. The variables x and y refer to numbers. Write a code segment that prompts the user for
an arithmetic operator and prints the value obtained by applying that operator to x and y.
Solution:
T
"""
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
op = input("Enter an arithmetic operator : ")
operation = 0
if op == '+':
    operation = x + y
elif op == '-':
    operation = x - y
elif op == '*':
    operation = x * y
elif op == '/':
    operation = x / y
elif op == '%':
    operation = x % y
else:
    print("Invalid Character!")
    print(x, op , y, "=", operation)

