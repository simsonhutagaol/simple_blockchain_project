class Transaction:
    def __init__(self, sender, receiver, amount): 
        self.sender = sender #sender artinya pengirim 
        self.receiver = receiver #receiver artinya penerima
        self.amount = amount #amount artinya jumlah yang dikirimkan

    def __str__(self): #method ini akan mengembalikan string yang berisi informasi pengirim, penerima, dan jumlah yang dikirimkan 
        return f"{self.sender} mengirim {self.amount} ke {self.receiver}"