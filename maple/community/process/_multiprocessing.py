#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/12/13 17:07
from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
