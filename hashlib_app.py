# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import hashlib_app, random

def get_md5(s):
    return hashlib_app.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def register():
    username = input('Username: ')
    password = input('Password: ')
    user = User(username, password)
    db[username] = get_md5(str(user.username) + str(user.password) + str(user.salt))

def login():
    username = str(input('Username: '))
    password = str(input('Password: '))
    if username in db:
        if get_md5(password + db[username].salt) == db[username].password:
            return True
        else:
            print('Wrong password')
    else:
        print('Wrong username')