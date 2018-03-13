# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 解析Message对象的层次结构
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s----------' % (' ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_comtent_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % (' ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))

# 邮件内容的解码函数
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 检测编码函数
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

# 输入邮箱地址、密码及POP3服务器域名
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

# 连接到POP3服务器
server = poplib.POP3(pop3_server)
# 返回每一步结果
server.set_debuglevel(1)
# 获取POP3服务器欢迎文字
print(server.getwelcome().decode('utf-8'))

# 邮箱账户密码登陆
server.user(email)
server.pass_(password)

# stat()方法返回邮箱邮件数目和占用空间
print('Message: %s. Size: %s' % server.stat())
# list()方法返回所有邮件编号
resp, mails, octets = server.list()
print(mails)

# 获取最新一封邮件
index = len(mails)
# lines储存了邮件的每一行内容
# retr()方法检索整个消息号并标记为已读
resp, lines, octets = server.retr(index)
# 获得邮件原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 解析邮件
msg = Parser().parsestr(msg_content)

server.quit()