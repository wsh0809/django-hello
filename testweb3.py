import config as cc
import bspider
import api
from BaseUtil import Address, NodeClient, Kit, Net, SmartContract
from BuyTokens import buy_tokens
from time import sleep

address = Address(address="0xceF9120096a6C05052ba2376EfD4F10EA0Ae2BB1", private_key="")
busd_token = "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"
kit = Kit(NodeClient.create(url=Net.main_net, proxy=cc.PROXY), address)
to_address = "0x80369d08c1617fcab4b54514e19c7a80feb0666e"
# 先转0.005的BNB
to_address = kit.web3.toChecksumAddress(to_address)
# nonce = kit.web3.eth.get_transaction_count(kit.web3.toChecksumAddress('0xceF9120096a6C05052ba2376EfD4F10EA0Ae2BB1'))
# tx = {
#     'nonce': nonce,
#     'to': to_address,
#     'gas': 160000,
#     'gasPrice': kit.web3.toWei('5', 'gwei'),
#     'value': kit.web3.toWei(0.005, 'ether')
# }
# try:
#     signed_tx = kit.web3.eth.account.sign_transaction(tx, '')
#     print(signed_tx)
#     tx_hash = kit.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
#     print(tx_hash)
#     print(kit.web3.toHex(tx_hash), 'pay success')
# except Exception as e:
#     print(f'转账异常: {e}')
# exit(0)

try:
    nonce = kit.web3.eth.get_transaction_count(kit.web3.toChecksumAddress('0xceF9120096a6C05052ba2376EfD4F10EA0Ae2BB1'))
    busd_token = kit.web3.toChecksumAddress(busd_token)
    busd_contract = kit.web3.eth.contract(address=busd_token, abi=api.tokenAbi(kit.web3.toChecksumAddress('0xb972c4027818223bb7b9399b3ca3ca58186e1590')))
    busd_txn = busd_contract.functions.transfer(to_address, kit.web3.toWei(51, 'ether')).buildTransaction({
        'from': kit.web3.toChecksumAddress('0xceF9120096a6C05052ba2376EfD4F10EA0Ae2BB1'),
        'gas': 160000,
        'gasPrice': kit.web3.toWei('5', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = kit.web3.eth.account.sign_transaction(busd_txn, private_key=address.get_private_key())
    tx_token = kit.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(kit.web3.toHex(tx_token))
except Exception as e:
    print(f'转账异常: {e}')
exit(0)


