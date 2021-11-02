"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_04_page_145.py
Problem:
4. Write a loop that accumulates the sum of the numbers in a list named data.
Solution:
total = 0
for num in data:
total += num
print(total)
"""
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))