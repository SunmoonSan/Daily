#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-17 上午12:06
# @site  : https://github.com/SunmoonSan

# 完美立方
#  a*a*a = b*b*b + c*c*c + d*d*d
#  a,b,c,d>1, b<=c<=d

if __name__ == '__main__':
    N = int(input("一个正整数>>>"))
    for a in range(2,N):
        for b in range(2, a):
            for c in range(b, a):
                for d in range(c, a):
                    if a*a*a == b*b*b + c*c*c + d*d*d:
                        print(a,b,c,d)


