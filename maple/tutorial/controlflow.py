
# 1.if语句
"""x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
"""


# 2.for语句

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print(words)

# 3.range()函数

for i in range(5):
    print(i, end=' ')

print()

for i in range(5, 10):
    print(i, end=' ')

print()

for i in range(0, 10, 3):
    print(i, end=' ')

print()

for i in range(-10, -100, -30):
    print(i, end=' ')

print()

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print()

for n,i in enumerate(a):
    print(n, i)

print()

# 在不同方面 range() 函数返回的对象表现为它是一个列表，
# 但事实上它并不是。当你迭代它时，它是一个能够像期望的序列返回连续项的对象；
# 但为了节省空间，它并不真正构造列表。
print(range(10))  # range(0, 10)
r = range(10)
print(list(r))

# 4.break和continue语句
for n in range(2, 10):
    for x in range(2, n//2):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        print(n, '是素数')

print()

# C, Java语言形式实现
for n in range(2, 20):
    x = 2
    for x in range(2, n):
        if n % x == 0:
            break
    if x > n // 2:
        print(n)

for num in range(2, 10):
    if num % 2 == 0:
        print('偶数', num)
        continue
    print(num)


# 5.pass语句
class MyEmptyClass:
    pass


def initlog(*args):
    pass


# 6.定义函数
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print(fib(200))