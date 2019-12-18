class Record:
    id = int
    name = str()
    amount = str()
    price = str()
    isBought = False

    def __init__(self, i, n, a, p, b):
        self.id = i
        self.name = n
        self.amount = str(a)
        self.price = str(p)
        self.isBought = b
