
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

class Dict(dict):

    def __init__(self, **kw):       #
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribiute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
