# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

from urllib_app import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        data = json.loads(f.read())
        print('Status: ', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data: ', data.decode('utf-8'))

url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(url)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')