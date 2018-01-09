"""def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        smaller = []
        bigger = []
        for i in array[1:]:
            if i >= pivot:
                bigger.append(i)
            else:
                smaller.append(i)
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)
"""


def quick_sort(array):
    """
    快速排序算法
    :param array:
    :return:
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<=pivot]
        greater = [i for i in array[1:] if i>pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


data0 = [2, 1, 5, 3, 7, 6]
print(quick_sort(data0))
data1 = [5]
print(quick_sort(data1))
data2 = []
print(quick_sort(data2))
