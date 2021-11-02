"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_08_page_132.py
Problem:
8. Write a script named copyfile.py. This script should prompt the user for the
names of two text files. The contents of the first file should be input and written
to the second file.
Solution:

"""
file1 = input(" please enter name of firts file : ")
file2 = input(" please enter name of Second file : ")
with open(file1) as f:
    with open(file2 , "w") as f1:
        f1.write(line)
log = open(file2,"r")
for line in log:
    print(line)
