#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-28 上午7:43
# @site  : https://github.com/SunmoonSan
"""
L>E>G>B
L,函数内部
G,全局
"""

passline = 60


def func(val, h=0, b=4, t='h'):
    passline = 90
    a = 3
    print(locals())
    if val >= passline:
        print('pass')
    else:
        print('fail')


func(89,t='k')
print(globals())