# json 序列化

import json

d = dict(name="Faser", age=32, score=100)

print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(json.loads(json_str))

# ------------------------- 高阶


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 78)
#  class 对象不是一个可序列化为 JSON 的对象。

'''
因为通常 class 的实例都有一个 __dict__ 属性，它就是一个 dict ，用来
存储实例变量。也有少数例外，比如定义了 __slots__ 的 class。
'''
print(json.dumps(s, default=lambda obj: obj.__dict__))
