import requests
import this


def pim_test():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    data = {
        'account': 'admin',
        'password': 'test123456',
        't': 'json',
    }
    session = requests.session()
    response = session.post('https://release.ashgso.com/CheckList/Public/checkLogin', verify=False, data=data)
    # print(response.headers)
    print(response.status_code)
    # print(response.content)
    # print(response.url)
    # print(response.cookies)
    file = {
        'file': ('狗头.jpg', open('狗头.jpg', 'rb'), 'image/jpg'),
    }
    data = {
        'dir': 'Cgi'
    }
    response = session.post('https://release.ashgso.com/CheckList/Pim/Upload/index', data=data, files=file)
    response.raise_for_status()
    print(response.status_code)
    print(response.json())
    return True


pim_test()
# []    列表
# {}    字典
# () (1,2) 元组
# {1,2,} set() 集合
exit(0)

r = requests.get('https://api.github.com/events')
print(r.encoding)

