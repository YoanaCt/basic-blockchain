
import hashlib

def hasheo(message):
	return hashlib.sha256(message.encode()).hexdigest()

# Solo se ejecuta en este módulo, utilizado para hacerle prueba
if __name__ == '__main__':	
	txList = ['tx1', 'tx2', 'tx3','tx4', 'tx5']
	hashList = []	
	for tx in txList:
		hashList.append(hasheo(tx))

def merkleFunction(hashList):
	newHashList = []
	while (len(hashList)!= 0 or len(newHashList) !=0):
		if len(hashList)  > 1:
			newElement = hashList[0] + hashList[1]
			del hashList[:2]

			newHash = hasheo(newElement)	
			newHashList.append(newHash)	
			
		elif len(hashList) == 1:
			newElement = hashList[0]
			del hashList[0]

			newHash = hasheo(newElement)	
			newHashList.append(newHash)		

		elif len(hashList) == 0  and len(newHashList) !=1:
			hashList = newHashList.copy()
			print(hashList)
			newHashList.clear()
			
		elif len(hashList) == 0  and len(newHashList) ==1:
			print('****ROOT****')
			hashRoot = newHashList[0]
			newHashList.clear()
			print(f'Hash Root: {hashRoot}')		

		print(f' HashList: {hashList}')		
		print(f'New hashList:{newHashList}')
		print('*************************************************************')
	

if __name__ == '__main__':	
	merkleFunction(hashList)




			





		
		


