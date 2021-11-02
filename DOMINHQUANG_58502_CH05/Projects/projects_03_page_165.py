"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_03_page_165.py
Problem:
3. Modify the sentence-generator program of Case Study 5.3 so that it inputs its
vocabulary from a set of text files at startup. The filenames are nouns.txt, verbs.
txt, articles.txt, and prepositions.txt. (Hint: Define a single new function,
getWords. This function should expect a filename as an argument. The function
should open an input file with this name, define a temporary list, read words
from the file, and add them to the list. The function should then convert the list
to a tuple and return this tuple. Call the function with an actual filename to initialize each of the four variables for the vocabulary.)
Solution:

"""
import random
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def sentence():
    return nounPhrase() + " " + verbPhrase()
def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
    prepositionalPhrase()
def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()
def main():
    number = int(input("Enter the number of sentences: "))
for count in range(number):
    print(sentence())
    if __name__ == "__main__":

main()