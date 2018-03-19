# -*- coding:utf-8 -*-
import datetime

import pyperclip
from PIL import Image
import matplotlib.pyplot as plt
import time

import HandlePic
import JudgePic
import Simple

try:
    from common import debug, config, screenshot
except Exception as ex:
    print(ex)
    print('请将脚本放在项目根目录中运行')
    print('请检查项目根目录中的 common 文件夹是否存在')
    exit(-1)


def yes_or_no(prompt, true_value='y', false_value='n', default=True):
    """
    检查是否已经为启动程序做好了准备
    """
    default_value = true_value if default else false_value
    prompt = '{} {}/{} [{}]: '.format(prompt, true_value,
                                      false_value, default_value)
    i = input(prompt)
    if not i:
        return default
    while True:
        if i == true_value:
            return True
        elif i == false_value:
            return False


def Start():
    screenshot.check_screenshot()


def MyPy():
    number = 1
    while True:
        s = '%05d' % number
        ticks = time.time()
        screenshot.pull_screenshot()
        img = Image.open('./Handle/screenShot.png')
        plt.figure("picture")
        plt.imshow(img)
        # plt.show()
        path = str('./screenshot/') + str(s) + str('.png')
        number = number + 1
        img.save(path)

        flag = JudgePic.main(path, s)

        if flag:
            HandlePic.HandlePic()
            key = Simple.Simple()
            index = '.'
            aa = key.find(index)
            words = key[aa+1:]
            pyperclip.copy(words)
            print(key)
            time.sleep(15)
            continue
        else:
            continue

        ticks1 = time.time()
        print(ticks1 - ticks)



def aaaaa():
    key = '11.ghfdfhfdgshfgh'
    index = '.'
    aa = key.find(index)
    words = key[aa+1:]
    print(words)

if __name__ == '__main__':
    aaaaa()
