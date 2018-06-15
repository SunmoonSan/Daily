#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-19 上午12:21
# @site  : https://github.com/SunmoonSan

import _thread
from time import sleep, ctime

loops = [2, 4]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()


def main_loop():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

        print('all Done at:', ctime())


    if __name__ == '__main__':
        main_loop()