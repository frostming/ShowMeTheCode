#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
# @Author: Frost Ming
# @Email: mianghong@gmail.com
# @Date: 2016/3/6

import os

result = [0, 0, 0]


def get_files(path):
    for fp in os.listdir(path):
        fullpath = os.path.join(path, fp)
        if os.path.isfile(fullpath):
            if fullpath.endswith('.py'):
                yield fullpath
        else:
            for file in get_files(fullpath):
                yield file


def do_statistics(file):
    fp = open(file, 'rb')
    global result
    for line in fp:
        if line.startswith('#'):
            result[2] += 1
        elif line == os.linesep:
            result[1] += 1
        else:
            result[0] += 1
    fp.close()


if __name__ == '__main__':
    files = get_files('E:/PythonScripts')
    for file in files:
        print file
        do_statistics(file)
    print """Code: %d lines
Blank: %d lines
Comments: %d lines""" % (result[0], result[1], result[2])
