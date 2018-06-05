#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ASCII 编码 1个字节
# Unicode  编码 2个字节
# UTF-8 编码 可变长字节
# python3.x中 字符串是以Unicode编码的，也就是说，python 字符串支持多语言

print("我开始学习python啦")

# ord()--获取字符才整数表示
print(ord('中'))
# chr()--编码转成对应的字符
print(chr(65))
# encode 字符串转化成字节
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# decode 字节转成字符串
print('ABC'.encode('ascii').decode('ascii'))
print('中文'.encode('utf-8').decode('utf-8'))

# 由于 Python 源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为 UTF-8 编码
# Python 解释器读取源代码时，为了让它按 UTF-8 编码读取，我们通常  在文件开头写上这两行：见文件头部
