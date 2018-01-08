
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

f = fib  # 函数赋值給变量
print(f(100))


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


f300 = fib2(300)  # 有返回值
print(f300)


# 7.深入Python函数定义
'''def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)
'''

# ask_ok('h')

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


def f1(a, L=[]):
    L.append(a)
    return L


print(f1(1))  # [1]
print(f1(2))  # [1, 2]
print(f1(3))  # [1, 2, 3]


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))  # [1]
print(f2(2))  # [1, 2]
print(f2(3))  # [1, 2, 3]


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("--This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("--Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='V00000M')
parrot(action='V00000M', voltage=1000000)
parrot('a million', 'better of life', 'jump')
parrot('a thousand', state='pushing up the daisies')


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-"*40)

    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))


def parrot2(voltage, state='a stiff', action='voom'):
    print("--This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


def make_incrementor(n):
    return lambda x: x+n


f = make_incrementor(42)
print(f(0))
print(f(1))


def my_function():
    """
    Do nothing, but document it.
    No, really, it doesn't do anything.
    :return:
    """
    pass


print(my_function.__doc__)
