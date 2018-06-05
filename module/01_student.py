#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类操作，公有 私有


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            print("A")
        elif self.__score >= 60:
            print("B")
        else:
            print("C")

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


s = Student("fraser", 90)
s.print_score()
s.get_grade()
print(s.get_name())
# print(s._Student__name)

# --------------------------
# 类属性和实例属性


class Person(object):
    name = "Fraser"


p = Person()
print(p.name)  # 打印 name 属性，因为实例并没有 name 属性，所以会继续查找 class 的 name 属性
print(Person.name)  # 打印类的 name 属性
p.name = "Hello world"  # 给实例绑定 name 属性
print(p.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name 属性
print(Person.name)  # 但是类属性并未消失，用 Student.name 仍然可以访问
del p.name  # 如果删除实例的 name 属性
print(p.name)  # 再次调用 s.name，由于实例的 name 属性没有找到，类的name 属性就显示出来了
