import json
#import datetime
from merkle import *
#from tx import *
from proof_of_work import *

if __name__ == '__main__':	
	hashList = []	
	txList = ['tx1', 'tx2', 'tx3','tx4', 'tx5']
	
	for tx in txList:
		hashList.append(hasheo(tx))
	

def buidBlock(message, difficulty, hashList, transaction, hashPrevious):
	#timeStamp = datetime.datetime.now() 

	block = {
		"header": {
			"hashPrevious": hashPrevious,
			"nonce": getNonce(message, difficulty),
			"rootHash": merkleFunction(hashList),	
		},
		"body": {
			"transaction": transaction
		}
	}
	blockString = json.dumps(block)
	print(f'bloque string {blockString}')
	hashBlock = hasheo(blockString)
	print(f'El hash de este bloque es: {hashBlock}' )
	
	return hashBlock


if __name__ == '__main__':	
	tx = 'transacción exitosa'
	buidBlock('hello world', 1, hashList, tx, hasheo('message'))