
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

def fact(n):
    '''

    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(9999)
    Traceback (most recent call last):
       ...
    RecursionError: maximum recursion depth exceeded in comparison

    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
