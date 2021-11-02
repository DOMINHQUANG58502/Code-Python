"""
Assignment 11: On Tap 02
Date : 30/10/2021
Author: DO MINH QUANG

"""
binary = int(input("Nhập số nhi phan = "))

def Cau1(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print("Số thập phân là:", decimal)

if __name__ == '__main__':
    Cau1(binary)