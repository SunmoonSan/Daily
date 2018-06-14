#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-14 16:59
# @site  : https://github.com/SunmoonSan
"""
由于Windows没有fork调用，上面的代码在Windows上无法运行。
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，
就fork出子进程来处理新的http请求。
multiprocessing
如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
"""
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_process(name):
    print('Run child process %s (%s)' % (name, os.getpid()))
    for i in range(1000):
        print('Child process >>> ', i)


if __name__ == '__main__':
    print('Master process %s.' % os.getpid())

    p = Process(target=run_process, args=('test',))
    print('Child process will start')
    p.start()

    for i in range(1000):
        print('Master process >>> ', i)
    p.join()
    print('Child process end')
