#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/16 09:11
from collections import abc

my_dict = {}
print(isinstance(my_dict, abc.Mapping))

print('-' * 100)

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

print(a == b == c == d == e)

print('-' * 100)

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    ('81', 'Japan')
]

country_code = {country: code for code, country in DIAL_CODES}
print(type(country_code))
print(country_code)

code_country = {code: country.upper() for country, code in country_code.items() if int(code) < 66}
print(code_country)

print('-'*100)
