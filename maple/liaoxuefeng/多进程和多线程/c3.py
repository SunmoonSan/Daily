#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-14 17:39
# @site  : https://github.com/SunmoonSan
# 如果要启动大量子进程，可以用进程池的方式批量创建进程
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    for i in range(50):
        time.sleep(random.random() * 1)
        print('Process %s --- %s' % (name, i))
    end = time.time()

    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Master process %s.' % os.getpid())
    pool = Pool(4)

    for i in range(5):
        pool.apply_async(func=long_time_task, args=(i, ))

    print('Waiting for all subprocesses done...')

    for i in range(50):
        time.sleep(random.random() * 1)
        print('Master process %s' % i)

    pool.close()
    pool.join()
    print('All subprocesses done.')
