# 怎样从一个集合中获得最大或者最小的 N 个元素列表？
# heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
nums.sort()  # 正排序
print(nums)
print(heapq.nlargest(3, nums))  # 最大3个数
print(heapq.nsmallest(4, nums))  # 最小4个数

print('-'*50)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 下面代码在对每个元素进行对比的时候，会以 price 的值进行比较。
cheap = heapq.nsmallest(3, portfolio, lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, lambda s: s['price'])
print(expensive)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
print(nums)
print(heap)
print('最大值， 最小值')
print(max(nums))  # 最大值
print(min(nums))  # 最小值

print('先排序，后切片')
print(sorted(nums)[:4])

print('堆排序')
heapq.heapify(heap)
print(heap)

print(heapq.heappop(heap))  # 弹出最小值
print(heapq.heappop(heap))  # 弹出第二小值
print(heapq.heappop(heap))  # 弹出第三小值

