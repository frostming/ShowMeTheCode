#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
# @Author: Frost Ming
# @Email: mianghong@gmail.com
# @Date: 2016/3/6

import re

def count_words(file):
    pattern = re.compile(r'\b[a-zA-Z\']+\b')
    target = open(file, 'r').read()
    res = pattern.findall(target)
    print res
    return len(res)

if __name__ == '__main__':
    file = 'test.txt'
    words_num = count_words(file)
    print 'The file "%s" contains %d words in total' %(file, words_num)