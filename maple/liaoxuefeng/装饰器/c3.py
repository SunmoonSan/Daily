#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-19 10:52
# @site  : https://github.com/SunmoonSan
import datetime


def log(text):
    print('>>> 调用log()')
    def decorator(func):
        print('>>> 调用decorator()')
        def wrapper(*args, **kwargs):
            print('>>> 调用wrapper()')
            print('%s %s(): ' % (text, func.__name__))
        return wrapper
    return decorator


@log('San')  # 等价于decorator = log('San'), wrapper = decorator(now), wrapper指向now()函数
def now():  # 带装饰的函数
    print(datetime.datetime.now())


now()
print(now.__name__)  # 函数名变成wrapper了
"""
>>> 调用log()
>>> 调用decorator()
>>> 调用wrapper()
San now(): 
wrapper
"""

# decorator = log('San')
# print(decorator.__name__)
# wrapper = decorator(now)
# print(wrapper.__name__)
"""
>>> 调用log()
decorator
>>> 调用decorator()
wrapper
"""