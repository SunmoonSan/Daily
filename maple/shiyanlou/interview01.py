#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-13 下午11:46
# @site  : https://github.com/SunmoonSan


class A(object):
    def show(self):
        print("base show")


class B(A):
    def show(self):
        print("derived show")

# 调用B类show()方法


obj = B()
print(obj.__class__)
obj.show()


# 调用A类show()方法
obj.__class__ = A # 将A的类对象赋值给A
# obj = A()
print(obj.__class__)
obj.show()
obj.__class__ = B
print(obj.__class__)
obj.show()