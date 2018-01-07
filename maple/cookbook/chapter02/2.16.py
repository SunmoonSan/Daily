
"""
你有一些长字符串，想以指定的列宽将它们重新格式化。
使用 textwrap 模块来格式化字符串的输出。
"""

import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))
print(textwrap.fill(s, 40, initial_indent='  ', subsequent_indent='    '))


print('-'*50)

# import os

# print(os.get_terminal_size())

