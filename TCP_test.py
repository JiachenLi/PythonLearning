# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import socket

# 创建一个套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 向服务器发送HTTP请求报文
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: closer\r\n\r\n')
# 接收数据
buffer = []
while True:
    # 每次最大接收数据量为1024字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 接受的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)