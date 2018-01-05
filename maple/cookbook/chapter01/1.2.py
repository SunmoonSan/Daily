
# 值得注意的是上面解压出的 phone_numbers 变量永远都是列表类型，不管解压的电话号码数量是多少（包括 0 个）
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

print('*'*50)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

print('*'*50)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


print('*'*50)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

print('*'*50)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

print('*'*50)
items = [1, 10, 7, 4, 5, 9]
head, *tail = items

print(head)
print(tail)

print('*'*50)


# 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法
def sum(items):
    h, *t = items
    return h + sum(t) if t else h


print(sum(items))