# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<hl>Hello, world!</hl>'

if __name__ == '__main__':
    app.run(debug=True)

