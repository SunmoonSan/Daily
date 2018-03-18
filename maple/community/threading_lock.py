#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-18 下午10:29
# @site  : https://github.com/SunmoonSan

import threading
import time

globals_num = 0

lock = threading.RLock()


def func(name):
    lock.acquire()  # 获得锁
    global globals_num
    globals_num += 1
    time.sleep(1)
    print(globals_num, '线程>>> ', name)
    lock.release()  # 释放锁


for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    t.start()