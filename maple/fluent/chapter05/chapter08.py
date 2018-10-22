#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/21 01:01

a = [1, 2, 3]
b = a
a.append(4)
print('a', a)
print('b', b)


class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()
print(x)

# y = Gizmo() * 10
# print(y)

print(dir())
