#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
# @Author: FrostMing
# @Email: mianghong@gmail.com
# @Date: 2016/3/6


from PIL import Image, ImageDraw, ImageFont


def add_num(img, num):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', width / 4)
    color = '#ff0000'
    draw.text((width - width / 4, 0), num, font=font, fill=color)
    img.save('result.jpg', 'jpeg')


if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image, '99')
