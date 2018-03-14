#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-14 下午11:01
# @site  : https://github.com/SunmoonSan


class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self, *args):
        print('default')

    def __getattr__(self, item):
        return self.mydefault


a1 = A(10, 20)
a1.fn1()
a1.fn2(40)
a1.fn3('Jasmine')