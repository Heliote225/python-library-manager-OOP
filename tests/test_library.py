import unittest
from book import Book
from library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = Library()
        self.book1 = Book("1984", "George Orwell", "123456789")
        self.book2 = Book("Brave New World", "Aldous Huxley", "987654321")
        self.lib.add_book(self.book1)
        self.lib.add_book(self.book2)

    def test_add_book(self):
        self.assertEqual(len(self.lib.books), 2)

    def test_find_by_isbn(self):
        book = self.lib.find_by_isbn("123456789")
        self.assertEqual(book.title, "1984")

    def test_find_by_title(self):
        results = self.lib.find_by_title("brave")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Aldous Huxley")

    def test_remove_book(self):
        self.lib.remove_book("987654321")
        self.assertEqual(len(self.lib.books), 1)
        self.assertIsNone(self.lib.find_by_isbn("987654321"))

    def test_borrow_and_return(self):
        self.book1.borrow()
        self.assertFalse(self.book1.available)
        self.book1.return_book()
        self.assertTrue(self.book1.available)

    def test_borrow_unavailable_book_raises_exception(self):
        self.book1.borrow()
        with self.assertRaises(Exception):
            self.book1.borrow()

if __name__ == '__main__':
    unittest.main()