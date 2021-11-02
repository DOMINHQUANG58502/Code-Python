"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_12_page_132.py
Problem:
12. The Payroll Department keeps a list of employee information for each pay period
in a text file. The format of each line of the file is the following:
<last name> <hourly wage> <hours worked>
Write a program that inputs a filename from the user and prints to the terminal a
report of the wages paid to the employees for the given period. The report should
be in tabular format with the appropriate header. Each line should contain an
employee’s name, the hours worked, and the wages paid for that period.
Solution:

"""
# Put your code here
filename = input("Enter the file name: ")
inputfile = open(filename, 'r')
print('\n%-15s%-10s%-10s' % ('Name', 'Hours', 'Total Pay'))
for line in inputfile:
    dataList = line.split()
    name = str(dataList[0])
    hours = int(dataList[1])
    payRate = float(dataList[2])
    totalPay = hours *payRate
print('%-15s%-10d%-10.2f' %(name,hours,totalPay))
