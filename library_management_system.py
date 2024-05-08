import os
from Books import Books, Library
from User import User, Actions
from Author import AuthorActions



def main():
    library = Library()
    author_actions = AuthorActions()
    

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
            user_operations(User)
        elif action == '3':
            author_operations(author_actions)  
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
            elif action == '4': 
                break
            else:
                print("Invalid Input. Try Again!")
        except ValueError as ve:
            print(f"ValueError: {ve} has occurred")
        except Exception as e:
            print(f"An error occurred: {e}")

        

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
                    # Get user's name
                name = input("Enter User's Name: ")
                # Search for the user
                found_user = actions.search_user(name=name)
                if found_user:
                    found_user.get_info()
            elif action == '3': # Display All
                actions.display_all_users()
            elif action == '4':
                actions.add_borrowed_book()
            elif action == '5':
                actions.remove_borrowed_book() 
            elif action == '6': #Back to main()
                break
            else:
                print("Invalid Input. Try Again!")
        except ValueError as ve:
            print(f"ValueError: {ve} has occurred")
        except Exception as e: #Dylan/Travis proof
            print(f"An error occurred: {e}")


def author_operations(author_actions):
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
            if action == '1':  
                author_actions.add_author()
            elif action == '2':  
                author_actions.display_author_info()
            elif action == '3':  
                author_actions.display_all_authors()
            elif action == '4':  
                break
            else:
                print("Invalid Input. Try Again!")
        except ValueError as ve:
            print(f"ValueError: {ve} has occurred")
        except Exception as e: #Dylan/Travis proof
            print(f"An error occurred: {e}")


main()