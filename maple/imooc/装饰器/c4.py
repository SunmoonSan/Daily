#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-19 01:08
# @site  : https://github.com/SunmoonSan
import time


def decorator(func):

    def wrapper(*args, **kwargs):
        print(time.time())
        func(*args, **kwargs)

    return wrapper


# 带关键字参数的装饰器
@decorator
def f1(a, b, **kwargs):
    print('This is a function' + a)
    print('This is a function' + b)
    print(kwargs)


f1('--a--', '--b--', c=2, d=3, e=5)