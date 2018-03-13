# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import socket, threading, time

# 建立基于IPv4和TCP协议的套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置监听端口
s.bind(('127.0.0.1', 9999))

# 指定等待连接的socket的最大数量
s.listen(5)
print('Waiting for connection...')

# 服务器处理连接的客户端数据
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 创建线程处理不同客户端的连接
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()