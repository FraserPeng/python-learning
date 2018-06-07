#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import namedtuple, deque,defaultdict

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

# namedtuple('名称', [属性 list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 1, 5)

# -------------------------------------------------
'''
使用 list 存储数据时，按索引访问元素很快，但是插入和删除元素就很
慢了，因为 list 是线性存储，数据量大的时候，插入和删除效率很低。
deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q.popleft()
if __name__ == '__main__':
    print(q)
