# 装饰器

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


now()

'''
把 @log 放到 now() 函数的定义处，相当于执行了语句：
now = log(now)
由于 log() 是一个 decorator，返回一个函数，所以，原来的 now() 函数仍
然存在，只是现在同名的 now 变量指向了新的函数，于是调用 now() 将
执行新函数，即在 log() 函数中返回的 wrapper() 函数。
'''


def logs(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(%s,%s):' % (text, func.__name__, args, kw))
            return func(*args, **kw)
        return wrapper
    return decorator


@logs("执行")
def nows():
    print('2015-3-25')


nows()
# 通过 wraps 改变函数名 wrapper nows
print(nows.__name__)


def t_logs(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin  %s call' % func.__name__)
            # print('decorator param :%s' % text)
            func(*args, **kw)
            print('end  %s call' % func.__name__)
        return wrapper
    return decorator


@t_logs()
def t_now():
    print('2015-3-25')


t_now()
print(t_now.__name__)
