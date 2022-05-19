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

last_price = {}
address_list = [{'name': 'LUNA', 'address': '0x156ab3346823b651294766e23e6cf87254d68962', 'origin': 0},
                {'name': 'GAL', 'address': '0xe4Cc45Bb5DBDA06dB6183E8bf016569f40497Aa5', 'origin': 0}]

# toast.show_toast(title='开启监听......', duration=5)
while 1:
    for item in address_list :
        url = 'https://api.opencc.xyz/v1api/v2/tokens/%s-bsc' % item['address']
        r = requests.get(url, proxies=proxies, headers=headers, verify=False)
        res = r.json()
        data = json.loads(res['data'])
        
        if item['origin'] != 0:
            update = (data['token']['current_price_usd'] - item['origin']) / item['origin']
            if update <= -0.08 :
                # 跌幅 8%
                title = '%s： %.8f %.2f' % (item['name'], data['token']['current_price_usd'], update)
                toast.show_toast(title=title, duration=5)
        else :
            item['origin'] = data['token']['current_price_usd']
        time.sleep(2)
    time.sleep(60)
