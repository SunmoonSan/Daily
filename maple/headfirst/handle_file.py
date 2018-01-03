data = open('sketch.txt', 'r')
print(data.readline(), end='')
print(data.readline(), end='')

print(data.seek(0))  # 返回到第0个字符
print(data.readline(), end='')

for each_line in data:
    if not each_line.find(':') == -1:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end=' ')
        print("said: ", end=' ')
        print(line_spoken, end='')


data.close()
