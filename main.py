from blockchain import Blockchain
from wallet import Wallet
# Membuat blockchain
my_blockchain = Blockchain(difficulty=4) #membuat blockchain dengan tingkat kesulitan 4

# Membuat wallet untuk pengguna
alice = Wallet("Alice") #membuat wallet dengan nama Alice
bob = Wallet("Bob") #membuat wallet dengan nama Bob
charlie = Wallet("Charlie") #membuat wallet dengan nama Charlie

# Alice mengirim 10 ke Bob
alice.send_money(bob, 10, my_blockchain) #Alice mengirim 10 ke Bob

# Bob mengirim 5 ke Charlie
bob.send_money(charlie, 5, my_blockchain) #Bob mengirim 5 ke Charlie

# Menambang blok untuk memproses transaksi
my_blockchain.mine_pending_transactions() #menambang

# Menampilkan saldo akhir
print(f"Saldo Alice: {alice.balance}")
print(f"Saldo Bob: {bob.balance}")
print(f"Saldo Charlie: {charlie.balance}")

# Menampilkan isi blockchain
for block in my_blockchain.chain: #untuk setiap blok di blockchain
    print(f"Block {block.index} [Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.transactions}]")