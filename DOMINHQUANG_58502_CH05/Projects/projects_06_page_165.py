"""
Author: Do Minh Quang
Date: 29/01/1997
Program: exercise_06_page_165.py
Problem:
6. Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers
in several bases.
Solution:

"""
num = int(input("Enter the Decimal: "))
baseinput = int(input("Enter the base: "))
def decimalToRep(num,baseinput):
    base = ""
    while num > 0:
        one = int(num % baseinput)
        if one < 10:
            base += str(one)
        else:
            base += chr(ord('A')+one-10)
        num //= baseinput
    base = base[::-1]
    return base
def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))

if __name__ == "__main__":
    main()