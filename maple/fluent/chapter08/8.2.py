#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/21 08:52
# 标识, 相等性和别名
charles = {'name': "C.L.D", 'born': 1832}
lewis = charles

print(lewis is charles)
print(id(charles), id(lewis))

lewis['balance'] = 950

print(charles)
print(lewis)


alex = {'name': 'C.L.D', 'born': 1832, 'balance': 950}

print(alex == charles == lewis)
print(alex is charles)

# 元组的相对不可变性
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print('t1 == t2', t1 == t2)
print('t1 is t2', t1 is t2)

print('id0', id(t1[0]))
print('id1', id(t1[1]))
print('id2', id(t1[2]))
print('')
print('id0', id(t2[0]))
print('id1', id(t2[1]))
print('id2', id(t2[2]))
t1[-1].append(50)
print('id(t1[-1])', id(t1[-1]))
print('t1 == t2', t1 == t2)
print('t1 is t2', t1 is t2)

