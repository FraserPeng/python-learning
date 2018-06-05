# 切片
# list 切片
# tuple 也是一种特殊的list 可以切片
# 字符串 也可以看成list 切片

L = [10, 12, 11, 14, 17, 8]
print(L[0:3])
print(L[:3])
print(L[2:3])
print(L[-3:-1])
print(L[-3:])
print(L[:-3])

numbers = list(range(100))

print(numbers[:10])
print(numbers[-10:])
print(numbers[10: 20])
# 前 10 个数，每两个取一个
print(numbers[:10:2])
# 所有数，每 5 个取一个
print(numbers[::5])
# 倒序
print(numbers[::-1])
