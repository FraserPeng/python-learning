# 过滤器 filter
# filter 返回的是一个Iterator 惰性序列，呈现出结果 需要使用list

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def fn(n):
    return n % 2 == 1


print(list(filter(fn, L)))
'''
质数 ；只能被1和它本身整除的自然数（除1外）
埃氏筛法
'''


def _odd_iter(m):
    '''
    生成奇数序列
    '''
    n = 1
    while n <= m:
        n += 2
        yield n


def _not_divisible(n):
    '''
    过滤序列
    '''
    return lambda x: x % n > 0


def primes(m):
    '''
    生成素数
    '''
    yield 2
    it = _odd_iter(m)  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印 10000 以内的素数:

table = []
row = []
for n in primes(100):
    if len(row) != 10:
        row.append('%05d' % n)
    else:
        table.append(row)
        row = []
        row.append('%05d' % n)
table.append(row)
for item in table:
    print(item)


'''
回数是指从左向右读和从右向左读都是一样的数，例如 12321 ， 909 。请
利用 filter() 滤掉非回数
'''


def natural_number(n):
    '''
    获取规定的 范围内自然数
    '''
    m = 1
    while m <= n:
        yield m
        m += 1


def is_huishu(n):
    '''
    判断是否是回数
    '''
    n_str = str(n)
    n_str = n_str[::-1]
    m = int(n_str)
    return m == n


def get_huishu(n):
    '''
    获取回数
    '''
    it = natural_number(n)
    while True:
        m = next(it)
        if m < 10:
            yield m
        else:
            p = is_huishu(m)
            if p:
                yield m


print(list(get_huishu(1000)))
