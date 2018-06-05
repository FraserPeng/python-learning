# 字典表查询

dist = {'lilei': 98, 'haimeimei': 80, 'xiaoheng': 97}

print(dist['lilei'])

print('xiaoheng' in dist)
# 根据key取值，如不存在，显示默认值
print(dist.get('hanmeimei', 60))

'''
和 list 比较，dict 有以下几个特点：
1. 查找和插入的速度极快，不会随着 key 的增加而增加；
2. 需要占用大量的内存，内存浪费多。
而 list 相反：
1. 查找和插入的时间随着元素的增加而增加；
2. 占用空间小，浪费内存很少。
所以，dict 是用空间来换取时间的一种方法。
'''
# 交集并集的实现
s = set([1, 2, 6, 5])
s1 = set([2, 3, 4, 7])
print(s & s1)
print(s | s1)
