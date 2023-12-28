

class Book:
    def __init__(self, title, author, price, quantity,id=None):
        self.id=id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity