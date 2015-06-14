#!/usr/bin/env python

from sys import argv

def fizzbuzz(top):
    for i in range(1,int(top) + 1):
        s = ''
        s += 'Fizz' if (i % 3 == 0) else ''
        s += 'Buzz' if (i % 5 == 0) else ''
        print s or i
    return

fizzbuzz(argv[1])

