# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

from PIL import Image, ImageDraw, ImageFilter, ImageFont

import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1
def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def rndColor2():
    return (random.randint(32,127), random.randint(32, 127), random.randint(32, 127))

# 像素240x60
width = 60 * 4
height = 60
image =Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('C:/windows/Fonts/Arial.ttf', 36)  # 此处需提供字体文件绝对位置
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor1())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')  # 生成的验证码文件保存在与.py相同文件夹下