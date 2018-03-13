# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import re

def is_valid_email(addr):
    stremail = str(addr)
    if re.match(r'[0-9a-zA-Z][0-9a-zA-Z._]*@[0-9a-zA-Z]+\.\w{3}', stremail):
        print('%s is a correct email address' % stremail)
    else:
        print('%s is a wrong email address' % stremail)

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')