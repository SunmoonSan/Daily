
# 字符串对齐


text = 'Hello World'
print(text.ljust(20))
print(text.ljust(20, '-'))
print(text.rjust(20))
print(text.rjust(20, '-'))
print(text.center(20))
print(text.center(20, '-'))

print('-'*50)

# format实现对齐 <, >, ^
print(format(text, '>20'))  # 向右对齐
print(format(text, '->20'))
print(format(text, '<20'))  # 向左对齐
print(format(text, '-<20'))
print(format(text, '^20'))  # 居中对齐
print(format(text, '-^20'))

print('-'*50)

print('{:>10s} {:>10s}'.format('Hello', 'World'))
print('{:->10s} {:*>10s}'.format('Hello', 'World'))
print('{:-<10s} {:*<10s}'.format('Hello', 'World'))
print('{:-^10s} {:*^10s}'.format('Hello', 'World'))

print('-'*50)

x = 1.2345
print(format(x, '0>10'))
print(format(x, '0^10.2f'))  # 0填充10位，保留2位小数

print('-'*50)

# 旧式用法
print('%-20s' % text)
print('%20s' % text)


"""
在新版本代码中，你应该优先选择 format() 函数或者方法format()要比 % 操作符的功能更为强大。
并且 format() 也比使用 ljust() , rjust() 或 center() 方法更通用，
因为它可以用来格式化任意对象，而不仅仅是字符串。
"""

