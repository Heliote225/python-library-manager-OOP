from book import Book
from library import Library

def print_menu():
    print("\n===== Library Manager =====")
    print("1. List all books")
    print("2. Add a book")
    print("3. Remove a book")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Search by title")
    print("7. Save and exit")
    print("============================")

def main():
    lib = Library()
    lib.load_from_file()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()

        elif choice == "2":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            lib.add_book(Book(title, author, isbn))
            print("Book added.")

        elif choice == "3":
            isbn = input("ISBN of the book to remove: ")
            try:
                lib.remove_book(isbn)
                print("Book removed.")
            except Exception as e:
                print(e)

        elif choice == "4":
            isbn = input("ISBN of the book to borrow: ")
            book = lib.find_by_isbn(isbn)
            if book:
                try:
                    book.borrow()
                    print("Book borrowed.")
                except Exception as e:
                    print(e)
            else:
                print("Book not found.")

        elif choice == "5":
            isbn = input("ISBN of the book to return: ")
            book = lib.find_by_isbn(isbn)
            if book:
                book.return_book()
                print("Book returned.")
            else:
                print("Book not found.")

        elif choice == "6":
            title = input("Enter part of the title to search: ")
            results = lib.find_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found with that title.")

        elif choice == "7":
            lib.save_to_file()
            print("Library saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()