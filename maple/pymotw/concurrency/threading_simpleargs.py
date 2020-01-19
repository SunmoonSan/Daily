#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2020/1/19 10:30
import threading
import time


def worker(num):
    """thread worker function"""
    print("Worker: %s" % num)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
