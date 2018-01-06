"""
检查字符串开头或结尾的一个简单方法是使用 str.startswith()
 或者是 str.endswith()
"""

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file.'))
url = 'http://www.python.org'
print(url.startswith('http:'))

'''
如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去， 
然后传给 startswith() 或者 endswith() 方法：
'''

import os

filenames = os.listdir('../..')
print(filenames)
print([name for name in filenames if name.endswith(('.txt', '.py'))])

print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# 奇怪的是，这个方法中必须要输入一个元组作为参数。
# 如果你恰巧有一个 list 或者 set 类型的选择项，
# 要确保传递参数前先调用 tuple() 将其转换为元组类型。比如：


choices = ['http', 'https', 'ftp']
url = 'http://www.python.org'
# print(url.startswith(choices))
print(url.startswith(tuple(choices)))


# 切片实现匹配
filename = 'spam.txt'
print(filename[-4:] == '.txt')
print(url[:5] == 'http:' or url[:6] == 'https' or url[:4] == 'ftp:')  # 很不科学， 不提倡


# 正则表达式匹配
import re
print(re.match('http:|https:|ftp:', url))


