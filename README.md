# Sniper

冲顶大会答题，自动识别问题并粘贴到剪切板

*免责声明：仅供研究使用，请勿进行非法用途。*

## 环境要求

1.python 3

2.adb以及相应的环境变量

#### [1.Python 3下载](https://www.python.org/downloads/release/python-364/)

#### [2.adb环境下载](http://adbshell.com/downloads)


需要先将手机打开开发者调试模式

然后打开命令提示窗 输入 adb devices 查看是否有设备

然后运行MyPy.py 程序开始

## 程序原理

使用adb截图并保存在ScreenShot文件中，查看特征像素点判断是否为题目状态。

判断是题目状态之后对图片进行截取，截出问题。

使用百度OCR(需要自行填写OCR信息)，对图片问题进行识别，并对返回值进行处理。

使用浏览器进行查询。

#


如有指教的大佬，欢迎加我QQ联系。

QQ：1846799608 加的时候请说明是在github上看到的，谢谢。
