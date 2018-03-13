# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

from wsgiref.simple_server import make_server
# 导入编写好的监听程序
from hello import application

# 创建服务器
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听8000端口
httpd.serve_forever()