import json
import datetime
from merkle import *
from transaction import *
from proof_of_work import *
from hash import hasheo


def buildBlock(message, difficulty, hashPrevious, coins, hashBlockIndex, txList):
	#timestamp = datetime.datetime.now() 
	
	pofw = mineBlock(message, difficulty)
	nonce  = pofw[0]
	miner = pofw[1]	
	keyMiner = str(miner)
	wallets[keyMiner] = reward
	coins -= reward
	rootHash = None
	hashList = []

	if len(hashBlockIndex) == 0:		
		transaction = f'Pimer bloque minado por: {miner}, recibe {reward} de recompensa'
	else:		
		tx = txList[0]		
		hashList.append(tx)		
		del txList[0]
		transaction = hashList.copy()
		rootHash = merkleFunction(hashList)

	block = {
		"header": {			
			"hashPrevious": hashPrevious,
			"nonce": nonce,
			"rootHash": rootHash
		},
		"body": {
			"transactions": transaction
		}
	}	
	
	blockString = json.dumps(block)	
	hashBlock = hasheo(blockString)
	#print(f'El hash de este bloque es: {hashBlock}' )	
	return hashBlock, miner, rootHash, nonce, hashPrevious, coins





