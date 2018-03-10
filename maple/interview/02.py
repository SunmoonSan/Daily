#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-3-10 下午9:30
# @site  : https://github.com/SunmoonSan


class ObjectCreator(object):
    pass


print(ObjectCreator)


def echo(o):
    print(o)


echo(ObjectCreator)
print(hasattr(ObjectCreator, 'new_attribute'))
ObjectCreator.new_attribute = 'foo'
print(hasattr(ObjectCreator, 'new_attribute'))
print(ObjectCreator.new_attribute)
ObjectCreatorMirror = ObjectCreator
print(ObjectCreatorMirror.new_attribute)
print(ObjectCreatorMirror())
print(ObjectCreator())

print('='*60)


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


MyClass = choose_class('foo')
print(MyClass)
print(MyClass())

print(type(1))
print(type('1'))
print(type(ObjectCreator))
print(type(ObjectCreator()))

print('='*60)

"""
class Foo(object):
    bar = True
"""

Foo = type('Foo', (), {'bar': True})
print(Foo)
print(Foo.bar)
f = Foo()
print(f)
print(f.bar)

print('='*60)
age = 25
print(age.__class__)
name = 'bob'
print(name.__class__)


def foo():
    pass


print(foo.__class__)


class Bar(object):
    pass


b = Bar()
print(b.__class__)

print(age.__class__.__class__)
print(name.__class__.__class__)
print(foo.__class__.__class__)
print(b.__class__.__class__)