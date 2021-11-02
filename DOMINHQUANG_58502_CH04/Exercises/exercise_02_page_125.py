"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_02_page_125.py
Problem:
2. Write a code segment that opens a file for input and prints the number of
four-letter words in the file.
Solution:
"""
count = 0
inputFile = open("myfile.txt", 'r')

for line in inputFile:

    wordlist = line.split()

    for word in wordlist:

        if len(word) == 4:

            count += 1

print("There are", count, "lines.")

