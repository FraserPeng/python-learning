# 排序问题

L = [36, 5, -12, 9, -21]

print(sorted(L))
print(sorted(L, key=lambda x: -1 * x))

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L, key=str.lower, reverse=True))

# 假设我们用一组 tuple 表示学生名字和成绩：
L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用 sorted() 对上述列表分别按名字排序：


def sort_by_name(obj):
    return obj[0].lower()


def sort_by_score(obj):
    return obj[1]


print(sorted(L, key=sort_by_name, reverse=True))
print(sorted(L, key=sort_by_score, reverse=True))
