# 切片
# list 切片
# tuple 也是一种特殊的list 可以切片
# 字符串 也可以看成list 切片

import numpy as np

import sys

sys.setrecursionlimit(10000)  # 例如这里设置为一百万

# L = [10, 12, 11, 14, 17, 8]
# print(L[0:3])
# print(L[:3])
# print(L[2:3])
# print(L[-3:-1])
# print(L[-3:])
# print(L[:-3])

# numbers = list(range(100))

# print(numbers[:10])
# print(numbers[-10:])
# print(numbers[10: 20])
# # 前 10 个数，每两个取一个
# print(numbers[:10:2])
# # 所有数，每 5 个取一个
# print(numbers[::5])
# # 倒序
# print(numbers[::-1])
# print(numbers[::])

data = np.zeros((2, 2), dtype=object)


def divisor(n):
    '''
    求自然数的公约数，
    '''
    div = []
    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i)
    return div


def filter_data(k, num, divs):
    '''
    过滤不符合要求的数据
    k:矩阵边长，
    num:求公约数的自然数
    divs:公约数
    '''
    a = divs.copy()
    for i in divs:
        if i > k:
            if i in a:
                a.remove(i)
            if (num / i) in a:
                a.remove(num / i)
    return a


remain = 4
count = 0


def process(k, row, col):
    global remain, data, count
    if k == row + 1 and k == col + 1:
        # print(row, col, k)
        if np.sum(data == 0) == 0:
            print(data)
            print('------------------')
        data = np.zeros((k, k), dtype=object)
        remain = pow(k, 2)
        return
    if(not check(row, col)):
        return
    for n in range(2, pow(k, 2) + 1):
        # print("----1----%s" % n)
        print(count)
        count += 1
        if remain < n:
            return
        divs = divisor(n)
        max_num = k - min([row, col])
        usable_divs = filter_data(max_num, n, divs)
        for i, div in enumerate(usable_divs):

            # print("----2----%s--%s" % (usable_divs, i))
            if (row + usable_divs[i]) > k or (col + usable_divs[-1 - i]) > k:
                continue
            for row1 in range(row, row + usable_divs[i]):
                for col1 in range(col, col + usable_divs[-1 - i]):
                    data[row1][col1] = (row, col)
            data[row][col] = n
            remain = remain - n
            for r in range(k):
                for c in range(k):
                    if(r <= row and c <= col):
                        continue
                    print({"r": r, "c": c})
                    process(k, r, c)


def check(row, col):
    value = data[row, col]
    if isinstance(value, tuple):
        if row > value[0] or (row == value[0] and col > value[1]):
            return False
        else:
            return True
    else:
        return True


def main(k):
    process(k, 0, 0)


if __name__ == "__main__":
    main(2)
