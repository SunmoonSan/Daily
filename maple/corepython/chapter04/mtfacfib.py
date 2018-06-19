#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-15 14:57
# @site  : https://github.com/SunmoonSan
from myThread import MyThread
from time import ctime, sleep


def fib(x):
    sleep(0.005)
    if x < 2 :
        return 1
    return fib(x-2) + fib(x-1)


def fac(x):
    sleep(0.1)
    if x<2 :
        return 1
    return x * fac(x-1)


def _sum(x):
    sleep(0.1)
    if x<2:
        return 1
    return x + _sum(x-1)


funcs = [fib, fac, _sum]
n = 12

if __name__ == '__main__':
    length = range(len(funcs))

    print('*** Single thread***')
    for i in length:
        print('starting', funcs[i].__name__, 'at: ', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())

    print('***Multi threads')
    threads = []
    for i in length:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in length:
        threads[i].start()

    for i in length:
        threads[i].join()
        print(threads[i].getResult())

    print('all DONE')