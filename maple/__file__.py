
file = open('沁园春.txt','a')

flag = True
while flag:
    ch = input("请输入(退出请输入'q')： ")
    if ch != 'q':
        file.writelines(ch)
    else:
        flag = False

qyc = open('沁园春.txt', 'r')
data = qyc.read()
l = data.split('。')
for i in l:
    print(i)

file.close() # 关闭文件
