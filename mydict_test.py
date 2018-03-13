
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    # 测试Dict能否正确生成实例
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    # 测试Dict实例能否用dict的方法取值
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    # 测试Dict实例能否用新的getattr属性取值
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    # 测试能否抛出KeyError
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    # 测试能否抛出AttributeError
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # 每次测试前的初始化工作
    def setUp(self):
        print('setUp...')

    # 每次测试后的善后工作
    def turnDown(self):
        print('turnDown...')
