from hash import *

coins = 50000000
reward = 20

wallets = {
	'1': 0,
	'2': 0,
	'3': 0,
	'4': 0,
	'5': 0
	}

	
def transaction(wallet1, wallet2, send):	
	walletsBefore = wallets.copy()
	
	if walletsBefore[wallet1] < send:
		print('ERROR')
		return
	else:
		wallets[wallet1] -= send
		wallets[wallet2] += send	

	transaction = f'Estado antes de la transacción: {walletsBefore}, Estado luego de la transacción: {wallets} '  
	print(transaction)	
	return transaction

def getTransactions():
	transactions = ''
	txList = []
	while True:
		transactions = input('Hacer transacción: y/n\n').lower()

		if transactions == 'y':
			walletOrigin = input('ingrese la wallet origen\n')
			walletDestiny = input('ingrese la wallet destino\n')
			send = int(input('Ingrese el monto a enviar\n'))
		
			try:				
				tx = transaction(walletOrigin, walletDestiny, send)
				txList.append(hasheo(tx))
			except Exception as e:
				print(f'Ocurrió un error: {e}, ingrese valores correctos ')				
			finally:
				print(txList)
		elif transactions == 'n':
			break
		else:
			print('Opción inválida')
			break
	return txList


if __name__ == '__main__':	
	transaction(wallets[1],wallets[2],50)

