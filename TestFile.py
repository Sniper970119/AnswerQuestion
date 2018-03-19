# -*-coding:utf-8 -*-
import time
from PIL import Image

import Simple
import MyPy
import pyperclip
import HandlePic


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
    # im = Image.open('./screenShot.png')
    HandlePic.HandlePic()
    key = Simple.Simple()
    pyperclip.copy(key)
    print(key)


if __name__ == '__main__':
    MyPy.Start()
    MyPy.MyPy()
    print(".")
    startTime = time.time()
    print(".")
    Start()
    print(".")
    useTime = time.time() - startTime
    print(".")
    s = round(useTime, 3)
    print(str(s) + 's')
