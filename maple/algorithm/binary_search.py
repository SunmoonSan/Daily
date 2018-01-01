
# 二分查找算法(递归描述)

print('二分查找算法(递归描述)')


def binary_search1(low, high, data, item):
    if data[low] <= item <= data[high]:
        mid = int((low + high) / 2)
        if item == data[mid]:
            return mid
        elif item > data[mid]:
            return binary_search1(mid + 1, high, data, item)  # if-else 结构必须一致，都要有return
        else:
            return binary_search1(low, mid - 1, data, item)
    else:
        return None


my_list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binary_search1(0, len(my_list1)-1, my_list1, 17))

print('===================分割线=======================')


# 二分查找算法
print('二分查找算法')


def binary_search2(data, item):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if data[mid] == item:
            return mid
        elif data[mid] > item:
            high = mid -1
        else:
            low = mid + 1
    return None


my_list2 = [1, 3, 5, 7, 9]
print(binary_search2(my_list2, 7))

