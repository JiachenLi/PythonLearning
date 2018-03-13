# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import struct_app

def bmp_info(bmp):
    with open(bmp, 'rb') as f:
        info = struct_app.unpack('<ccIIIIIIHH', f.read(30))
        if info[0] == b'B':
            if info[1] == b'M' or info[1] == b'A':
                print('The file is a bmp')
                print('width: ', info[6], 'height: ', info[7], 'color: ', info[9])
            else:
                print('It\'s not a bmp')
        else:
            print('It\'s not a bmp')