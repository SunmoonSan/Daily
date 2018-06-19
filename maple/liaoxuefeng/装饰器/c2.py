#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-19 10:40
# @site  : https://github.com/SunmoonSan
"""
现在,我们要增强函数now()的功能,在调用钱自动打印日志, 但是又不改动now()函数
这种在代码运行期间动态增加功能的方式,称之为 装饰器
"""
import datetime


def log(func):  # 定义装饰器函数
    def wrapper(*args, **kwargs):  # func可以接受任何参数
        print('call %s(): ' % func.__name__)
        return func(*args, **kwargs)
    return wrapper  # 返回内部函数


@log  # 等价于now = log(now)
def now():  # 带装饰的函数
    print(datetime.datetime.now())


now()