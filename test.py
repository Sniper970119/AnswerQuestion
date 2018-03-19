# -*- coding:utf-8 -*-
import pyperclip
import time

import HandlePic
import JudgePic
import Simple


def test(path):
    flag = JudgePic.main(path)

    if flag:
        HandlePic.HandlePic()
        key = Simple.Simple()
        pyperclip.copy(key)
        print(key)
        time.sleep(15)
        print("continue")
    else:
        print("continue")


if __name__ == '__main__':
    test('./screenshot/00001.png')
    test('./screenshot/00087.png')
    test('./screenshot/00078.png')
