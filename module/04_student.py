# 类操作 使用@property


class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(99)
print(s.get_score())
# s.set_score(101)
# print(s.get_score())
# -----------------------------------------


class Students(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def age(self):
        return 2015


s = Students()
s.score = 60  # OK，实际转化为 s.set_score(60)
print(s.score)  # OK，实际转化为 s.get_score()
s.score = 999


'''
注意到这个神奇的 @property ，我们在对实例属性操作的时候，就知道该
属性很可能不是直接暴露的，而是通过 getter 和 setter 方法来实现的。
还可以定义只读属性，只定义 getter 方法，不定义 setter 方法就是一个
只读属性：
'''
