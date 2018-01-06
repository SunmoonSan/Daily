import re

#  删除字符串中不需要的字符
s = '  hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

s = '   Hello    world \n'
print(s.strip())


# 如果你想处理中间的空格，那么你需要求助其他技术。
# 比如使用 replace() 方法或者是用正则表达式替换。

print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))

# with open('../../multi.txt') as f:
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(lines)


