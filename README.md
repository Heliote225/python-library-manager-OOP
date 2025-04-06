# python-library-manager-OOP

## Structure des fichiers
python-library-manager/
│
├── README.md
├── main.py
├── book.py
├── user.py
├── member.py
├── librarian.py
├── library.py
├── exceptions.py
├── data/
│   └── books.json
├── tests/
│   └── test_library.py
├── requirements.txt
└── .gitignore

## Library Manager CLI

A simple command-line application written in Python to manage a small library system using object-oriented programming (OOP) principles.

### Features

- Add, remove, and search for books
- Manage members and librarians
- Borrow and return books
- Save and load data (JSON format)
- Command-line menu interface
- Unit tests included

### Technologies

- Python 3.x
- JSON for data persistence
- unittest for testing

### Getting Started

#### Clone the repository

git clone https://github.com/votre-utilisateur/python-library-manager.git
cd python-library-manager

#### Install dependencies (if any)

pip install -r requirements.txt

#### Run the app

python main.py

#### Run tests

python -m unittest discover tests
