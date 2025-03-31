class Library:
    def __init__(self, username):
        self.books = []
        self.username = username
        print(f"\nHello {self.username}, welcome to your Library!\n")

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})
        print(f'Book "{title}" by {author} added successfully!')

    def search_book(self, title):
        found_books = [book for book in self.books if book["title"].lower() == title.lower()]
        if found_books:
            print("Book found:", found_books[0])
        else:
            print(f'Book "{title}" not found.')

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nList of Books in Library:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book['title']} by {book['author']}")


def main():
    username = input("Enter your name: ")
    library = Library(username)
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display Books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == "2":
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")
if __name__ == "__main__":
    main()