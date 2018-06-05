# 偏函数

import functools

'''
简单总结 functools.partial 的作用就是，把一个函数的某些参数
给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数
会更简单

当函数的参数个数太多，需要简化时，使用 functools.partial 可以创建
一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用
时更简单。
'''

max2 = functools.partial(max, 10)

print(max2(5, 6, 7))
