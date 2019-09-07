#! /usr/bin/env python
# -*- coding: utf-8 -*-

from test1 import *

test_var = 'test2'


def fun2():
    global test_var
    print test_var


# def fun1():
#     print 111

# 全局变量和函数，优先使用本文件（模块）的，再使用外部的
if __name__ == '__main__':
    fun1()
    fun2()
