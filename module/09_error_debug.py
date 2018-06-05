# 异常处理
# raise 抛出错误
# logging 错误日志记录

import logging
logging.basicConfig(level=logging.INFO)


def foo():
    try:
        print("try...")
        r = 10 / 0
        print("result....")
    except ZeroDivisionError as e:
        print("except:", e)
        raise ZeroDivisionError("这是一个错误")
    finally:
        print("finally...")
    print("END")


def main():
    try:
        foo()
    except Exception as e:
        print("Exception:", e)


# main()
# --------------------------------------

# 调试
# print()
# 断言  assert
# logging
# pdb
# n 单步执行
# p 查看变量
# q 退出

# pdb.set_trace() 


def foos(s):
    n = int(s)
    assert n != 0, 'n is zero'
    logging.info('n = %d' % n)
    return 10 / n


def mains():
    foos('1')


mains()
