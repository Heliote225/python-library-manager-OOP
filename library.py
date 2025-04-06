import json
from book import Book
from typing import List, Optional

class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, isbn: str):
        book = self.find_by_isbn(isbn)
        if book:
            self.books.remove(book)
        else:
            raise Exception(f"No book found with ISBN {isbn}")

    def find_by_title(self, title: str) -> List[Book]:
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            print(book)

    def save_to_file(self, filepath="data/books.json"):
        data = [{
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "available": book.available
        } for book in self.books]
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filepath="data/books.json"):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                for item in data:
                    book = Book(item["title"], item["author"], item["isbn"])
                    if not item["available"]:
                        book.borrow()
                    self.add_book(book)
        except FileNotFoundError:
            print("No saved data found.")