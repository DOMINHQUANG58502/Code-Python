"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_09_page_132.py
Problem:
9. Write a script named numberlines.py. This script creates a program listing from a
source program. This script should prompt the user for the names of two files. The
input filename could be the name of the script itself, but be careful to use a different
output filename! The script copies the lines of text from the input file to the output
file, numbering each line as it goes. The line numbers should be right-justified in
4 columns, so that the format of a line in the output file looks like this example:
1> This is the first line of text
Solution:

"""
input_filename = input('Enter input file name: ')
output_filename = input('Enter output file name: ')

with open(input_filename, 'r') as f, open(output_filename, 'w') as w:
    number = 0
    for line in f:
        number += 1
        w.write('{:>4}> {}'.format(number, line))