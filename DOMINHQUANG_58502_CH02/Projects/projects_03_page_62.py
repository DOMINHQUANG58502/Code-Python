"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_03_page_62.py
Problem:
3. Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
like to buy LP record albums. The store rents new videos for $3.00 a night, and
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
can use to calculate the total charge for a customer’s video rentals. The program
should prompt the user for the number of each type of video and output the total
cost.
Solution:

"""
new=int(input("Nhập vào số lượng video mới: "))
old=int(input("Nhập vào số lượng video cũ: "))
Result=(new*3.00)+(old*2.00)
print("Tổng số tiền chi trả","$",Result)

