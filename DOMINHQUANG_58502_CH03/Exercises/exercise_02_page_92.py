"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_02_page_92.py
Problem:
2. The factorial of an integer N is the product of the integers between 1 and N, inclusive. Write a while loop that computes the factorial of a given integ
Solution:

"""
n = int(input("Input a number to compute the factiorial : "))
factorial = 1
if n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,n + 1):
        factorial = factorial * i
    print("The factorial of",n,"is",factorial)
