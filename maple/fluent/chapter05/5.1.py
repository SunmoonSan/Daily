#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/17 23:54
# 5.1 把函数试作对象


def factorial(n):
    """:return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)  # :return n!
print(type(factorial))  # <class 'function'>

fact = factorial
print(fact, factorial)  # <function factorial at 0x101c141e0> <function factorial at 0x101c141e0>
print(fact(5))
print(map(factorial, range(11)))
print(list(map(factorial, range(11))))
