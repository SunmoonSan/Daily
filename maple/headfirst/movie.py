
movies = [
    "The Holy Grail",
    1975,
    "Terry Jones & Terry Gilliam",
    91,
    ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]
]

"""
def print_lol(array, indent=False, level=0):
    
    for each_item in array:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                print("\t" * level, each_item)
            else:
                print(each_item)

"""

def print_lol(array, indent=False, level=0):
    """
    将列表中的每个数据都递归打印出来
    :param array: 列表数据
    :param indent: True：缩进， False：不缩进，默认False
    :param level: 缩进的格数
    :return: 无返回值
    """
    for each_item in array:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                print("\t" * level, end='')
            print(each_item)


print_lol(movies) # 不缩进
print('----------------------------')
print_lol(movies, True) # 首行默认不缩进， 其余一次缩进
print('----------------------------')
print_lol(movies, True, 4) # 首行默认缩进4Tab键， 其余默认加1Tab键