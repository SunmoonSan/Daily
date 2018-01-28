#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-28 下午10:23
# @site  : https://github.com/SunmoonSan

# 给函数参数增加元信息


def add(x:int, y,int) ->int:
    return x + y


print(help(add))
print(add.__annotations__)