#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-28 上午8:38
# @site  : https://github.com/SunmoonSan


def dec(func):
    print('---call dec---')

    def in_dec(*args):
        print('--- in in_dec---')
        if len(args) == 0:
            return 0
        for val in args:
            if not isinstance(val, int):
                return 0
        return func(*args)

    return in_dec


@dec
def my_sum(*args):
    # if len(args) == 0:
    #     return 0
    # for val in args:
    #     if not isinstance(val, int):
    #         return 0
    print('---in my_sum---')
    return sum(args)


# 加上语法糖，不需要调用，就默认调用装饰器
# my_average = dec(my_average) 此时my_average已经指向in_dec
# my_average = in_dec
@dec
def my_average(*args):
    # if len(args) == 0:
    #     return 0
    # for val in args:
    #     if not isinstance(val, int):
    #         return 0
    print('---in my_average---')
    return sum(args) / len(args)


# my_s = dec(my_sum)
# print(my_s)
# sum_ = my_s(1, 2, 3, 4, 5)
# print(sum_)
#
# print('-'*60)
#
# my_a = dec(my_average)
# print(my_a)
# aver = my_a(1, 2, 3, 4, 5, '6')
# print(aver)

print(my_sum)
print(my_average)

print(my_sum(1, 2, 3, 4, 5))
print(my_average(1, 2, 3, 4, 5))
# print(sum((3, 4, 5)))
