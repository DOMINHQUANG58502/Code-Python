"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_04_page_149.py
Problem:
4. Define a function named summation. This function expects two numbers, named
low and high, as arguments. The function computes and returns the sum of the
numbers between low and high, inclusive.
Solution:

"""
low = int(input("Please enter your data : "))
high = int(input("Please enter your data : "))
def summation():
    sum = 0
    for i in (low, high):
        sum += i
    print(sum)
summation()