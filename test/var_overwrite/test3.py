#! /usr/bin/env python
# -*- coding: utf-8 -*-

# test_var使用最后一次导入
from test2 import *
from test1 import *


def fun3():
    global test_var
    print test_var


# 引用外部文件（模块）的变量如果重名，使用最后一次导入的为准
if __name__ == '__main__':
    fun1()
    fun2()
    fun3()
