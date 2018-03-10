#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-10 下午3:17
# @site  : https://github.com/SunmoonSan


class Test(object):
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


if __name__ == '__main__':
    print(Test.num_of_instance)
    t1 = Test('jack')
    print(Test.num_of_instance)
    t2 = Test('lucy')
    print(t1.name, t1.num_of_instance)
    print(t2.name, t2.num_of_instance)


class Person:
    name = "aaa"


p1 = Person()
p2 = Person()
p1.name = 'bbb'
print(p1.name)
print(p2.name)
print(Person.name)


class Person1:
    name = []


p3 = Person1()
p4 = Person1()
p3.name.append(1)
print(p3.name)
print(p4.name)
print(Person1.name)
