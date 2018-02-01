#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-2-1 下午10:51
# @site  : https://github.com/SunmoonSan

# 定义匿名或内联函数


add = lambda x, y: x + y
print(add(2, 3))
print(add('hello', 'world'))


def add(x, y):
    return x + y


names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))