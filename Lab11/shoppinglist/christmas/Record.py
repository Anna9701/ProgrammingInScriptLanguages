class Record:
    id = int
    name = str()
    amount = str()
    price = str()
    isBought = "No"

    def __init__(self, i, n, a, p, b):
        self.id = i
        self.name = n
        self.amount = str(a)
        self.price = str(p)
        if b:
            self.isBought = "Yes"
