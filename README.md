# Simple Blockchain Project

This project is a simple implementation of a blockchain in Python. It includes basic functionalities such as creating wallets, making transactions, mining blocks, and validating the blockchain.

## Project Structure


## Files

- `block.py`: Contains the `Block` class which represents a single block in the blockchain.
- `blockchain.py`: Contains the `Blockchain` class which manages the chain of blocks and pending transactions.
- `transaction.py`: Contains the `Transaction` class which represents a transaction between two wallets.
- `wallet.py`: Contains the `Wallet` class which represents a user's wallet.
- `main.py`: The main script to run the blockchain simulation.

## Classes and Methods

### Block

Defined in [block.py](block.py)

- `__init__(self, index, previous_hash, transactions, timestamp, nonce=0)`: Initializes a new block.
- `calculate_hash(self)`: Calculates the hash of the block.
- `mine_block(self, difficulty)`: Mines the block by finding a hash that meets the difficulty criteria.

### Blockchain

Defined in [blockchain.py](blockchain.py)

- `__init__(self, difficulty=4)`: Initializes the blockchain with a genesis block and sets the mining difficulty.
- `create_genesis_block(self)`: Creates the genesis block.
- `get_latest_block(self)`: Returns the latest block in the chain.
- `add_transaction(self, transaction)`: Adds a transaction to the list of pending transactions.
- `mine_pending_transactions(self)`: Mines the pending transactions and adds a new block to the chain.
- `is_chain_valid(self)`: Validates the integrity of the blockchain.

### Transaction

Defined in [transaction.py](transaction.py)

- `__init__(self, sender, receiver, amount)`: Initializes a new transaction.
- `__str__(self)`: Returns a string representation of the transaction.

### Wallet

Defined in [wallet.py](wallet.py)

- `__init__(self, name)`: Initializes a new wallet with a given name and a starting balance of 100.
- `send_money(self, receiver, amount, blockchain)`: Sends money from the wallet to another wallet and adds the transaction to the blockchain.

## Usage

To run the blockchain simulation, execute the `main.py` script:

```sh
python main.py
```
# Example Output
Alice mengirim 10 ke Bob
Bob mengirim 5 ke Charlie
Blok berhasil ditambang: 0000a3b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5
Saldo Alice: 90
Saldo Bob: 105
Saldo Charlie: 105
Block 0 [Hash: 0000a3b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5, Previous Hash: 0, Data: ['Genesis Block']]
Block 1 [Hash: 0000a3b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5, Previous Hash: 0000a3b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5, Data: [<transaction.Transaction object at 0x7f8b8c0b0d30>, <transaction.Transaction object at 0x7f8b8c0b0d60>]]


# Next Steps:
- Network: Simulasikan jaringan blockchain dengan beberapa node yang saling berkomunikasi.

- Consensus: Implementasikan mekanisme konsensus seperti Proof of Stake (PoS).

- Database: Simpan blockchain di database seperti SQLite atau MongoDB.

- Frontend: Buat antarmuka pengguna menggunakan Flask atau Django.