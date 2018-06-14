#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-14 20:51
# @site  : https://github.com/SunmoonSan
# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
# Python的multiprocessing模块包装了底层的机制,提供了Queue, Pipes等多种
# 方式来交换数据.
# 以Queue为例,在主进程创建2个子进程,一个往Queue里写数据,一个从Queue里读数据

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程
def write_process(q):
    print('Process to write %s' % os.getpid())
    for value in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程
def read_process(q):
    print('Process to read %s ' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 主进程创建Queue, 并传递给各个子进程
    q = Queue()
    pw = Process(target=write_process, args=(q,))
    pr = Process(target=read_process, args=(q,))

    # 启动子进程pw
    pw.start()
    # 启动子进程pr
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程是死循环,无法等待结束,只能强行终止
    pr.terminate()