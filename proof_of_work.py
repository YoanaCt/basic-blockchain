import hashlib
import random

def hasheo(message):
	return hashlib.sha256(message.encode()).hexdigest()
	
def getNonce(message,difficulty):
	pow = message
	zeroInhash = 0

	while zeroInhash != difficulty:
		nonce = str(random.random())
		pow = hasheo(pow + nonce)	
		
		for character in pow[0:difficulty]:
			miner = random.randrange(1,5)
			if character != '0':				
				zeroInhash = 0
				break			
			zeroInhash += 1		
	return nonce, miner, pow


if __name__ == '__main__':
	difficulty = 1
	miner =  getNonce('message',difficulty)[1]
	nonce = getNonce('message',difficulty)[0]
	pow = getNonce('message',difficulty)[2]
	print(f'El nonce que cumple es: {nonce}\nEl hash encontrado es: {pow} ')
	print(f'El minero que realizó esta prueba de trabajo es: {miner}' )
	
