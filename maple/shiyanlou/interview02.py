#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-14 上午12:00
# @site  : https://github.com/SunmoonSan


class A(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)

    def __call__(self, num):
        print('call:', num+self.__a+self.__b)


a1 = A(10, 20)
a1.myprint()
a1(80)