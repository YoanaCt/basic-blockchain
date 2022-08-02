import hashlib

def hasheo(message):
	return hashlib.sha256(message.encode()).hexdigest()
	