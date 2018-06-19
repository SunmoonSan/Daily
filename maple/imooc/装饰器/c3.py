#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-19 01:03
# @site  : https://github.com/SunmoonSan

# 带多个参数的装饰器
import time


def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)  # 用*args,不是args
    return wrapper


#  装饰器的意义,增强函数功能,却不改变函数的代码结构
@decorator
def f1(a):
    print("This is a function" + a)


@decorator
def f2(a, b):
    print('This is a function' + a + b)


f1('---a---')
f2('---a---', '---b---')
