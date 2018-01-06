text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))  # 返回查到的字符串第一个字符的索引

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
if re.match('\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match('\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

m = datepat.match('11/27/2012')
print(m)
print(m.group(0))
print(m.groups())
print(text)

