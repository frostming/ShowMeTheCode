#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# @Author: Frost Ming
# @Email: mianghong@gmail.com
# @Date: 2016/3/6

import re
import os


def get_files(path):
    for fp in os.listdir(path):
        fullpath = os.path.join(path, fp)
        if os.path.isfile(fullpath):
            yield fullpath
        else:
            yield get_files(fullpath)


def get_most_important_word(files):
    worddict = {}
    for file in files:
        with open(file, 'r') as fp:
            content = fp.read()
            words = re.findall(r'\b[a-zA-Z\']+\b', content)
            for word in words:
                worddict[word] = worddict.get(word, 0) + 1
    wordsort = sorted(worddict.items(), key=lambda e: e[1], reverse=True)
    return wordsort


if __name__ == '__main__':
    files = get_files('test')
    wordsort = get_most_important_word(files)
    # print wordsort
    for word in wordsort:
        if word[1] == wordsort[0][1]:
            print word[0]
