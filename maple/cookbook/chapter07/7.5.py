#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-30 下午11:23
# @site  : https://github.com/SunmoonSan

# 定义有默认参数的函数


def spam(a, b=42):
    print(a, b)


spam(1)
spam(1, 2)


def spam1(a, b=None):
    if b is None:
        b = []


_no_value = object()


def spam2(a, b=_no_value):
    if b is _no_value:
        print("No b value supplied")


spam2(1)
spam2(1, 2)
spam2(1, None)

x = 42
def spam3(a, b=x):
    print(a, b)

spam3(1)
x = 23
spam3(1)


def spam4(a, b=[]):
    print(b)
    return b


x = spam4(1)
print(x)
x.append(99)
x.append('Yow!')
print(x)
spam4(1)

# def spam4(a, b=None):
#     if not b:
#         b = []
