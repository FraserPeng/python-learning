#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Test'
import sys


def __pri_test():
    print("私有函数")


def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()

'''
第 1 行和第 2 行是标准注释，第 1 行注释可以让这个 hello.py 文件直接
在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8
编码；
第 4 行是一个字符串，表示模块的文档注释，任何模块代码的第一个字
符串都被视为模块的文档注释；
第 6 行使用 __author__ 变量把作者写进去，这样当你公开源代码后别人
就可以瞻仰你的大名；
以上就是 Python 模块的标准文件模板，当然也可以全部删掉不写，但
是，按标准办事肯定没错。

后面开始就是真正的代码部分。
你可能注意到了，使用 sys 模块的第一步，就是导入该模块：
import sys
导入 sys 模块后，我们就有了变量 sys 指向该模块，利用 sys 这个变量，
就可以访问 sys 模块的所有功能。
sys 模块有一个 argv 变量，用 list 存储了命令行的所有参数。 argv 至少
有一个元素，因为第一个参数永远是该.py 文件的名称，例如：
运行 python3 hello.py 获得的 sys.argv 就是 ['hello.py'] ；
运行 python3 hello.py Michael 获得的 sys.argv 就是 ['hello.py',
'Michael] 。
最后，注意到这两行代码：
if __name__=='__main__':
test()
当我们在命令行运行 hello 模块文件时，Python 解释器把一个特殊变量
__name__ 置为 __main__ ，而如果在其他地方导入该 hello 模块时， if 判断
将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一
些额外的代码，最常见的就是运行测试。
我们可以用命令行运行 hello.py 看看效果：
$ python3 hello.py
Hello, world!
$ python hello.py Michael
Hello, Michael!

如果启动 Python 交互环境，再导入 hello 模块：
$ python3
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello
>>>
导入时，没有打印 Hello, word! ，因为没有执行 test() 函数。
调用 hello.test() 时，才能打印出 Hello, word! ：
>>> hello.test()
Hello, world!
'''
