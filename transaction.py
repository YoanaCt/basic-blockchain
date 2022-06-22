from blockchain import *

coins = 50000000
reward = 20

wallets = {
	'1': 0,
	'2': 0,
	'3': 0,
	'4': 0,
	'5': 0
}

walletsBefore = wallets.copy()

def transaction(wallet1, wallet2, send):
	if wallet1 < send:
		return 'ERROR'
	else:
		wallet1 -= send
		wallet2 += send

	wallets[wallet1] = wallet1
	wallets[wallet2] = wallet2

	tx = f'Estado antes de la transacción: {walletsBefore}, Estado luego de la transacción: {wallets} '  
	return tx


