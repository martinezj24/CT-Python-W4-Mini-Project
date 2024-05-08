from Books import Books, Library 
class AuthorActions:
    def __init__(self):
        self.authors_books = {}  # Dictionary to store authors and their books

    def add_author(self):
        try:
            author_name = input("Enter author's name: ")
            book_title = input("Enter a book they have written: ")
            if author_name in self.authors_books:
                self.authors_books[author_name].append(book_title)
            else:
                self.authors_books[author_name] = [book_title]
            print(f"Added '{book_title}' to {author_name}'s collection of written books successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_author_info(self):
        try:
            author_name = input("Enter author's name to view their books: ")
            if author_name in self.authors_books:
                print(f"{author_name}'s Books:")
                for book in self.authors_books[author_name]:
                    print(f"- {book}")
            else:
                print("Author not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_all_authors(self):
        if self.authors_books:
            print('All Authors:')
            for author, books in self.authors_books.items():
                print(f"{author}: {', '.join(books)}")
                print('--------------------------')
        else:
            print('No authors found.')


