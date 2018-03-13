# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParse(HTMLParser):

    def __init__(self):
        self.event = dict()

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and attrs['class'] == 'event-title':
            self.event['eventwebsite'] = attrs['href']

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        pass

    def handle_comment(self, data):
        pass

    def handle_entityrsf(self, name):
        pass

    def handle_charref(self, name):
        pass

parser = MyHTMLParse()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser --!>
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END<p>
</body></html>''')