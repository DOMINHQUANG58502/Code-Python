"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_09_page_85.py
Problem:
9. Does the Boolean expression count > 0 and total // count > 0 contain a
potential error? If not, why not?
Solution:
The code contains error.
count >0 This statement is right if we match this with the syntax of regular comparison operation. Here count is
an operand, “0” is the constant operand and these two operands are operated by the operator “>”. when we take
total // count >0 Here count>0 returns Boolean and total is assumed to be an integer and an integer cannot be
divided by a Boolean value. So it can be rectified as (total // count)>0.
"""


