import requests
import time
import json
import urllib3
from win10toast import ToastNotifier

toast = ToastNotifier()

# 使用代理访问，x-auth 为avedex.cc 请求头里的一个参数
proxies = {'https': '10.146.243.152:7890'}
headers = {
    'x-auth': 'a3ca896fdf14e1a591607e9ee6902a4a1652621830718628681'
}
urllib3.disable_warnings()
# url = 'https://api.opencc.xyz/v1api/v2/pairs/0x7c8922200f2c80a9c3b1262c28cfbf950952f9c0-bsc/kline?interval=1&category=u&count=800'
# r = requests.get(url, proxies=proxies, headers=headers)
# res = r.json()
# data = json.loads(res['data'])
# print(type(data))

last_price = {}
address_list = [{'name': 'LUNA', 'address': '0x156ab3346823b651294766e23e6cf87254d68962', 'origin' : 0.000158, 'principal' : 500, 'sum' : 3157342.378816},
                {'name': 'GAL', 'address': '0xe4Cc45Bb5DBDA06dB6183E8bf016569f40497Aa5', 'origin' : 5.78, 'principal' : 300, 'sum' : 51.8734}]
while 1:
    for item in address_list :
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
            # print('当前价格： %.8f' % data['token']['current_price_usd'] + '\r\n' + 'LUNA 10分钟内价格涨跌： %.2f' % update)
            title = '%s： %.8f $%.2f' % (item['name'], data['token']['current_price_usd'], (data['token']['current_price_usd'] * item['sum']))
            msg = '^%.2f $ %.2f' % ( rose, (rose * item['principal'])) + '\r\n' + '10分钟内价格涨跌： %.2f' % update
            toast.show_toast(title=title, duration=5, icon_path=None, msg=msg)
        else :
            rose = (data['token']['current_price_usd'] - item['origin']) / item['origin']
            title = '%s： %.8f $%.2f' % (item['name'], data['token']['current_price_usd'], (data['token']['current_price_usd'] * item['sum']))
            msg = ' ^%.2f $ %.2f' % (rose, (rose * item['principal']))
            toast.show_toast(title=title, duration=5, icon_path=None, msg=msg)
        last_price[item['name']] = data['token']['current_price_usd']
        time.sleep(2)
    time.sleep(300)
