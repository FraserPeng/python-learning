# 返回函数


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lazy_sum(*L)
print(f())
'''
在这个例子中，我们在函数 lazy_sum 中又定义了函数 sum ，并且，内部
函数 sum 可以引用外部函数 lazy_sum 的参数和局部变量，当 lazy_sum 返
回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为“闭包
（Closure）”的程序结构拥有极大的威力
'''


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


fs = count()
for fn in fs:
    print(fn())


def count1():
    fs = []

    def f(j):
        def g():
            return j * j
        return g
    for n in range(1, 4):
        fs.append(f(n))
    return fs


fs = count1()
for fn in fs:
    print(fn())
