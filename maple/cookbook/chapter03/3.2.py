#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-16 下午11:41
# @site  : https://github.com/SunmoonSan

# 执行精确的浮点数运算

a = 4.2
b = 2.1
print(a + b)  # 6.300000000000001
print((a + b) == 6.3)  # False

print('-'*60)

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)  # 6.3
print((a+b) == Decimal('6.3'))  # True

print('-'*60)

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

print('-'*60)

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))

import math
print(math.fsum(nums))

