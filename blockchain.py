from block import *

def addBlock():
	hashBlockIndex = {
	#'0': 'dfdg1dhs3jhd7kd1k4fss',
	#'1': '9f8ghf4dt0kh4hfdg5h45'
	}	

	def hashPrevious(hashBlockIndex):
		if len(hashBlockIndex)==0:
			hashPrevious = hasheo('Hash previo del bloque génesis')
		else:		
			hashPrevious = hashBlockIndex[str(len(hashBlockIndex)-1)]
			print(hashPrevious)
		return hashPrevious

	hashPrevious = hashPrevious(hashBlockIndex)
	
	newBlock = buidBlock('hello world', 1, hashList, 80, 50, 15, hashPrevious)

	hashBlockIndex[str(len(hashBlockIndex))] = newBlock

	print(hashBlockIndex)

addBlock()
