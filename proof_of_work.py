from hash import hasheo
import random
from random import randint
	
def mineBlock(message, difficulty):
	pofw = message
	zeroInhash = 0

	while zeroInhash != difficulty:
		nonce = str(randint(0,9999999999999999999999999999999))
		pofw = hasheo(pofw + nonce)	
		
		for character in pofw[0:difficulty]:
			miner = random.randrange(1,5)  # Se elige aleatoriamente un minero de las wallets 			
			if character != '0':					 # presdeterminadas para simular a un minero que realiza la pofw
				zeroInhash = 0
				break			
			zeroInhash += 1		
	return nonce, miner, pofw

# Solo se ejecuta en este módulo, utilizado para hacer pruebas
if __name__ == '__main__': 
	difficulty = 4
	mineBlock('message',difficulty)
	miner =  mineBlock('message',difficulty)[1]
	nonce = mineBlock('message',difficulty)[0]
	pow = mineBlock('message',difficulty)[2]
	print(f'El nonce de esta prueba de trabajo es: {nonce}\nEl hash encontrado es: {pow} ')
	print(f'El minero que realizó esta prueba de trabajo es: {miner}' )
	
	

