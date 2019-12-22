#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2019/12/21 11:38 上午
# @site  : https://github.com/SunmoonSan
"""
12.3 线程间通信
"""
from queue import Queue
from threading import Thread


def producer(out_q):
    while True:
        out_q.put('a')


def consumer(in_q):
    while True:
        data = in_q.get()
        print(data)


q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
