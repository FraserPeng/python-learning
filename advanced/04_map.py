# 高阶函数 map
from functools import reduce


def f(n):
    return lambda x: pow(x, n)


def add(x, y):
    return x + y


def add1(n):
    return lambda x, y: x + y + n


L = [1, 2, 4, 5, 6, 7, 8, 9]
m = map(f(3), L)
print(list(m))
print(list(map(str, L)))
print(reduce(add, L))
# 等同于上面
print(reduce(lambda x, y: x + y, L))
print(reduce(add1(2), L))


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
            '7': 7, '8': 8, '9': 9, '.': -1}[s]


r = reduce(fn, map(char2num, '13579'))
print(r)


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))


def str2int1(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int("231231"))


def str2float(s):
    '''
    字符串转float
    '''
    count = 0
    isPoint = False

    def fn(x, y):
        nonlocal count
        nonlocal isPoint
        if isPoint:
            count += 1
        if y == -1:
            isPoint = True
            return x
        if count > 0:
            return x + pow(0.1, count) * y
        else:
            return x * 10 + y
    return reduce(fn, map(char2num, s))


print(str2float("1231.21"))


def prod(L):
    '''
    list中元素乘积
    '''
    def fn(x, y):
        return x * y
    return reduce(fn, L)


print(prod([1, 2, 3]))
