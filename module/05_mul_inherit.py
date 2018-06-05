# 多重继承

'''
在设计类的继承关系时，通常，主线都是单一继承下来的，例如， Ostrich
继承自 Bird 。但是，如果需要“混入”额外的功能，通过多重继承就可以
实现，比如，让 Ostrich 除了继承自 Bird 外，再同时继承 Runnable 。这
种设计通常称之为 MixIn
'''


class Animal(object):
    pass


class Mammal(Animal):  # 哺乳动物
    pass


class Bird(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print("Running")


class FlyableMixIn(object):
    def fly(self):
        print("Flying")


class Dog(Mammal, RunnableMixIn):  # 狗狗
    pass


class Bat(Mammal, FlyableMixIn):  # 蝙蝠
    pass


class Parrot(Bird, FlyableMixIn):  # 鹦鹉
    pass


class Ostrich(Bird, RunnableMixIn):  # 鸵鸟
    pass
