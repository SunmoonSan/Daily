#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-15 00:40
# @site  : https://github.com/SunmoonSan
"""
多线程和多进程最大的不同在于,多进程中,同一个变量,各有一份拷贝存在于每个进程中,
互不影响. 而多进程中,所有的变量都由所有线程共享,所以,任何一个变量都可以被任何
一个线程篡改,因此,线程之间共享数据最大的危险在于多个线程同时改一个变量,把内容
改的乱套了.
Lock
"""

import time, threading


balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    time.sleep(0.1)
    balance = balance - n
    return balance

# 给change_it()上一把锁,当某个线程开始执行change_it()时,我们说,该线程因为获得了锁
# 因此其他线程不能同时执行change_it(),只能等待,直到锁被释放,获得该锁后方能篡改.由于锁
# 只有一个,无论多少线程,同一时刻最多只有一个线程持有该锁,所以不会造成篡改冲突.
def run_thread(n):
    for i in range(20):
        # 先要获取锁
        lock.acquire()
        try:
            # 一个线程在篡改数据的同时,其他线程不能进行篡改了
            b = change_it(n)
            print('thread %s run >>> %s' % (threading.current_thread().name, b), i)
        finally:
            # 篡改完以后一定要释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t3 = threading.Thread(target=run_thread, args=(9,))
t4 = threading.Thread(target=run_thread, args=(4,))
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
print(balance)
