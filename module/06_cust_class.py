# 定制类
'''
__slots__
__len__
__str__:返回用户看到的字符串
__repr__:返回程序开发者看到的字符串，也就是说， __repr__() 是为调试服务的。
__iter__:
__getitem__
__setitem__
__delitem__


__getattr__
__call__
'''


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器 a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值
    # 要表现得像 list 那样按照下标取出元素，需要实现 __getitem__() 方法：

    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n, int):  # n是索引
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片

            start = n.start
            stop = n.stop
            step = n.step
            signStep = 0
            if start is None:
                start = 0
            if step is None:
                step = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    if step != 0:
                        if signStep == 0:
                            L.append(a)
                            signStep += 1
                        elif step != signStep:
                            signStep += 1
                        else:
                            signStep = 0
                    else:
                        L.append(a)
                a, b = b, a + b
            return L


fn = Fib()
print(fn[2:12:0])
'''
总之，通过上面的方法，我们自己定义的类表现得和 Python 自带的 list、
tuple、dict 没什么区别，这完全归功于动态语言的“鸭子类型”，不需要
强制继承某个接口。

'''


class Chain(object):
    '''
    链式调用
    '''

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr__ = __str__


print(Chain("as").status.user.timeline.list)


class Student(object):
    '''
    任何类，只需要定义一个 __call__() 方法，就可以直接对实例进行调用
    '''

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()  # self 参数不要传入

print(callable(max))
print(callable(Student("")))
