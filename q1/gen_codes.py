#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# @Author: FrostMing
# @Email: mianghong@gmail.com
# @Date: 2016/3/6

import string
import random
import os

letters = string.letters + string.digits


def gen_codes(length):
    result = ''.join(random.sample(letters, length))
    return result


if __name__ == '__main__':
    result = open('result.txt', 'w')
    for i in range(200):
        result.write(gen_codes(8)+os.linesep)
    result.close()
