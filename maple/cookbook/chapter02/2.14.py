
# 合并字符串

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

print('*'*50)

# 如果你仅仅只是合并少数几个字符串，使用加号(+)通常已经足够了：
a = 'Is Chicago'
b = 'Not Chicago?'
print(a+ ' ' +b)
print('{} {}'.format(a, b))

print('*'*50)

a = 'Hello' 'World'
print(a)

print('*'*50)
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

print('*'*50)
a = 'a'
b = 'b'
c = 'c'
print(a + ':' + b + ':' + c)  # Ugly
print(':'.join([a, b, c]))  # Still ugly
print(a, b, c, sep=':')  # Better

