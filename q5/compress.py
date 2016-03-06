#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# @Author: Frost Ming
# @Email: mianghong@gmail.com
# @Date: 2016/3/6 0006

import os
from PIL import Image

def compress(source, target, maxsize=1280):
    img = Image.open(source)
    w, h = img.size
    if max(w, h) <= maxsize:
        return None
    if w > h:
        ws = maxsize
        hs = h * maxsize / w
    else:
        hs = maxsize
        ws = w * maxsize / h
    out = img.resize((ws, hs))
    out.save(target)


if __name__ == '__main__':
    image_folder = 'Pictures'
    for image in os.listdir(image_folder):
        source = os.path.join(image_folder, image)
        path, ext = os.path.splitext(source)
        target = path +'_Compressed' + ext
        compress(source, target)