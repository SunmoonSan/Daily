#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-15 下午11:51
# @site  : https://github.com/SunmoonSan

# 数字的四舍五入

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

print('-'*60)

a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

print('-'*60)

x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))

print('-'*60)

a = 2.1
b = 4.2
c = a + b
print(c)
c = round(c, 2)
print(c)


