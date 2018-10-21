#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/21 10:06
# 默认做浅复制
import copy

l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
l3 = l1[:]
print(l1)
print(l2)
print(l3)


print(l1 == l2 == l3)
print(id(l1), id(l2), id(l3))
print(l2 is l1)
print(l3 is l1)

print('-' * 100)

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)

l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)

print('-' * 100)


class Bus:
    def __init__(self, passengers):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)


