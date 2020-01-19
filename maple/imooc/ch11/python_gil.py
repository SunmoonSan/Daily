#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2019/12/20 1:15 上午
# @site  : https://github.com/SunmoonSan

# gil: global interpreter lock
# Python中一个线程对应C语言上的一个线程
# gil使得同一时刻只有一个线程在一个CPU上执行字节码

# gil会根据执行的字节码行数已经时间片释放gil, gil在遇到IO操作的时候主动释放
import dis


def add(a):
    a = a + 1
    return a


print(dis.dis(add))

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


import threading

threading1 = threading.Thread(target=add)
threading2 = threading.Thread(target=desc)
threading1.start()
threading2.start()
threading1.join()
threading2.join()
print(total)
