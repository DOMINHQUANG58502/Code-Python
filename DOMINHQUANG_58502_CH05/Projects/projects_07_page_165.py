"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_07_page_165.py
Problem:
7. Write a program that inputs a text file. The program should print the unique
words in the file in alphabetical order.
Solution:

"""
fileName = input("Enter the input file name:")
word_list = []
with open(fileName) as words:
    for line in words:
        line.rstrip()
        for list_of_words in line.split():
            print(list_of_words)
            word_list.sort()
            for list2_words in word_list:
                if list2_words not in word_list:
                    word_list.sort()
                    word_list.append(list_of_words)
                for new_words in line.split():
                    print(new_words)