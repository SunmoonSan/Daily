#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-19 10:34
# @site  : https://github.com/SunmoonSan
# 由于函数也是一个对象,而且函数对象可以被赋值给变量, 所以, 通过变量也能调用该函数
import datetime


def now():
    print(datetime.datetime.now())


f = now  # 函数赋值给变量
f()
print('-'*60)
print(now.__name__, f.__name__)
print(id(now), id(f))  # 变量f和函数now地址一样

