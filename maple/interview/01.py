#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-10 下午5:54
# @site  : https://github.com/SunmoonSan


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i


mygenerator = createGenerator()
print(mygenerator)

for i in mygenerator:
    print(i)