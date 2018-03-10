#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-10 下午3:36
# @site  : https://github.com/SunmoonSan


class MyClass():
    def __init__(self):
        self.__superprivate = 'Hello'
        self._semiprivate = ', world!'


mc = MyClass()
print(mc._semiprivate)
print(mc.__dict__)
