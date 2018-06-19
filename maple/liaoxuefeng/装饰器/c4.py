#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-19 11:09
# @site  : https://github.com/SunmoonSan
import functools
import datetime


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s(): ' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log
def now():
    print(datetime.datetime.now())

"""
now = log(now)
print(now.__name__)  # now, 不再改变函数名
now()
"""

now()
print(now.__name__)