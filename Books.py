class Books():


    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn

    

    def get_info(self):
        availability = 'Available' if self.is_available else 'Not Available'
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nAvailability: {availability}"
 

    


    


class Library():

    def __init__(self):
        self.library = []
        self.is_available = True




    def search_book(self, find_book):  
        found = False
        for book in self.library:
            if (find_book.lower() in book.title.lower() or 
            find_book.lower() in book.author.lower() or 
            find_book.lower() == book.isbn.lower()):
                print(book.get_info())
                found = True
        if not found:
            print("This book is not in our library.")
            add_book = input("Would you like to add it? Please enter (y/n): ")
            if add_book.lower() == 'y':
                self.add_book()
            else:
                print("Returning to Main Menu...")



    def add_book(self):
        try:
            title = input('Title: ') #Pass in book object into method
            author = input('Author: ')
            genre = input('Genre: ')
            isbn = input('ISBN: ')
            new_book = Books(title, author, genre, isbn)  # Provide the required arguments
            self.library.append(new_book)
            print('New Book Added!')
        except Exception as e:
            print(f"An error occurred: {e}")
    


    def remove_book(self): #Removal Options included for more versatile removal method
        try:
            removal_option = input("How would you like to remove the book? (ISBN, Title, Author): ").lower()
            if removal_option == "isbn":
                isbn = input('Enter the ISBN of the book you want to remove: ')
                found_book = None
                for book in self.library:
                    if book.isbn == isbn:
                        found_book = book
                        break
                if found_book:
                    self.library.remove(found_book)
                    print('Book removed successfully.')
                else:
                    print('The book with the provided ISBN is not in the library.')
            elif removal_option == "title":
                title = input('Enter the title of the book you want to remove: ')
                removed_books = [book for book in self.library if book.title == title]
                if removed_books:
                    for book in removed_books:
                        self.library.remove(book)
                    print('Books removed successfully.')
                else:
                    print('No books with the provided title are in the library.')
            elif removal_option == "author":
                author = input('Enter the author of the book you want to remove: ')
                removed_books = [book for book in self.library if book.author == author]
                if removed_books:
                    for book in removed_books:
                        self.library.remove(book)
                    print('Books removed successfully.')
                else:
                    print('No books by the provided author are in the library.')
            else:
                print('Invalid removal option. Please choose ISBN, Title, or Author.')
        except Exception as e: #Dylan/Travis proof
            print(f"An error occurred: {e}")



    def display_all_books(self):
        try:
            if not self.library:
                print('The Library is Currently Empty')
            else:
                print('All Books in the Library:')
                for idx, book in enumerate(self.library, start=1):
                    print(f'{idx}.) {book.get_info()}')  
                    print('--------------------')  # For readability between books
        except Exception as e: #Dylan/Travis proof
            print(f"An error occurred: {e}")


    def available_books(self, is_available):
        self.is_available = is_available


    def check_available_books(self, title):
        for book in self.library:
            if book.title == title and book.is_available:
                return True
        return False


    #  I tried to add sorting the books by alphbetical order but it proved to be too
    #  complicated at this time. Definitely something I would like to figure
    #  out in the future!