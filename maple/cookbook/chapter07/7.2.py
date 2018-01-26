#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-26 下午10:45
# @site  : https://github.com/SunmoonSan

# 只接受关键字参数的函数


def recv(maxsize, *, block):
    "Receives a message"
    pass


# print(recv(1024, True))
print(recv(1024, block=True))


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m;
    return m


print(mininum(1, 5, 2, -5, 10))
print(mininum(1, 5, 2, -5, 10, clip=0))

print(help(recv))
print(help(mininum))