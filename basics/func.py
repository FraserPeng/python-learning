'''
# 函数
# 函数定义、注解、说明
# 参数定义、注解
# 默认参数
# 可变参数
# 关键字参数
# 命名关键字参数
'''
import math


def circle_l(r: float, ndigits: '保留小数位' = 2) -> dict(type=float, help='圆周长'):
    '''
    计算圆周长
    '''
    if not isinstance(r, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(ndigits, (int)):
        raise TypeError('ndigits 必须是整数')
    s = math.pi * r * 2
    return round(s, ndigits)


def circle_s(r: dict(type= float, help= '半径'),
             ndigits: dict(type=int, help="保留小数位") = 2)\
        -> dict(type=float, help='圆面积'):
    '''
    计算圆的面积
    '''
    if not isinstance(r, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(ndigits, (int)):
        raise TypeError('ndigits 必须是整数')
    s = math.pi * pow(r, 2)
    return round(s, ndigits)


def quadratic(a: int, b: int, c: int):
    '''
    一元二次方程求解 ax²+bx+c=0
    '''
    if a == 0:
        raise TypeError('a≠0')
    m = pow(b, 2) - 4 * a * c
    if m < 0:
        raise TypeError('前置条件：b²-4ac>=0')
    x1 = ((b + math.sqrt(m)) / (2 * a)) * -1
    x2 = (-1 * b + math.sqrt(m)) / (2 * a)
    return round(x1, 2), round(x2, 2)


def calc(*ns):
    '''
    可变参数
    '''
    sum = 0
    for n in ns:
        sum += n
    return sum


nums = [1, 2, 3, 4, 5, 6]
print(calc(*nums))


def person(name, age, **kw):
    '''
    关键字参数写法
    '''
    print('name:', name, 'age:', age, "other:", kw)


person('fraser', '32', city='sz', job='vk')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('fraser', '32', **extra)


def personInfo(name, age, *, city='深圳', job):
    '''
    命名关键字参数,不能像关键字参数那样简便写法
    '''
    print('name:', name, 'age:', age, "city:", city, 'job：', job)


personInfo('fraser', '32', job='project')

'''
在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键
字参数和命名关键字参数，这 5 种参数都可以组合使用，除了可变参数
无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必
选参数、默认参数、可变参数/命名关键字参数和关键字参数。
'''