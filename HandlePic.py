# -*- coding:utf-8 -*-

# 40*160
# 440* 230
from PIL import Image


def HandlePic():
    im = Image.open('./Handle/screenShot.png')
    img_size = im.size
    # print("图片宽度和高度分别是{}".format(img_size))
    '''
    裁剪：传入一个元组作为参数
    元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
    '''
    # 截取图片中一块宽和高都是250的
    x = 80
    y = 350
    w = 840
    h = 140
    region = im.crop((x, y, x + w, y + h))
    region.save("./Handle/HandlePic.png")


if __name__ == '__main__':
    HandlePic()
