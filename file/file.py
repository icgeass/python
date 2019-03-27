#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import datetime
import decimal
import os
import shutil
import tempfile
import urllib2
from os import path


def test_other():
    # 时间格式化
    print('now: %s' % datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))

    # 执行命令
    print('nc cmd: %s' % os.system('nc -vz -w 1 127.0.0.1 22'))

    # 创建临时目录
    # os.makedirs可以创建多级目录，需要判断是否存在
    tmp_dir = tempfile.mkdtemp('', 'tmp_', path.dirname(__file__))

    # 目标目录是否存在
    print('tmp_dir: %s, exists: %s' % (tmp_dir, os.path.exists(tmp_dir)))

    # 执行ll命令
    print('os.popen: %s' % os.popen('ls -alFR .').read())

    shutil.copy('/etc/bash.bashrc', path.dirname(__file__) + '/bash.bashrc.copy')

    # 删除文件夹
    shutil.rmtree(tmp_dir)

    # 下载文件并用base64编码
    # http://tools.knowledgewalls.com/onlinebase64stringtoimageconverter
    print base64.b64encode(urllib2.urlopen('https://www.baidu.com/img/bd_logo1.png').read())


if __name__ == '__main__':
    test_other()
