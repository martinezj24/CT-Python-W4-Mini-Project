from Books import Library, Books
class User():
    

    def __init__(self, name=None, library_id=None,credit_card=None, borrowed_books=None):
        self.name = name
        self.library_id = library_id
        self.__credit_card = credit_card
        self.borrowed_books = borrowed_books or []      



    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Library ID: {self.library_id}")
        print(f"Currently Borrowed Books: {self.borrowed_books}")
        last_four_digits = self.__credit_card[-4:] # Extracting last 4 digits
        hidden_card = "*" * (len(self.__credit_card) - 4) + last_four_digits #Hiding all digits but last 4
        print(f"Current Card On File: {hidden_card}") 






class Actions():
    

    def __init__(self):
        self.users = []
        self.library = Library()



    def add_new_user(self):
        try:
            name = input("Enter User's Name: ")
            library_id = input("Enter User's Library ID #: ")
            credit_card = input('Enter Credit Card Number: ')
            new_user = User(name, library_id, credit_card)
            self.users.append(new_user)
            print('New User Added Successfully!')
        except Exception as e:
            print(f"An error occurred: {e}")




    def search_user(self, name=None, library_id=None):
        if not name and not library_id:
            print('Please provide a valid name or Library ID')
            return None

        found_user = None
        for user in self.users:
            if name and name.lower() in user.name.lower():
                found_user = user
                break
            elif library_id and library_id == user.library_id:
                found_user = user
                break

        return found_user



    def add_borrowed_book(self):
        try:
            search_option = input("Search user by name or library ID? (name/library ID): ").lower()
            found_user = None
            
            if search_option == "name":
                user_name = input("Enter the name of the user: ")
                found_user = self.search_user(name=user_name)
            elif search_option == "library id":
                user_library_id = input("Enter the library ID of the user: ")
                found_user = self.search_user(library_id=user_library_id)
            else:
                print("Invalid search option.")

            if found_user:
                book_title = input("Enter the title of the book you want to borrow: ")
                # Check if the book is available in the library
                if self.library.check_available_books(book_title):
                    print(f"Book '{book_title}' added to user '{found_user.name}' successfully!")
                else:
                    print(f"Book '{book_title}' is not available for borrowing.")
            else:
                print("User not found. Try again!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_borrowed_book(self):
        try:
            # Get user input for user's name, library ID, and book title to return
            search_option = input("Search user by name or library ID? (name/library ID): ").lower()
            found_user = None
            
            if search_option == "name":
                user_name = input("Enter the name of the user: ")
                found_user = self.search_user(name=user_name)
            elif search_option == "library id":
                user_library_id = input("Enter the library ID of the user: ")
                found_user = self.search_user(library_id=user_library_id)
            else:
                print("Invalid search option.")
            

            if not found_user and library_id:  # If user not found by name, search by library ID
                for user in self.users:
                    if user.library_id == library_id:
                        found_user = user
                        break

            if found_user:
                book_title = input("Enter the title of the book you want to return: ")
                if book_title in found_user.borrowed_books:
                    found_user.borrowed_books.remove(book_title)
                    print(f"Book '{book_title}' removed from user '{found_user.name}' successfully.")
                else:
                    print(f"Book '{book_title}' not found in user '{found_user.name}' borrowed books.")
            else:
                print("Please provide a valid name or Library ID.")
        except ValueError as ve:
            print(f"ValueError: {ve} has occurred")


    def display_all_users(self):
        if not self.users:
            print("No users in the system.")
        else:
            print("All Users:")
            for user in self.users:
                user.get_info()  
                print("--------------------")