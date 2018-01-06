
# fnmatch模块提供了两个函数—fnmatch()和fnmatchcase()，可以用来实现这样的匹配。

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, '*.csv')])

# fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式。
print(fnmatch('foo.txt', '*.TXT'))  # Linux为False， Windows 为True
print(fnmatchcase('foo.txt', '*.TXT'))  # fnmatchcase不区分大小写


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

# 这两个函数通常会被忽略的一个特性是在处理非文件名的字符串时候它们也是很有用的。
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][]0-9] *CLARK*')])
