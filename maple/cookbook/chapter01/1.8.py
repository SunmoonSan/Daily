#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-19 下午10:41
# @site  : https://github.com/SunmoonSan

# 字典的运算
# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print("min_price>>>", min_price)
print("max_price>>>", max_price)

print('-'*60)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。
# 比如，下面的代码就会产生错误：
# prices_and_names = zip(prices.values(), prices.keys())
# print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

# 如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是值。比如：

print(min(prices))
print(max(prices))

print(min(prices.values()))
print(max(prices.values()))

print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)

prices = {'AAA': 45.23, 'ZZZ':45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
