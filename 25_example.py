class Book:
    
    TYPE = ("Hardcover", "Softcover")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weight is {self.weight}gms>"
        

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPE[0], page_weight+100)
    
    @classmethod
    def softcover(cls, name, page_weight):
        return cls(name, cls.TYPE[1], page_weight)
    
    
#book = Book("Bhagvad Gita", "Hardcover", 1200)

hardcover_book = Book.hardcover("Bhagvad Gita", 1200)
softcover_book = Book.softcover("Ramayan", 1000)

print(hardcover_book)
print(softcover_book)