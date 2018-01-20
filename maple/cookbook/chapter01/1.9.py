#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-20 下午10:17
# @site  : https://github.com/SunmoonSan

# 查找两字典的相同点
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

print('-'*60)

c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
