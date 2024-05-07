class Author:

    def __init__(self, name):
        self.name = name



    def get_author_info(self):
        try:
            print(f"Author Name: {self.name}")
            print("Books Written:")
            written_books = [book.title for book in Books.books if book.author == self.name]
            if written_books:
                for book in written_books:
                    print(f"- {book}")
            else:
                print("No books written by this author.")
        except Exception as e:
            print(f"An error occurred: {e}")




    def add_author(self):
        try:
            name = input("Enter author's name: ")
            new_author = Author(name)
            book_title = input("Enter a book they have written: ")
            Books.books.append(book_title)   # Append the book to the list of all books
            print(f"Added '{book_title}' to {new_author.name}'s collection of written books successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

            


    def display_all_authors(self):
        try:
            all_authors = sorted(set(book.author for book in Books.books)) #In alphabetical order
            if all_authors:
                print('All Authors (A-Z):')
                for author in all_authors:
                    print(f"- {author}")
            else:
                print('No authors found.')
        except Exception as e:
            print(f"An error occurred: {e}")
