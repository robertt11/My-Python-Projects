class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ").strip().title()
        author = input("Enter book author: ").strip().title()
        if title and author:
            self.books.append(Book(title, author))
            print(f"Book '{title}' added!")
        else:
            print("Title and author cannot be empty!")

    def show_books(self):
        if not self.books:
            return print("Library is empty.")
        print("\n--- Library Books ---")
        for i, book in enumerate(self.books, start=1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{i}. {book.title} by {book.author} [{status}]")

    def borrow_book(self):
        title = input("Enter book title to borrow: ").strip().title()
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    return print("Already borrowed!")
                book.is_borrowed = True
                return print(f"You borrowed '{title}'!")
        print("Book not found.")

    def return_book(self):
        title = input("Enter book title to return: ").strip().title()
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    return print("Not borrowed!")
                book.is_borrowed = False
                return print(f"You returned '{title}'!")
        print("Book not found.")

    def run(self):
        while True:
            print("\n1. Add | 2. Show | 3. Borrow | 4. Return | 5. Exit")
            choice = input("Choose: ")
            
            if choice == "1": self.add_book()
            elif choice == "2": self.show_books()
            elif choice == "3": self.borrow_book()
            elif choice == "4": self.return_book()
            elif choice == "5": break

if __name__ == "__main__":
    Library().run()
