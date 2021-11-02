"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_05_page_145.py
Problem:
5. Assume that data refers to a list of numbers, and result refers to an empty list.
Write a loop that adds the nonzero values in data to the result list, keeping them
in their relative positions and excluding the zeros.
Solution:

"""
list = [1, -4, 5, -8]
result = []
index = 0

while index<len(list):
    list[index] = abs(list[index])
    index += 1
    result.append(list)
    print(result)
