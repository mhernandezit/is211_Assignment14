#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Michael Hernandez
#IS211 Assignment 14

def fibonacci(n):
    """ Fibonacci sequence recursive function """
    if n < 0:
        print "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print fibonacci(15)

def gcd(x, y):
    """ Greatest common denominator recursive function """
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

print(gcd(12, 6))

def compareTo(string1, string2):
    """ A recursive function to compare string lengths """
    if not string1 and not string2:
        return 0
    elif not string1:
        return -1
    elif not string2:
        return 1
    else:
        return compareTo(string1[1:], string2[1:])

print compareTo('shortstr', 'longstring')
print compareTo('same', 'same')
print compareTo('longstring', 'shortstr')