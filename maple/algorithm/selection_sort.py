
# 选择出该数组的最小值, 并返回最小值的索引


def find_smallest(array):
    smallest = array[0]
    index = 0
    for i in range(1, len(array)):
        if smallest > array[i]:
            smallest = array[i]
            index = i
    return index


def selection_sort(array):
    sorted_array = []
    # n = len(array)
    # for i in range(n):
    for i in range(len(array)): # len(array)的值循环一次减1， 总觉得这样不合适, 用上面两行较好理解
        print(array)
        smallest_index = find_smallest(array) # smallest_index用来记录第一次遍历后找到的最小值索引
        sorted_array.append(array[smallest_index]) # 将本次查找到的最小值记录到一个新的列表sorted_array中
        array.pop(smallest_index) # 弹出本次找到的最小值，然后进行下一次查找
    return sorted_array


data = [7, 5, 0, 9, 1, 6, 5, 8]
print(selection_sort(data))