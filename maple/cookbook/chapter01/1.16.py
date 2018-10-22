#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-18 下午11:30
# @site  : https://github.com/SunmoonSan

# 过滤序列元素
mylist = [1,4,-5,10,-7,2,3,-1]
print(mylist)
print([n for n in mylist if n<0])

print('-'*60)

pos = (n for n in mylist if n>0)
for x in pos:
    print(x)

print('-'*60)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

print('-'*60)

mylist = [1,4,-5,10,-7,2,3,-1]
import math
print([math.sqrt(n) for n in mylist if n>0])

print('-'*60)

clip_neg = [n if n>0 else 0 for n in mylist]
print(clip_neg)

address = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0,3,10,4,1,7,6,1]
from itertools import compress
more5 = [n>5 for n in counts]
print(more5)
l = list(compress(address, more5))
print(l)
