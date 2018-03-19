# -*- coding:utf-8 -*-
from PIL import Image


def main(path,s):
    im = Image.open(path)
    flagOne = False
    flagTwo = False
    flagThree = False
    im_pixel = im.load()
    flag_pixel = im_pixel[80, 170] #200
    for i in range(80, 900, 50):
        pixel = im_pixel[i, 170]
        if pixel != flag_pixel:
            flagOne = True
            break
        if i >= 850:
            flagOne = False

    flag_pixel = im_pixel[80, 200]
    for i in range(80, 900, 50):
        pixel = im_pixel[i, 200]
        if pixel != flag_pixel:
            flagTwo = True
            break
        if i >= 850:
            flagTwo = False

    flag_pixel = im_pixel[80, 300]  # 200
    for i in range(80, 900, 50):
        pixel = im_pixel[i, 300]
        if pixel != flag_pixel:
            flagThree = False
            break
        if i >= 850:
            flagThree = True

    if flagTwo and flagOne and flagThree:
        print("yes")
        return True
    else:
        print("no"+str(s))
        return False



if __name__ == '__main__':
    im = Image.open('./screenshot/00087.png')
    # im = Image.open('./screenshot/00001.png')
    # im = Image.open('./screenshot/00012.png')
    main(im)
