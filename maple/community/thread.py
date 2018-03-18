#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-18 下午10:08
# @site  : https://github.com/SunmoonSan

import threading
import time


def worker(num):
    """
    thread worker function
    :param num:
    :return:
    """
    time.sleep(1)
    for i in range(10):
        print('The num is %d---%d' % (num, i))
    return


for i in range(20):
    t = threading.Thread(target=worker, args=(i,), name='t.%d' % i)
    t.start()