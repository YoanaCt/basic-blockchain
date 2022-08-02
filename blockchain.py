from block import *
from transaction import *
from merkle import *
from proof_of_work import *

def buildBlockchain(difficulty):	
	
	# Atibutos iniciales de la blockchain
	hashBlockIndex = {}	
	txList = []	 #Lista para almacenar las transacciones efectuadas
	blockNumber = -1
	height = blockNumber
	hashPrevious = hasheo('Hash previo para el bloque génesis')
	
	# llamado a la función buildBlock para construir el bloque génesis
	block = buildBlock('message', difficulty, hashPrevious, coins, hashBlockIndex, txList)

	hashBlock = block[0]
	miner = block[1]
	rootHash = block[2]
	nonce = block[3]	

	# Metadata correspondiente al bloque génesis
	hashBlockIndex[str(len(hashBlockIndex))] = hashBlock
	blockNumber += 1
	height += 1

	print(f'Bloque {blockNumber}'.center(50,'-'))
	print(f'Hash: {hashBlock} ')
	print(f'Hash previo: {hashPrevious} ')
	print(f'Miner: {miner} ' )
	print(f'Merkle Root: {rootHash} ' )
	print(f'Nonce: {nonce} ' )

	#Llamado a la función que obtiene las transacciones 
	txList = getTransactions()

	# Recorre la lista de transacciones y construye un bloque por transacción
	while txList:
		block = buildBlock('message', difficulty, hashBlock, block[5], hashBlockIndex, txList)

		hashBlock = block[0]
		miner = block[1]
		rootHash = block[2]
		nonce = block[3]
		hashPrevious = block[4]

		hashBlockIndex[str(len(hashBlockIndex))] = hashBlock
		#hashPrevious = hashBlockIndex[str(len(hashBlockIndex))]
		blockNumber += 1
		height += 1
		
		print(f'Bloque {blockNumber}'.center(50,'-'))
		print(f'Hash: {hashBlock} ')
		print(f'Hash previo: {hashPrevious} ')
		print(f'Miner: {miner} ' )
		print(f'Merkle Root: {rootHash} ' )
		print(f'Nonce: {nonce} ' )

	
buildBlockchain(5)