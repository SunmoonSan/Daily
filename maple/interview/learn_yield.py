#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-13 下午11:15
# @site  : https://github.com/SunmoonSan

mygenerator = (x*x for x in range(3)) # 生成器
print(mygenerator)
for i in mygenerator:
    print(i)

print('-'*60)


"""
yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。
重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
"""


def call(m):
    return m*2


def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
    print("do something")
    print("end.")


my_generator = yield_test(5)
for i in yield_test(5):
    print(i, ",")