#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-19 下午10:32
# @site  : https://github.com/SunmoonSan

# 字典排序:
# 你想创建一个字典，
# 并且在迭代或序列化这个字典的时候能够控制元素的顺序。
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

import json
print(json.dumps(d))