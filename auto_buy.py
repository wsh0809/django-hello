import config as cc
import bspider
import api
from BaseUtil import Address, NodeClient, Kit, Net, SmartContract, CustomWindow
from BuyTokens import buy_tokens
from time import sleep


"""
desc：自动买卖某个smart contract token
1.先配置购买的token address 和 兑换所用的 token address（busd）,设置买入的价格和卖出的价格
2.通过为avedex.cc获取当前token价格，如果价格低于买入价格，并且地址中该token的数量为0，则买入，数量不为0则不操作；如果价格高于等于卖出价格，并且地址中该token的数量大于0，则卖出，数量为0则不操作
"""

address = Address(address=cc.WALLET_ADDRESS, private_key=cc.PRIVATE_KEY)
buy_token = "0x156ab3346823b651294766e23e6cf87254d68962"
busd_token = "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"
buy_price = 0.000128
sale_price = 0.000134
auto_buy_money = 50
kit = Kit(NodeClient.create(url=Net.main_net, proxy=cc.PROXY), address)
buy_token = kit.web3.toChecksumAddress(buy_token)
buy_contract = SmartContract(kit.web3.eth.contract(address=buy_token, abi=api.tokenAbi(buy_token)))
busd_token = kit.web3.toChecksumAddress(busd_token)
busd_contract = SmartContract(kit.web3.eth.contract(address=busd_token, abi=api.tokenAbi(busd_token)))

# while 1:
#     price = bspider.get_address_price(buy_token)
#     if price <= buy_price and kit.web3.fromWei(buy_contract.get_balance(address=address.get_address()), 'ether') == 0:
#         # 买入
#         balance = kit.web3.fromWei(busd_contract.get_balance(address=address.get_address()), 'ether')
#         buy_tokens(kit=kit, tokenToBuy=buy_token, tokenSpend=busd_token, value=balance)
#         print('买入%d' % auto_buy_money)
#     elif price >= buy_price and kit.web3.fromWei(buy_contract.get_balance(address=address.get_address()), 'ether') > 0:
#         # 卖出
#         balance = kit.web3.fromWei(buy_contract.get_balance(address=address.get_address()), 'ether')
#         buy_tokens(kit=kit, tokenToBuy=busd_token, tokenSpend=buy_token, value=balance)
#         print('卖出入%d' % auto_buy_money)
#     else:
#         print('无操作 %.8f' % price)
#     sleep(60)


def auto_swap():
    try:
        price = bspider.get_address_price(buy_token)
        if price <= buy_price and buy_contract.get_balance(address=address.get_address()) == 0:
            # 买入
            balance = busd_contract.get_balance(address=address.get_address())
            res = buy_tokens(kit=kit, tokenToBuy=buy_token, tokenSpend=busd_token, value=balance)
            msg = '买入%d \n %s' % (kit.web3.fromWei(balance, 'ether'), res)
        elif price >= sale_price and buy_contract.get_balance(address=address.get_address()) > 0:
            # 卖出
            balance = buy_contract.get_balance(address=address.get_address())
            res = buy_tokens(kit=kit, tokenToBuy=busd_token, tokenSpend=buy_token, value=balance)
            msg = '卖出%d \n %s' % (kit.web3.fromWei(balance, 'ether'), res)
        else:
            buy_balance = kit.web3.fromWei(buy_contract.get_balance(address=address.get_address()), 'ether')
            busd_balance = kit.web3.fromWei(busd_contract.get_balance(address=address.get_address()), 'ether')
            print(type(buy_balance))
            msg = '无操作 %.8f\n token: %s \n busd: %f ' % (price, buy_balance, busd_balance)
        print(msg)
    except Exception as e:
        print(e)
        msg = str(e)
    return msg


window = CustomWindow(auto_swap)
