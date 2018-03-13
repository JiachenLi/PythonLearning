
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import os
from datetime import datetime

pwd = os.path.abspath('.')
print('%s 的目录' % pwd)

for x in os.listdir(pwd):
    x_size = os.path.getsize(x)
    modified_time = datetime.fromtimestamp(os.path.getmtime(x)).strftime('%y/%m/%d %H/%M')
    x_type = '<DIR>' if os.path.isdir(x) else ''
    print('%s%9s%9d %s' % (modified_time, x_type, x_size, x))
