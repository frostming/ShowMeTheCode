#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0008 题：一个HTML文件，找出里面的正文。
# 第 0009 题：一个HTML文件，找出里面的链接。
# @Author: Frost Ming
# @Email: mianghong@gmail.com
# @Date: 2016/3/6


from bs4 import BeautifulSoup

def find_the_content(path):
    with open(path) as f:
        text = BeautifulSoup(f, 'lxml')
        content = text.get_text().strip('\n')

        return content#.encode('gbk','ignore')

def find_links(path):
    with open(path) as f:
        soup = BeautifulSoup(f, 'lxml')
        link_list = soup.find_all('a')

    return [item['href'] for item in link_list]

if __name__ == '__main__':
    print find_the_content('test.html')
    print '\n'.join(find_links('test.html'))