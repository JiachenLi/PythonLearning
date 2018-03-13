# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

from flask import Flask, render_template

app = Flask(__name__, template_folder=r'D:\Projects\templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)