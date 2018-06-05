# 使用元类

'待完善.......'

'''
我们说 class 的定义是运行时动态创建的，而创建 class 的方法就是使用
type() 函数。
type() 函数既可以返回一个对象的类型，又可以创建出新的类型，比如，
我们可以通过 type() 函数创建出 Hello 类，而无需通过 class
'''
# Hello(objet)定义


def fn(self, name="world"):
    print("Hello,%s" % name)


#  class 名称
# 继承父类的集合，注意 Python 支持多重继承，如果只有一个父类，别忘了 tuple 的单元素写法
# class 的方法名称与函数绑定，这里我们把函数 fn 绑定到方法名hello 上。
Hello = type('Hello', (object,), dict(hello=fn))  # 创建 Hello class

h = Hello()
h.hello()
