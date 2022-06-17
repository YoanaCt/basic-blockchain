import hashlib
#import pickle

wallets = {
	'Alice': 80,
	'Bob' : 50
}
walletsBefore = wallets.copy()

wallet1 = wallets['Alice']
wallet2 = wallets['Bob'] 

""" wallets = {
	'w1': 50,
	'w2': 80
} """


def transaction(wallet1, wallet2, send):
	if wallet1 < send:
		return 'ERROR'
	else:
		wallet1 -= send
		wallet2 += send

	wallets['Alice'] = wallet1
	wallets['Bob'] = wallet2

	tx = f'Estado antes de la transacción: {walletsBefore}, Estado luego de la transacción: {wallets} '  

	return tx


hs = str(wallets)
print(f' Convertido a string{hs}')

def hasheo(message):
	return hashlib.sha256(message.encode()).hexdigest()

print(hasheo(hs))

class bloque:
	tx1 = transaction(wallets['Alice'], wallets['Bob'], 50) 
	tx2 = transaction(wallets['Bob'], wallets['Alice'], 15)

	print(tx1)
