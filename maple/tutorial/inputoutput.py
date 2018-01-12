# 输入和输出

s = 'Hello, world.'
print(str(s))
print(repr(s))
print(str(1 / 7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
print(repr((x, y, ('spam', 'eggs'))))

print('-' * 60)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x ** 2).rjust(3), end=' ')
    print(repr(x ** 3).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x ** 2, x ** 3))

print('-' * 60)

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print('-' * 60)

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
    food='spam', adjective='adsolutely horrible'
))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

print('-' * 60)

# '!a' (应用 ascii())，'!s' （应用 str() ）和 '!r' （应用 repr() ）可以在格式化之前转换值:

import math

print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack':4098, 'Dcab':7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

# print('Jack:{0[Jack]:d};Sjoerd:{0[Sjoerd]:d};')

print('The value of PI is approximately %5.3f.' % math.pi)