# 类动态新增属性 方法


from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'hello', 'get_hello')  # 用 tuple 定义允许绑定的属性名称
    pass


def hello(self, name):
    print("Hello %s" % name)


s = Student()
s.name = "fraser"
s.age = 32
s.hello = MethodType(hello, s)
Student.get_hello = MethodType(hello, Student)

# s.hello("fraser")

# s.get_hello("vanke")


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 50
