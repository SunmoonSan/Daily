
# 任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多个变量。
# 唯一的前提就是变量的数量必须跟序列元素的数量是一样的。

p = (4, 5)
x, y = p

print(x)
print(y)

print('-'*50)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

print(name)
print(date)

name, shares, price, (year, mon, day) = data

print(name)
print(year)
print(mon)
print(day)

# 实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。
#  包括字符串，文件对象，迭代器和生成器。
print('-'*50)

s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(e)

print('-'*50)
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

print(shares)
print(price)