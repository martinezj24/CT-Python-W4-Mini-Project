import os
from Books import Books, Library
from User import User, Actions
from Author import Author

# #Im visiualizing this project from the eyes of a manager/librarian in a library
# # assisting a customer at a register. Employees will be able to perfom various actions 
# # both on the admin level (inventory, customer handling, etc)
# # and for daily operations of returning/ checking out books


joshua = User('Joshua', '1234', '785674', borrowed_books=[])
john = User('John', '5678', '908984', borrowed_books=[])
sean = User('Sean', '0987', '467874', borrowed_books=[])

book1 = Books('More Than A Carpenter', 'Josh McDowell', 'Christian Lit.', '45678')
book2 = Books('The Case For Christ', 'Lee Strobel', 'Christian Lit.', '12230')
book3 = Books('Seeking Allah, FInding Jesus', 'Nabeel Qureshi', 'Christian Lit.', '46029')

McDowell = Author('Josh McDowell')
Qureshi = Author('Nabeel Qureshi')
Strobel = Author('Lee Strobel')

def main():
    library = Library() 
    user = User(joshua, john, sean)
    # actions = Actions()
    # author = Author(McDowell)
    # books = [book1, book2, book3]
    

    while True:
        action = input('''
        Welcome to the Library Management System!

        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit

        > ''')

        if action == '1':
            book_operations(library)
        elif action == '2':
            user_operations(user)
        elif action == '3':
            author_operations(Author)
        elif action == '4':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid Input. Try Again')

def book_operations(library):
    os.system('cls')  
    while True:
        print('Book Operations Menu:')
        try:
            action = input('''
            1.) Search Available Books in Library 
            2.) Display Full Library
            3.) Add Book or Remove Book
            4.) Back To Main Menu
            > ''')

            if action == '1': 
                search_criteria = input('How would you like to search? (Title, Author, or ISBN): ')
                if search_criteria.lower() in ['title', 'author', 'isbn']:
                    criteria = input(f"Enter the {search_criteria}: ")
                    library.search_book(criteria)
            elif action == '2': 
                library.display_all_books()
            elif action == '3': 
                inventory = input('Would you like to add or remove a book? Enter (add/remove): ')
                if inventory.lower() == 'add':
                    library.add_book()
                elif inventory.lower() == 'remove':
                    library.remove_book()
                else:
                    print('Invalid Entry. Try again!')    
            # elif action == '4': 
            #     book_title = input("Enter the title of the book you want to borrow: ")
            #     User.add_borrowed_book(book_title)
            # elif action == '5': 
            #     book_title = input("Enter the title of the book you want to return: ")
            #     User.remove_borrowed_book(book_title)
            elif action == '4': 
                break
            else:
                print("Invalid Input. Try Again!")
        except ValueError as ve:
            print(f"ValueError: {ve} has occurred")
        # except Exception as e:
        #     print(f"An error occurred: {e}")

        

def user_operations(User):
    os.system('cls')
    actions = Actions()
    while True:
        print('User Operations Menu:')
        try:
            action = input('''
            1.) Add New User
            2.) View User Details
            3.) Display All Users
            4.) User Book Checkout
            5.) User Book Return
            6.) Back To Main Menu
            
            > ''')
            if action == '1': # Add New User
                actions.add_new_user()
            elif action == '2': # View User Details
                name = input("Enter User's Name: ")
                actions.search_user(name=name)
            elif action == '3': # Display All
                actions.display_all_users()
            elif action == '4':
                actions.add_borrowed_book() #Need to fix
            elif action == '5':
                actions.remove_borrowed_book() #Need to fix
            elif action == '6': #Back to main()
                break
            else:
                print("Invalid Input. Try Again!")
        except ValueError as ve:
            print(f"ValueError: {ve} has occurred")
        except Exception as e: #Dylan/Travis proof
            print(f"An error occurred: {e}")

def author_operations(Author):
    os.system('cls')
    while True:
        print('Author Operations Menu:')
        try:
            action = input('''
            1.) Add New Author
            2.) View Author Details
            3.) Display All Authors
            4.) Back To Main Menu
            
            > ''')
            if action == '1': # Add New Author
                Author.add_author(Author)
            elif action == '2': # View Author Details
                Author.get_author_info(Author)
            elif action == '3': # Display All
                Author.display_all_authors(Author)
            elif action == '4': #Back to main()
                break
            else:
                print("Invalid Input. Try Again!")
        except ValueError as ve:
            print(f"ValueError: {ve} has occurred")
        # except Exception as e: #Dylan/Travis proof
        #     print(f"An error occurred: {e}")
    
main()