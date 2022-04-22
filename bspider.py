import requests
import time
import json

proxies = {'https': '10.146.243.152:7890'}
headers = {
    'x-auth': '986297fc16a844e448e5300fe5d6de3b1650510430773871136'
}
# url = 'https://api.opencc.xyz/v1api/v2/pairs/0x7c8922200f2c80a9c3b1262c28cfbf950952f9c0-bsc/kline?interval=1&category=u&count=800'
# r = requests.get(url, proxies=proxies, headers=headers)
# res = r.json()
# data = json.loads(res['data'])
# print(type(data))

last_price = 0
url = 'https://api.opencc.xyz/v1api/v2/tokens/0x87b212d654b90b31699f42ab73058d48f37a6492-bsc'
while 1:
    r = requests.get(url, proxies=proxies, headers=headers)
    res = r.json()
    data = json.loads(res['data'])
    print('当前时间：%s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('当前价格： %e' % data['token']['current_price_usd'])
    print('当前涨幅: %.2f %%' % (data['token']['price_change']))
    if last_price != 0:
        update = (data['token']['current_price_usd'] - last_price) / data['token']['current_price_usd']
        print('一分钟内价格涨跌： %.2f' % update)
    last_price = data['token']['current_price_usd']
    time.sleep(60)
