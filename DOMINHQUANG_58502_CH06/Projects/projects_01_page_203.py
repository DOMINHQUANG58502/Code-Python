"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_01_page_203.py
Problem:
1. Package Newton’s method for approximating square roots (Case Study 3.6) in a
function named newton. This function expects the input number as an argument
and returns the estimate of its square root. The script should also include a main
function that allows the user to compute square roots of inputs until she presses
the enter/return key.
Solution:
"""
import math
TOLERANCE = 0.000001
def newton(x):
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) /2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break
    return estimate
def main():
    while True:
        x = input("Enter a positive number or enter/ return to quit: ")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == '__main__':
    main()