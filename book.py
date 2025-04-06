class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available = True

    def borrow(self):
        if not self._available:
            raise Exception(f"The book '{self.title}' is already borrowed.")
        self._available = False

    def return_book(self):
        self._available = True

    @property
    def available(self):
        return self._available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"