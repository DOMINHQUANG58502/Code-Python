"""
Author: Do Minh Quang
Date: 29/01/1997
Program: casestudy_01_page_126.py
Problem:
Solution:
"""
"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_05_page_125.py
Problem:
5. Write a code segment that prompts the user for a filename. If the file exists, the
program should print its contents on the terminal. Otherwise, it should print an
error message.
Solution:
"""
# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()
# Count the sentences
sentences = text.count('.') + text.count('?') + \
 text.count(':') + text.count(';') + \
 text.count('!')
# Count the words
words = len(text.split())

# Count the syllables
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
# Compute the Flesch Index and Grade Level
index = 206.835 – 1.015 * (words / sentences) – \
 84.6 * (syllables / words)
level = round(0.39 * (words / sentences) + 11.8 * \
 (syllables / words) – 15.59)
# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")
