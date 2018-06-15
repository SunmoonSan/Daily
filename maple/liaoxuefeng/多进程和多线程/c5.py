#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-14 23:38
# @site  : https://github.com/SunmoonSan

import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(10):
        print('thread %s >>> %s' % (threading.current_thread().name, i))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)

t = threading.Thread(target=loop, name='LoopThread')
t.start()

for i in range(10):
    print('thread %s >>> %s' % (threading.current_thread().name, i))
    time.sleep(1)

t.join()
print('thread %s ended. ' % threading.current_thread().name)
