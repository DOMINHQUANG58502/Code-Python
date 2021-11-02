"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_11_page_132.py
Problem:
11. Jack just completed the program for the Flesch text analysis from this chapter’s
case study. His supervisor, Jill, has discovered an error in his code. The error
causes the program to count a syllable containing consecutive vowels as multiple
syllables. Suggest a solution to this problem in Jack’s code and modify the program so that it handles these cases correctly.
Solution:

"""
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

sentences = text.count('.') + text.count('?') + \
text.count(':') + text.count(';') + \
text.count('!')
words = len(text.split())
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
for ending in ['es', 'ed', 'e']:
    if word.endswith(ending):
         syllables -= 1
    if word.endswith('le'):
        syllables += 1

index = 206.835 - 1.015 * (words / sentences) - \
84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
(syllables / words) - 15.59))

print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")