# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import base64_app

def safe_base64_decode(s):
    if len(s)%4 == 0:
        return base64_app.b64decode(s)
    else:
        while len(s)%4 != 0:
            s = s + b'='
        return base64_app.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')