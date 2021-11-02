"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_02_page_165.py
Problem:
2. Write a program that allows the user to navigate the lines of text in a file. The
program should prompt the user for a filename and input the lines of text into a
list. The program then enters a loop in which it prints the number of lines in the
file and prompts the user for a line number. Actual line numbers range from 1 to
the number of lines in the file. If the input is 0, the program quits. Otherwise, the
program prints the line associated with that number.
Solution:

"""
namefile = input("Enter the file name: ")
file = open(enterfile, 'r')
linecount = 0
for line in file:
    linecount = linecount + 1
print("The number of lines in this txt. file is", linecount)
linenum = 0
while True:
    num = int(input("Please enter a line number or press 0 to quit: "))
if num >=1 and num <= linecount:
    file = open(namefile, 'r')
    for lines in file:
        linenum = linenum + 1
        if linenum == num:
            print(lines)
else:
    if num == 0:
        print("Thanks for using the program")
        break