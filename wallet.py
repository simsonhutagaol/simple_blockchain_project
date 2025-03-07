from transaction import Transaction

class Wallet:
    def __init__(self, name): # ini merupakan constructor yang akan dijalankan ketika objek dibuat dengan nama Wallet dan parameter name yang diinputkan oleh user 
        self.name = name
        self.balance = 100  # Saldo awal

    def send_money(self, receiver, amount, blockchain): #method ini akan mengirimkan uang dari wallet pengirim ke wallet penerima dengan jumlah tertentu 
        if self.balance >= amount: #jika saldo wallet pengirim lebih besar atau sama dengan jumlah yang akan dikirimkan maka transaksi akan dilakukan 
            transaction = Transaction(self.name, receiver.name, amount) #membuat objek transaction dengan parameter sender, receiver, dan amount 
            blockchain.add_transaction(transaction) #menambahkan transaksi ke blockchain 
            self.balance -= amount #mengurangi saldo wallet pengirim 
            receiver.balance += amount #menambah saldo wallet penerima
            print(f"{self.name} mengirim {amount} ke {receiver.name}")
        else:
            print("Saldo tidak cukup!")