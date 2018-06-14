#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018-06-14 16:40
# @site  : https://github.com/SunmoonSan

# 多进程（multiprocessing）
# 要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
# 但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
# 然后，分别在父进程和子进程内返回。
# 子进程永远返回 0， 而主进程返回子进程的ID，这样做的理由是，一个主进程可以fork出很多
# 子进程，所以主进程要记下子进程的ID，而而子进程调用getppid()就可以获得主进程的ID。
import os

print('Process (%s) start' % os.getpid())

# Only work on Unix,Linux, Mac
pid = os.fork()
print('pid >>> ', pid)
if pid == 0:
    print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s)' % (os.getpid(), pid))