
from collections import deque

graph = {
    'you': ['Bob', 'Alice', 'Claire'],
    'Bob': ['Anuj', 'Peggy'],
    'Alice': ['Peggy'],
    'Claire': ['Thom', 'Jonny'],
    'Anuj': [],
    'Peggy': [],
    'Thom': [],
    'Jonny': []
}


def is_seller(name):
    """
    如name以‘m’结尾，则返回True, 否则返回False
    :param name:
    :return:
    """
    return name[-1] == 'm'


def search(name):
    """
    图查找算法
    :param name:
    :return:
    """
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_seller(person):
                print(person, " is mango seller !")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search('you')