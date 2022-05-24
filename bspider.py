import requests
import time
import json
import urllib3
from win10toast import ToastNotifier
import config as cc

toast = ToastNotifier()

# 使用代理访问，x-auth 为avedex.cc 请求头里的一个参数
proxies = {'https': cc.PROXY}
headers = {
    'x-auth': 'a09c739cef404fbc6f06c158a93688151653270027627173295'
}
urllib3.disable_warnings()
# url = 'https://api.opencc.xyz/v1api/v2/pairs/0x7c8922200f2c80a9c3b1262c28cfbf950952f9c0-bsc/kline?interval=1&category=u&count=800'
# r = requests.get(url, proxies=proxies, headers=headers)
# res = r.json()
# data = json.loads(res['data'])
# print(type(data))

last_price = {}
address_list = [{'name': 'LUNA', 'address': '0x156ab3346823b651294766e23e6cf87254d68962', 'origin': 0.000185, 'principal': 200, 'sum': 1000000},
                {'name': 'Supe', 'address': '0xb972c4027818223bb7b9399b3ca3ca58186e1590', 'origin': 15, 'principal': 2500, 'sum': 237.016}]

def get_address_price(address):
    url = 'https://api.opencc.xyz/v1api/v2/tokens/%s-bsc' % address
    r = requests.get(url, proxies=proxies, headers=headers, verify=False)
    res = r.json()
    data = json.loads(res['data'])
    return data['token']['current_price_usd']

def get_prices():
    msg_res = []
    for item in address_list:
        url = 'https://api.opencc.xyz/v1api/v2/tokens/%s-bsc' % item['address']
        r = requests.get(url, proxies=proxies, headers=headers, verify=False)
        res = r.json()
        data = json.loads(res['data'])
        # print('当前时间：%s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        # print('当前价格： %.8f' % data['token']['current_price_usd'])
        # print('当前涨幅: %.2f %%' % (data['token']['price_change']))
        if item['name'] in last_price and last_price[item['name']] != 0:
            update = (data['token']['current_price_usd'] - last_price[item['name']]) / last_price[item['name']]
            rose = (data['token']['current_price_usd'] - item['origin']) / item['origin']
            title = '%s： %.8f' % (item['name'], data['token']['current_price_usd'])
            msg = '^%.2f $ %.2f' % (rose, (rose * item['principal']))
            msg_res.append(title)
        else:
            rose = (data['token']['current_price_usd'] - item['origin']) / item['origin']
            title = '%s： %.8f ' % (item['name'], data['token']['current_price_usd'])
            msg = ' ^%.2f $ %.2f' % (rose, (rose * item['principal']))
            msg_res.append(title)
        last_price[item['name']] = data['token']['current_price_usd']
        time.sleep(2)
    return msg_res


'''
while 1:
    for item in address_list:
        url = 'https://api.opencc.xyz/v1api/v2/tokens/%s-bsc' % item['address']
        r = requests.get(url, proxies=proxies, headers=headers, verify=False)
        res = r.json()
        data = json.loads(res['data'])
        # print('当前时间：%s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        # print('当前价格： %.8f' % data['token']['current_price_usd'])
        # print('当前涨幅: %.2f %%' % (data['token']['price_change']))
        if item['name'] in last_price and last_price[item['name']] != 0:
            update = (data['token']['current_price_usd'] - last_price[item['name']]) / last_price[item['name']]
            rose = (data['token']['current_price_usd'] - item['origin']) / item['origin']
            title = '%s： %.8f $%.2f' % (item['name'], data['token']['current_price_usd'], (data['token']['current_price_usd'] * item['sum'])) + '\r\n' + '10分钟内价格涨跌： %.2f' % update
            msg = '^%.2f $ %.2f' % (rose, (rose * item['principal']))
            toast.show_toast(title=title, duration=5, icon_path=None, msg=msg)
        else :
            rose = (data['token']['current_price_usd'] - item['origin']) / item['origin']
            title = '%s： %.8f $%.2f' % (item['name'], data['token']['current_price_usd'], (data['token']['current_price_usd'] * item['sum']))
            msg = ' ^%.2f $ %.2f' % (rose, (rose * item['principal']))
            toast.show_toast(title=title, duration=5, icon_path=None, msg=msg)
        last_price[item['name']] = data['token']['current_price_usd']
        time.sleep(2)
    time.sleep(60)
'''
