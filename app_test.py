# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<hl>Home</hl>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form acti-on="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['userna8me'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run(debug=True)
