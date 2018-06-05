# 列表和数组

students = ['lilei', 'haimeimei', 'poly']
print(len(students))
for item in students:
    print(item)
# 另类取元素方式--取倒数第几个元素
print(students[-1])
# 列表操作
students.append('xiaoming')
print(students[-1])
# 插入
students.insert(2, 'xiaohong')
print(students)
# 删除
students.pop()
print(students)
students.pop(2)
print(students)
# 赋值
students[1] = 'Sarah'
print(students)
# tuple --元组；tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改
students = ('lilei', 'haimeimei', [1, 2, 3])
print(students)
students[2].append(4)
print(students)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0], L[1][1], L[2][2])
