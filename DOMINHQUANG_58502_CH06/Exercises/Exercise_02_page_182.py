"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_02_page_182.py
Problem:
2. The factorial of a positive integer n, fact(n), is defined recursively as follows:
 fact( ) n 1 5 , when n 1 5
 fact( ) n n 5 2 * fact n( ) 1 , otherwise
 Define a recursive function fact that returns the factorial of a given positive
integer.
Solution:
"""
def fact(n):
   if n == 1 or n==0:
       return 1
   else :
       return n*fact(n-1)

print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))