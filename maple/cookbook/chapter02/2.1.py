
"""
string 对象的 split() 方法只适应于非常简单的字符串分割情形，
它并不允许有多个分隔符或者是分隔符周围不确定的空格。
当你需要更加灵活的切割字符串的时候，最好使用 re.split() 方法：
"""

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
result = re.split(r'[;,\s]\s*', line)  #
print(result)
print('*'*50)
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
print(values)
delimiters = fields[1::2] + ['']
print(delimiters)
print(''.join(v+d for v,d in zip(values, delimiters)))


'''
如果你不想保留分割字符串到结果列表中去，
但仍然需要使用到括号来分组正则表达式的话，
确保你的分组是非捕获分组，形如 (?:...) 。比如：
'''
print(re.split(r'(?:,|;|\s)\s*', line))
