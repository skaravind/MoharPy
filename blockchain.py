import hashlib

class Block:
	def __init__(self,previoushash, transactions):
		self.hashofBlock = hashlib.sha256(hashlib.sha256(transactions).hexdigest().encode() + previoushash).hexdigest().encode()

	def gethash(self):
		return self.hashofBlock

genesis = Block(b'0',b'Aravind sends 10 MoHARs to Utkarsh')
blockchain = []
blockchain.append(genesis)

for i in range(2):
	for j in range(2):
		transactions = []
		transaction = input()
		transactions.append(transaction)
	trans = ''
	for t in transactions:
		trans += t
	block = Block(blockchain[-1].gethash(), trans.encode())
	blockchain.append(block)
	print('Block created!, hash is = %s'%(blockchain[-1].gethash()))

print(blockchain)