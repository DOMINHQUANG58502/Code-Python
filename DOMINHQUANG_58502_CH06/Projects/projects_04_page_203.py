"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_04_page_203.py
Problem:
4. Restructure Newton’s method (Case Study 3.6) by decomposing it into three
cooperating functions. The newton function can use either the recursive strategy
of Project 1 or the iterative strategy of Case Study 3.6. The task of testing for the
limit is assigned to a function named limitReached, whereas the task of computing a new approximation is assigned to a function named improveEstimate. Each
function expects the relevant arguments and returns an appropriate value.
Solution:
"""
import math
TOLERANCE = 0.000001

def newton(x, estimate=1):
    if limitReached(x, estimate):
        return estimate
    else:
        return newton(x, improveEstimate(x, estimate))

def limitReached(x, estimate):
    difference = abs(x - estimate ** 2)
    return difference <= TOLERANCE

def improveEstimate(x, estimate):
    return (estimate + x / estimate) / 2

def main():
    while True:
        x = input("Enter a positive number or enter/ return to quit: ")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is", newton(x, 1))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == '__main__':
    main()

