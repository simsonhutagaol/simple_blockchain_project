import time
from block import Block
class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()] #membuat blockchain dengan blok genesis 
        self.difficulty = difficulty #tingkat kesulitan mining 
        self.pending_transactions = [] #transaksi yang belum diproses 

    def create_genesis_block(self): #method ini akan membuat blok genesis 
        return Block(0, "0", ["Genesis Block"], time.time()) #blok genesis memiliki previous hash 0 dan data "Genesis Block"

    def get_latest_block(self): #method ini akan mengembalikan blok terakhir di blockchain 
        return self.chain[-1] #blok terakhir adalah blok dengan index paling besar 

    def add_transaction(self, transaction): #method ini akan menambahkan transaksi ke pending_transactions 
        self.pending_transactions.append(transaction) #menambahkan transaksi ke pending_transactions 

    def mine_pending_transactions(self): #method ini akan memproses transaksi yang ada di pending_transactions 
        new_block = Block(len(self.chain), self.get_latest_block().hash, self.pending_transactions, time.time()) #membuat blok baru dengan transaksi yang ada di pending_transactions
        new_block.mine_block(self.difficulty) #melakukan proses mining blok 
        self.chain.append(new_block) #menambahkan blok baru ke blockchain 
        self.pending_transactions = [] #mengosongkan pending_transactions

    def is_chain_valid(self): #method ini akan memeriksa apakah blockchain valid atau tidak 
        for i in range(1, len(self.chain)): #untuk setiap blok di blochchain
            current_block = self.chain[i] #blok saat ini
            previous_block = self.chain[i - 1] #blok sebelumnya

            if current_block.hash != current_block.calculate_hash(): #jika hash blok tidak valid
                print("Hash tidak valid!")
                return False

            if current_block.previous_hash != previous_block.hash: #jika previous hash tidak valid
                print("Previous hash tidak valid!")
                return False

        return True #jika semua blok valid, maka blockchain valid