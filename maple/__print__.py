
data = []
file = open('multi.txt', 'w')
st = ''

file.writelines('打印三角形')
# 打印三角形， Java,C++,C, Python是最简单的
for i in range(10):
    print('*' * i)
    file.writelines('*' * i)
    file.writelines('\n')

file.writelines('\n')
file.writelines('#' * 110)
file.writelines('\n\n')

file.writelines('打印乘法表\n')
for i in range(1, 10):
    for j in range(1, i+1):
        st = "{j} * {i} = {s}\t".format(j=j, i=i, s=i*j)
        file.writelines(st)
        print(st, end='')
    print('\n')
    file.writelines('\n')



