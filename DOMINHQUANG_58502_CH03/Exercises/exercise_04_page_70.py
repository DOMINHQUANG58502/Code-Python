"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exersice_04_page_70.py
Problem:
4. Write a loop that prints the first 128 ASCII values followed by the corresponding
characters (see the section on characters in Chapter 2). Be aware that most of the
ASCII values in the range “0..31” belong to special control characters with no standard print representation, so you might see strange symbols in the output for these
values.

Solution:

"""
for i in range(128):
    values=ascii(i)
    symbols=chr(i)
    print(symbols,end= "")
    print(values,end= "")