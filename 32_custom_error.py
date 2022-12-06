class TooManyPagesReadError(ValueError):
    pass
    
class Book:
    def __init__(self, name: str, page_count: int) -> None:
        self.name = name
        self.page_count = page_count
        self.page_read = 0
    
    def __repr__(self) -> str:
        return(
            f"<Book {self.name}, read {self.page_read} pages out of {self.page_count}>"
        )
    
    def read(self, pages: int):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.page_read + pages } pages, but this book only has {self.page_count} pages"
            )
        self.page_read += pages
        print(f"you have read {self.page_read} pages out of {self.page_count}")
        
pythonBook  = Book("Python Basic", 50)
try:
    pythonBook.read(25)
    pythonBook.read(26)
except TooManyPagesReadError as e:
    print(e)