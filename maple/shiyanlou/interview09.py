#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-14 下午11:10
# @site  : https://github.com/SunmoonSan


def nulby(num):
    def gn(val):
        return num * val
    return gn


zw = nulby(7)
print(zw)
print(zw(9))