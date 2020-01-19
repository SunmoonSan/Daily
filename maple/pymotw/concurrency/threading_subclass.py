#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2020/1/19 14:00
import logging
import threading


class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

for i in range(5):
    t = MyThread()
    t.start()
