#!/usr/bin/env python3
class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title        # Public attribute for book title
        self.author = author      # Public attribute for book author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available (returned)."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

class Library:
    """A class representing a library with a collection of books."""

    def __init__(self):
        self._books = []  # Private list to store book instances

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Checked out {title}"
        return f"Book '{title}' is not available."

    def return_book(self, title):
        """Return a book to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Returned {title}"
        return f"Book '{title}' is not checked out."

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are available.")

