import requests

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另外一个模块')


def test_1():
    url = 'http://c.biancheng.net/uploads/course/python_spider/191009.html'

    res = requests.get(url)

    res.encoding = 'utf-8'

    file = open('全身在格斗中的作用.txt', 'a+')
    """
    a 是在末尾追加写入，不可读取
    a+ 追加读写
    r 从开始读取，不存在文件报错
    r+ 从开始读写，覆盖
    w 从开始写 不存在文件则创建
    w+ 从开始读写
    """
    file.write(res.text)
    file.close()


def test_2():
    url = 'https://release.ashgso.com/CheckList/Upload/CGI/82bb069a2c046dc1c0926c.png'
    res = requests.get(url)
    photo = open('be careful.jpg', 'wb')
    photo.write(res.content)
    photo.close()


def test_3():
    url = 'http://vcast-resource.cdn.bcebos.com/vcast-resource/de76312e-af16-4c02-a9c9-cea509719f89.mp3'
    res = requests.get(url)
    photo = open('test.mp3', 'wb')
    photo.write(res.content)
    photo.close()
