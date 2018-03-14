#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-14 下午10:53
# @site  : https://github.com/SunmoonSan


num = 9


def f1():
    num = 20


def f2():
    print(num)


f2()
f1()
f2()

print('-'*60)


def f3():
    global num
    num = 20


def f4():
    print(num)


f4()
f3()
f4()
