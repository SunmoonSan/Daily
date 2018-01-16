#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-16 下午11:52
# @site  : https://github.com/SunmoonSan

# 数字的格式化输出

x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '0,.1f'))

print('-'*60)

print(format(x, 'e'))
print(format(x, '0.2E'))

print('-'*60)

print('The value is {:0,.2f}'.format(x))

print(x)
print(format(x, '0.1f'))
print(format(-x, '0.1f'))

print('-'*60)

swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))

print('%0.2')
