#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-14 下午10:47
# @site  : https://github.com/SunmoonSan


ls = [1, 2, 3, 4]
list1 = [i for i in ls if i>2]
print(list1)

list2 = [i*2 for i in ls if i>2]
print(list2)

dic1 = {x:x**2 for x in (2, 4, 6)}
print(dic1)

dic2 = {x: 'item' + str(x**2) for x in (2, 4, 6)}
print(dic2)

set1 = {x for x in 'hello world' if x not in 'low level'}
print(set1)