#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
# @Author: Frost Ming
# @Email: mianghong@gmail.com
# @Date: 2016/3/6

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
import string


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def rndChar():
    return chr(random.randint(65, 90))


def rndTilt():
    return random.randint(-30, 30)


def draw_image():
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    for t in range(4):
        draw.text((t * 60 + 10, 10), rndChar(), font=font, fill=rndColor2())
        tmp = image.crop((60*t, 0, 60+60*t, 60))
        tmp = tmp.rotate(rndTilt())
        image.paste(tmp, (60*t, 0, 60+60*t, 60))

    for x in range(width):
        for y in range(height):
            point = image.getpixel((x, y))
            if point == (0, 0, 0):
                draw.point((x, y), fill=rndColor())
    image = image.filter(ImageFilter.BLUR)
    image.save('captcha.jpg')


if __name__ == '__main__':
    draw_image()
