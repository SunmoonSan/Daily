#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-2-6 下午10:19
# @site  : https://github.com/SunmoonSan
from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)
s1(2, 3, 4)

s1(4, 5, 6)
s2 = partial(spam, d=42)
s2(1, 2, 3)
s2(4, 5, 5)
s3 = partial(spam, 1, 2, d=42)
s3(3)
s3(4)
s3(5)

print('-'*60)

points = [(1,2), (3,4), (5,6), (7,8)]
import math


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)


pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)