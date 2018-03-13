# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import hmac_app, random

def hmac_md5(key, s):
    return hmac_app.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def register():
    username = input('Username: ')
    password = input('Password: ')
    user = User(username, password)
    db[username] = hmac_md5(user.key, str(user.username) + str(user.password))

def login():
    username = str(input('Username: '))
    password = str(input('Password: '))
    if username in db:
        if hmac_md5(db[username].key, password) == db[username].password:
            return True
        else:
            print('Wrong password')
    else:
        print('Wrong username')