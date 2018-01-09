
# 数据结构
a = [66.25, 333, 1, 1234.5]
print(a)
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
print(a)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
print(a.pop())

print('-'*60)

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

print("-"*60)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue.popleft())
print(queue)

print('-'*60)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**3 for x in range(10)]
print(squares)

s = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(s)

# 等价于

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
freshfruit = ['   banana', ' loganberry ', '  passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
print([(x, x**2) for x in range(6)])
# print([x, x**2 for x in range(6)])  错误实例
vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])

# 等价于
r = []
for elem in vec:
    for num in elem:
        r.append(num)

print(r)

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

# 嵌套的列表表达式
print([[row[i] for row in matrix] for i in range(4)])

# 等价于
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(list(zip(*matrix)))  # 十分费解

print('-'*60)

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a
# print(a)  a变量被删除了

print('-'*60)

t = 12345, 54321, 'hello！'
print(t[0])
print(t)
u = t, (1,2,3,4,5)
print(u)
# t[0] = 8888 元组不可篡改
v = ([1,2,3], [3,2,1])
print(v)

empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(singleton)

print('-'*60)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

# 列表表达式， 集合形式
s = {x for x in 'abracadabra' if x not in 'abc'}
print(s)


tel = {'jack':400, 'sape': 4139}
tel['guido'] = 4127

print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print('guido' in tel)
print('jack' not in tel)
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

s = {x: x**2 for x in (2,4,6)}
print(s)
print(dict(sape=4139, guido=4127, jack=4098))

# 字典遍历
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k, v)

for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions, answers):
    print('What is your {0} ? It is {1}.'.format(q,a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

words = ['cat', 'window', 'defenestrte']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print(words)


strings1, strings2, strings3 = '', 'Trondheim', 'Hammer Dance'
non_null = strings1 or strings2 or strings3
print(non_null)

print('-'*60)

print((1,2,3) < (1,2,4))
print([1,2,3] < [1,2,4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1,2,3,4) < (1,2,4))
print((1,2) < (1,2,-1))  # 不好理解
print((1,2,3) == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))  # 不好理解
