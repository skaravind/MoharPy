import time, datetime
from ProofofWork import *


class Block:
	def __init__(self,previoushash, transactions):
		self.hashofBlock = hashlib.sha256(hashlib.sha256(transactions).hexdigest().encode() + previoushash).hexdigest().encode()
		self.timestamp = str(datetime.datetime.now())

	def gethash(self):
		return self.hashofBlock

genesis = Block(b'0',b'Aravind sends 10 MoHARs to Utkarsh')
blockchain = [genesis]

for i in range(2):
	for j in range(2):
		transaction = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(int(random.random()*50)))
	block = Block(blockchain[-1].gethash(), transaction.encode())
	print('Block created!, hash is = %s'%(block.gethash()))
	print('transaction in this block = %s'%transaction)
	attempt = start(blockchain[-1].gethash().decode())
	if hashlib.sha256(attempt.encode()).hexdigest().startswith('0000'):
		print('Validated!')
		blockchain.append(block)
		print('Block added to the blockchain')
print(blockchain)