#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-10 下午4:07
# @site  : https://github.com/SunmoonSan


def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))


print_everything('apple', 'banana', 'cabbage')


def table_things(**kwargs):
    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


table_things(apple='fruit', cabbage='vegetable')


def print_three_things(a, b, c):
    print('a={0}, b={1}, c={2}'.format(a, b, c))


mylist = ['aa', 'bb', 'cc']
print_three_things(*mylist)  # 解压列表

for i in mylist:
    print(i)
    print(i)


for j in  mylist:
    print(j)
