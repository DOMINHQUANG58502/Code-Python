"""
Author: Do Minh Quang
Date: 29/01/1997
Program: casestudy_01_page_73.py
Problem:

Solution:

"""
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))
rate = rate / 100
totalInterest = 0.0
print("%4s%18s%10s%16s" % ("Year", "Starting balance",     "Interest", "Ending balance"))
for year in range(1, years + 1):
 interest = startBalance * rate
 endBalance = startBalance + interest
 print("%4d%18.2f%10.2f%16.2f" % \
 (year, startBalance, interest, endBalance))
 startBalance = endBalance
 totalInterest += interest