# 1.编写一个递归形式的sum求和函数


def calculate_sum(array, i):
    """
    递归求和
    :param array: 带求和列表
    :param i: 索引
    :return: 求和结果
    """
    if len(array) != 0:
        if len(array) - 1 == i:
            return array[i]
        else:
            return array[i] + calculate_sum(array, i + 1)
    else:
        return 0


def calculate_sum2(array):
    if not array:
        return 0
    else:
        return array[0] + calculate_sum2(array[1:])


data = [0, 1, 2, 3, 4]
print(calculate_sum2(data))
data1 = []
print(calculate_sum2(data1))
data2 = [3]
print(calculate_sum2(data2))

print("---------------分割线---------------------")


def calculate_count(array):
    """
    递归计算数组元素的个数
    :param array:
    :return:
    """
    if not array:
        return 0;
    else:
        return 1 + calculate_count(array[1:])


data0 = []
print(calculate_count(data0))
data1 = [3]
print(calculate_count(data1))
data2 = [3, 4, 6]
print(calculate_count(data2))