# 生成器
'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含 100 万个元素的列表，不
仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的 list，从
而节省大量的空间。在 Python 中，这种一边循环一边计算的机制，称为生成器：generator
'''
# 要创建一个 generator，有很多种方法。第一种方法很简单，只要把一个
# 列表生成式的 [] 改成 () ，就创建了一个 generator：
'''
generator 保存的是算法，每次调用 next(g) ，就计算出 g 的
下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出
StopIteration 的错误

'''
g = (x * x for x in range(10))

# 错误打印方式
print(g)
for n in g:
    print(n)
# print(next(g))

# 如果推算的算法比较复杂，用类似列表生成式的 for
# 循环无法实现的时候，还可以用函数来实现
'''
著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任
意一个数都可由前两个数相加得到：
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
'''


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):
    print(n)

'''
但是用 for 循环调用 generator 时，发现拿不到 generator 的 return 语句
的返回值。如果想要拿到返回值，必须捕获 StopIteration 错误，返回值
包含在 StopIteration 的 value 中：
'''
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
