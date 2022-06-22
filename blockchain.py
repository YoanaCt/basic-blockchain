from block import *
from tx import *

class Blockchain:
	def __init__(self,difficulty):
		self.difficulty = difficulty

	def hasheo(message):
		return hashlib.sha256(message.encode()).hexdigest()

	def buildBlockchain():
		hashBlockIndex = {}	
		height = 0
		transactions = []		

		if height==0:
			hashPrevious = hasheo('Hash previo del bloque génesis')
			pof = getNonce('message',1)
			nonce = pof[0]
			miner = pof[1]
			wallets[miner] = reward
			coins -= reward
			tx = f'Pimer bloque minado por: {miner}, recibe {reward} de recompensa'

			block = {
				"header": {
					"hashPrevious": hashPrevious,
					"nonce": nonce			
				},
				"body": {
					"transaction": tx
				}
			}
			blockToString = json.dumps(block)
			hashBlock = hasheo(blockToString)
			#print(hashBlock)

			height += 1
			hashBlockIndex[str(len(hashBlockIndex))] = hashBlock

		else:		
			makeTransactions = 'y'
			hashTxList = []
			hashPrevious = hashBlockIndex[str(len(hashBlockIndex)-1)]
			while(makeTransactions == 'y'):
				transactions = input('Hacer transacción: y/n')
				
				walletOrigin = input('ingrese la wallet origen')
				walletDestiny = input('ingrese la wallet destino')
				send = input('Ingrese el monto a enviar')
				tx = transaction(walletOrigin, walletOrigin, send)
				transactions.append[tx]

				for index in tx:
					hashTxList.append(hasheo(tx))	

			transaction = hashTxList[0]
			
			buidBlock('message', difficulty, hashList, transaction, hashPrevious)


		#print(hashPrevious)
	
	
			
blockchain1 = Blockchain(1)
