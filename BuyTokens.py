import time
import config

def buyTokens(**kwargs):
	symbol = kwargs.get('symbol')
	wb3 = kwargs.get('web3')
	walletAddress = kwargs.get('walletAddress')
	contractPancake = kwargs.get('contractPancake')
	TokenToBuyAddress = kwargs.get('TokenToSellAddress')
	WBNB_Address = kwargs.get('WBNB_Address')