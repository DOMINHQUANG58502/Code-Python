"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_02_page_149.py
Problem:
2. Define a function named even. This function expects a number as an argument and
returns True if the number is divisible by 2, or it returns False otherwise. (Hint: A
number is evenly divisible by 2 if the remainder is 0.)
Solution:

"""
numbers = [10,35,2,15,4,100,1,20]
def is_even(number):
    if number % 2 == 0:
        print (number,"is even")
        return True
    else:
        print (number, "is odd")
        return False
for number in numbers:
    is_even(number)