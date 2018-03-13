# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import re

def name_of_email(addr):
    s = str(addr)
    m = re.match(r'/^\<([a-zA-Z\s]+)\>\s([a-zA-Z][a-zA-Z\d\_\.]*@[a-zA-Z\d]+\.[a-zA-Z]{2,3})$/', s)
    if m:
        print(m.group(1))
    else:
        print('can\'t get the name of email')