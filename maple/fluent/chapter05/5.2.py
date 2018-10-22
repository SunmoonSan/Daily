#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/17 23:54
# 5.2高阶函数
from functools import reduce
from operator import add

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
fruits_sorted = sorted(fruits, key=len)
print(fruits_sorted)


def reverse(word):
    return word[::-1]


print(reverse('testing'))

print(sorted(fruits, key=reverse))


def factorial(n):
    """:return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(list(map(factorial, range(6))))
li = [factorial(n) for n in range(6)]
print(li)

print(all([]))

print(reduce(add, range(100)))
print(sum(range(100)))
