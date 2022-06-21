import json
import datetime
from merkle import *
from transaction import *
from proof_of_work import *


def buidBlock(message, difficulty, hashList, w1, w2, send, hashPrevious):
	timeStamp = datetime.datetime.now() #str(datetime.timedelta(seconds=60))

	block = {
		"header": {
			"hashPrevious": hashPrevious,
			"nonce": getNonce(message, difficulty),
			"rootHash": merkleFunction(hashList),	
		},
		"body": {
			"transaction": transaction(w1, w2, send)
		}
	}
	blockString = json.dumps(block)
	print(f'bloque string {blockString}')
	hashBlock = hasheo(blockString)
	print(f'El hash de esta bloque es: {hashBlock} ' )
	return hashBlock


if __name__ == '__main__':	
	buidBlock('hello world', 1, hashList, 80, 50, 15, hasheo('message'))