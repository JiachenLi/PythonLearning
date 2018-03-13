# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

from xml.parsers.expat import ParserCreate
from urllib_app import request

class WeatherSaxHandler(object):

    forelist = list()

    def __init__(self):
        self.weather = dict()

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.weather['city'] = attrs['city']
            self.weather['country']= attrs['country']
        if name == 'yweather:forecast':
            global forelist
            everyday = {
                'date': attrs['date'],
                'day': attrs['day'],
                'high': attrs['high'],
                'low': attrs['low'],
                'weather': attrs['text']
            }
            forelist.append(everyday)
            self.weather['forecast'] = forelist

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass

def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return handler.weather

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parse_weather(data.decode('utf-8'))