#!/usr/bin/env python

def fzzybzzy(top):
    
    for i in range(1,top + 1):
        s = ''
        
        s += 'Fizz' if (i % 3 == 0) else ''
        s += 'Buzz' if (i % 5 == 0) else ''
        
        print s or i
    
    return
