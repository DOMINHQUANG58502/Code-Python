"""
Author: Do Minh Quang
Date: 29/01/1997
Program: projects_07_page_203.py
Problem:
7. Write a recursive function that expects a pathname as an argument. The pathname can be either the name of a file or the name of a directory. If the pathname
refers to a file, its name is displayed, followed by its contents. Otherwise, if the
pathname refers to a directory, the function is applied to each name in the directory. Test this function in a new program.
Solution:
"""
def displayFile(path):
    if os.path.isfile(path):
        print("File name: " + path)
        f = open(path, 'r')
        print(f.read())
    else:
        print("Directory name: "+ path)
        lyst = os.listdir(path)
        for element in lyst:
            recursive_element = os.path.join(path, element)
            print("element:", element)
            print("recursive_element:", recursive_element)
            displayFile(recursive_element)


if __name__ == '__main__':
    print(f"Directory: {os.getcwd()}")
    displayFile(os.getcwd())