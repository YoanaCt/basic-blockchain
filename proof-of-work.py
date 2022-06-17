import hashlib
import random

difficulty = 4

def hasheo(message):
	return hashlib.sha256(message.encode()).hexdigest()
	
def getNonce(message,difficulty):
	pfw = message
	zeroInhash = 0

	while zeroInhash != difficulty:
		nonce = str(random.random())
		pfw = hasheo(pfw + nonce)
		print(pfw)
		
		for character in pfw[0:difficulty]:
			if character != '0':				
				zeroInhash = 0
				break			
			zeroInhash += 1

	print(f'El nonce que cumple es: {nonce}\nEl hash encontrado es: {pfw} ')
	#return nonce


getNonce('g',difficulty)

#random.seed(0)
