#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-10 上午10:06
# @site  : https://github.com/SunmoonSan

a = 1
print("before>>> ", id(a), id(1))


def fun(a):
    print("func_in", id(a))
    a = 2
    print("a_addr>>> ", id(a), "2_addr>>> ", id(2))


fun(a)
print("after>>> ", id(a))
print(a)  # 1


b = []


def fun1(b):
    b.append(1)


fun1(b)
print(b)

print("="*60)


def try_to_change_list_contents(the_list):
    """
    引用传递
    :param the_list:
    :return:
    """
    print('got', the_list)
    the_list.append('four')
    print('changed_to', the_list)


outer_list = ['one', 'two', 'three']
print('before, outer_list= ', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list= ', outer_list)

print('='*60)


def try_to_change_list_reference(the_list):
    """
    改变引用
    :param the_list:
    :return:
    """
    print('reference>>> ', id(the_list))
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)
    print('reference>>> ', id(the_list))


outer_list = ['we', 'like', 'proper', 'English']
print('outer>>> ', id(outer_list))
print('before, outer_list= ', outer_list)
try_to_change_list_reference(outer_list)
print('outer_list>>> ', id(outer_list))
print('after, outer_list= ', outer_list)


print('='*60)


def try_to_change_string_reference(the_string):
    print('got', the_string)
    the_string = 'In a kingdom by the sea'
    print('set to', the_string)


outer_string = 'It was many and many a year ago'
print('before, outer_string= ', outer_string)
try_to_change_string_reference(outer_string)
print('after, outer_string= ', outer_string)