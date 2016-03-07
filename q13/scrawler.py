#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
# @Author: Frost Ming
# @Email: mianghong@gmail.com
# @Date: 2016/3/7

import requests
import os
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/4392017599'

def simple_spider():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'lxml')
    image_list = soup.find_all('img', class_='BDE_Image')
    if not os.path.isdir('Images'):
        os.mkdir('Images')
    for index, item in enumerate(image_list):
        img_url = item['src']
        ext = os.path.splitext(img_url)[1]
        img_req = requests.get(img_url)
        fp = open('Images/%d%s' % (index, ext), 'wb')
        fp.write(img_req.content)
        fp.close()

if __name__ == '__main__':
    simple_spider()