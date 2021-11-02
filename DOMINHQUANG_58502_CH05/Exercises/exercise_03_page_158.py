"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_03_page_158.py
Problem:
3. Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
expressions that perform the following tasks:
a. Replace the value at the key 'b' in data with that value’s negation.
b. Add the key/value pair 'c':40 to data.
c. Remove the value at key 'b' in data, safely.
d. Print the keys in data in alphabetical order.
Solution:
a.data.get("b")
b.data.update({'c': 40})
c.print(data)
d.list(data.keys())
"""
