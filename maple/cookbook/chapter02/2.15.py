
s = '{name} has {n} messages'
print(s.format(name='Guido', n=37))

print('-'*50)

# 如果要被替换的变量能在变量域中找到，
# 那么你可以结合使用 format_map() 和 vars()

name = 'Guido'
n = 37
print(s.format_map(vars()))  # 很奇怪的用法

print('-'*50)


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
print(s.format_map(vars(a)))