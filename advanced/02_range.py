# 列表生成器
import os  # 导入 os 模块，

print(list(range(1, 11)))

L = [x * x for x in range(1, 11)]
print(L)

L1 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L1)

L2 = [m + n for m in 'ABC' for n in 'XYZ']
print(L2)

L3 = [m + n + z for m in 'ABC' for n in 'XYZ' for z in '123']
print(L3)

f = [d for d in os.listdir('.')]
print(f)

d = {'name': 'fraser', 'age': 30, 'job': 'engineer'}

for x, y in d.items():
    print(x, '=', y)

L = ['Hello', 'World', 18, 'Apple', None]

r = [s.lower() for s in L if isinstance(s, str)]

print(r)
