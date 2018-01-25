#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-25 下午11:13
# @site  : https://github.com/SunmoonSan

# 可接受任意数量参数的函数


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1,2))
print(avg(1, 2, 3, 4))

import html


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )

    return element


print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))
