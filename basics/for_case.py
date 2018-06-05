# 循环 for  while

sum = 0
for item in list(range(101)):
    sum += item
print(sum)


# 列出 1-10000中的质数：只能被1和它本身整除的数
# 结果按二位数组层现，每行10个
# 可参照 advanced/filter中质数的求解方法
table = []
row = []
for n in list(range(2, 10001)):
    if n % 2 == 0 and n != 2:
        continue
    m = n - 1
    p = True

    while m > 1:
        r = n % m
        if r == 0:
            p = False
            break
        m -= 1
    if p:
        if len(row) == 10:
            table.append(row)
            row = []
            row.append('%05d' % n)
        else:
            row.append('%05d' % n)

table.append(row)
print(len(table))
for item in table:
    print(item)
