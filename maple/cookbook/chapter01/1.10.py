#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-20 下午10:37
# @site  : https://github.com/SunmoonSan

# 删除序列相同元素并保持顺序


def dedeupe(items):
    seen = set()
    for item in items:
        if item not in items:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedeupe(a)))

import re
s =  'Ryszard Kapuściński（瑞斯札德．卡普欽斯基） / 胡洲賢 / 馬可孛羅文化事業股份有限公司 / 2008/10/02 / 152.00元'
match = re.search(r'\d{4}/\d{2}/\d{2}', s)
t = s.replace(match.group(0), ' ')
print(t)
print(t.split('/', 3))
# print(match.group(0))
# t = s.split('/', 4)
# print(t)

import random

print(random.randint(0, 9))