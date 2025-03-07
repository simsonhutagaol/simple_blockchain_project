import hashlib
class Block:
    def __init__(self, index, previous_hash, transactions, timestamp, nonce=0):
        self.index = index
        self.previous_hash = previous_hash #hash dari blok sebelumnya 
        self.transactions = transactions #transaksi yang terjadi di blok ini 
        self.timestamp = timestamp #waktu blok dibuat
        self.nonce = nonce #nonce digunakan untuk proses mining
        self.hash = self.calculate_hash() #hash dari blok ini

    def calculate_hash(self): #method ini akan menghitung hash dari blok ini 
        block_data = str(self.index) + self.previous_hash + str(self.transactions) + str(self.timestamp) + str(self.nonce) #menggabungkan data-data blok 
        return hashlib.sha256(block_data.encode()).hexdigest() #menghitung hash dari data-data blok 

    def mine_block(self, difficulty): #method ini akan melakukan proses mining blok 
        target = '0' * difficulty #target adalah string yang terdiri dari difficulty banyak karakter '0' 
        while self.hash[:difficulty] != target: #selama hash blok tidak memenuhi target, nonce akan terus ditambahkan dan hash akan dihitung ulang
            self.nonce += 1 #menambahkan nonce 
            self.hash = self.calculate_hash() #menghitung hash baru 
        print("Blok berhasil ditambang:", self.hash) 