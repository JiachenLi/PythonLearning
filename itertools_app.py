# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import itertools_app

def pi(N):
    odd_list1 = itertools_app.count(1, 2)
    odd_list2 = list(itertools_app.takewhile(lambda x: x <= 2 * N - 1, odd_list1))
    odd_list3 = []
    for i in odd_list2:
        if odd_list2.index(i)%2 == 0:
           i = 4/i
        else:
            i = -4/i
        odd_list3.append(i)
    return sum(odd_list3)