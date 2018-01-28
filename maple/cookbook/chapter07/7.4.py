#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-28 下午11:23
# @site  : https://github.com/SunmoonSan

# 返回多个值的函数


def myfun():
    return 1, 2, 3


a, b, c = myfun()
print(a)
print(b)
print(c)

a = (1, 2)
print(a)
b = 1, 2
print(b)

x = myfun()
print(x)