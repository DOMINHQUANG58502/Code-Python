"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_10_page_63.py
Problem:

Solution:

"""
wage= float(input("Enter the wage: $"))
regularHours = float(input("Enter the regular hours: "))
overtimeHours = float(input("Enter the overtime hours:"))

totalpay = regularHours * wage * overtimeHours * wage *1.5

print("The total weekly pay is $"+ str(round(totalpay,2)))