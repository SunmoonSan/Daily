#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2020/1/19 11:18
import logging
import threading
import time


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

d = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()
