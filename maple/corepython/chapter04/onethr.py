#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-19 上午12:01
# @site  : https://github.com/SunmoonSan

from time import sleep, ctime


def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop1() 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())


def main_loop():
    print('starting at:',ctime())
    loop0()
    loop1()
    print('all Done at:', ctime())


if __name__ == '__main__':
    main_loop()