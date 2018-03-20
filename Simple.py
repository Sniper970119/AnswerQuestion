# -*- coding:utf-8 -*-

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = 'xxxxx'
API_KEY = 'xxxxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def Simple():
    image = get_file_content('./Handle/HandlePic.png')

    """ 调用通用文字识别, 图片参数为本地图片 """
    client.basicGeneral(image)

    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    a = client.basicGeneral(image, options)
    a = a['words_result']
    word = ''
    # print(a)
    if len(a) == 2:
        b = a[0]
        word = word + b['words']
        b = a[1]
        word = word + b['words']
    elif len(a) == 1:
        b = a[0]
        word = b['words']
    # print(word)
    return word


# if __name__ == '__main__':
#     Simple()
