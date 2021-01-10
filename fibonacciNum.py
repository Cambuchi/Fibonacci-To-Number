#!/usr/bin/env python3
# fibonacciNum.py - generate the Fibonacci sequence to a given number or to the Nth number.

def fibonacciNum(num):
    if num == 0 or num == 1:
        print(num)
    f1: int = 0
    f2: int = 1
    while f1 <= (num):
        print(f1)
        f3 = f2 + f1
        f1 = f2
        f2 = f3

if __name__ == '__main__':
    num = int(input('Please input a positive number to get the fibonacci sequence up to that number: \n'))
    try:
        if num < 0:
            print('Please enter a POSITIVE number')
        fibonacciNum(num)
    except ValueError:
        print('Please enter a NUMBER.')
