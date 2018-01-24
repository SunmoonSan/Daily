#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-24 下午9:31
# @site  : https://github.com/SunmoonSan

# 判断线程是否已经启动

"""
from threading import Thread, Event
import time


def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


started_evt = Event()
print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

started_evt.wait()
print('countdown is running')
"""

import threading
import time


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True

        t.start()

    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


ptimer = PeriodicTimer(5)
ptimer.start()


def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1


threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()