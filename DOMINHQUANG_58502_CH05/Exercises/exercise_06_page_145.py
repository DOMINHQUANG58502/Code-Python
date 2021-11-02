"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_06_page_145.py
Problem:
6. Write a loop that replaces each number in a list named data with its absolute value.

Solution:

"""
def main():
    data = [2,3,-2,-3]
    j=0
    for x in data:
        if x < 0:
            x=abs(x)
            data[j]=x
        j+=1
    print(data)
main()