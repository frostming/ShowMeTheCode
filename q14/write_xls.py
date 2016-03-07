#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容
# @Author: Frost Ming
# @Email: mianghong@gmail.com
# @Date: 2016/3/7

# Requires tablib module
import tablib
import json


def convert_xls(path):
    content = json.loads(open('student.txt').read())
    table = tablib.Dataset()
    for item, value in content.iteritems():
        table.append([item] + value)
    with open('student.xls', 'wb') as fp:
        fp.write(table.xls)


if __name__ == '__main__':
    convert_xls('student.txt')
