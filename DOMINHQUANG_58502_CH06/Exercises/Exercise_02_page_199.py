"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_02_page_199.py
Problem:
2. Write the code for a filtering that generates a list of the positive numbers in a list
named numbers. You should use a lambda to create the auxiliary function.
Solution:

"""
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the said list: ",new_nums)

