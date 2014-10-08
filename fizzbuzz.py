#!/usr/bin/env python

from sys import argv

def fizzbuzz(top):
    for i in range(1,top + 1):
        if (i % 5 == 0) and (i % 3 == 0):
            print 'FizzBuzz'
        elif (i % 3 == 0):
            print 'Fizz'
        elif (i % 5 == 0):
            print 'Buzz'
        else:
            print i
    return

fizzbuzz(argv[1])
