#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-28 上午7:51
# @site  : https://github.com/SunmoonSan
passline = 60

'''
def func_100(val):
    passline = 60
    if val >= passline:
        print('pass')
    else:
        print('fail')


def func_150(val):
    passline = 90
    if val >= passline:
        print('pass')
    else:
        print('fail')
'''


def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print('pass')
        else:
            print('fail')
    return cmp


f_100 = set_passline(60)
print(f_100)
print(f_100.__name__)
f_100(78)
f_100(46)

f_150 = set_passline(90)
f_150(98)
f_150(76)
