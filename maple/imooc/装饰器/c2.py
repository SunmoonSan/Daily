#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-19 00:53
# @site  : https://github.com/SunmoonSan

# 带参数的装饰器
import time


def decorator(func):
    def wrapper(a):
        print(time.time())
        func(a)
    return wrapper


#  装饰器的意义,增强函数功能,却不改变函数的代码结构
@decorator
def f1(a):
    print("This is a function" + a)


# f = decorator(f1)
# f()
# ----上下等价----
f1('---a---')

