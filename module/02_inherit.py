#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类继承  多业态


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
'''
静态语言 vs  动态语言
对于静态语言（例如 Java）来说，如果需要传入 Animal 类型，则传入的
对象必须是 Animal 类型或者它的子类，否则，将无法调用 run() 方法。
对于 Python 这样的动态语言来说，则不一定需要传入 Animal 类型。我
们只需要保证传入的对象有一个 run() 方法就可以了：
class Timer(object):
def run(self):
print('Start...')
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象
只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
Python 的“file-like object“就是一种鸭子类型。对真正的文件对象，它有
一个 read() 方法，返回其内容。但是，许多对象，只要有 read() 方法，
都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
你不一定要传入真正的文件对象，完全可以传入任何实现了 read() 方法
的对象。
'''
