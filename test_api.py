import api
from web3 import Web3
import config as cc
import bspider

supe_address = '0xb972c4027818223bb7b9399b3ca3ca58186e1590'
pancake_address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
abi = api.tokenAbi(supe_address, None)
sender_address = "0xceF9120096a6C05052ba2376EfD4F10EA0Ae2BB1"
bsc = "https://bsc-dataseed.binance.org/"
proxy = 'http://'+ cc.PROXY
provider = Web3.HTTPProvider(bsc, request_kwargs={"proxies": {'https': proxy, 'http': proxy}})
web3 = Web3(provider)
supe_address = web3.toChecksumAddress(supe_address)
contract = web3.eth.contract(address=supe_address, abi=abi)
balance = contract.functions.balanceOf(sender_address).call()
coins = web3.fromWei(balance, 'ether')
print(coins)
price = bspider.get_address_price(supe_address)
print(float(coins) * price)
