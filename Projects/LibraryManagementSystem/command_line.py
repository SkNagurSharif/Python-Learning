from datetime import datetime, timedelta


from items.gold_member import GoldMember
from items.library import Library
from items.library_item import LibraryItem
from items.staff import Staff

from items.student import Student

# [Include all the classes: User, Student, Staff, GoldMember, LibraryItem, Reservation, and Library]

def main_menu():
    print("\n--- Library Management System ---")
    print("1. Add User")
    print("2. Add Item")
    print("3. Borrow Item")
    print("4. Return Item")
    print("5. Display all Users")
    print("6. Display all Items")
    print("7. Reserve Item")
    print("8. Fulfill Reservations")
    print("9. Search for an Item by Title")
    print("10. Check and Charge Fines")
    print("11. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_user_interface(lib):
    print("1. Student")
    print("2. Staff")
    print("3. Gold Member")
    user_type = input("Enter user type: ")
    user_id = input("Enter user ID: ")
    name = input("Enter name: ")

    if user_type == "1":
        grade_level = input("Enter grade level: ")
        major = input("Enter major: ")
        advisor = input("Enter advisor name: ")
        user = Student(user_id, name, grade_level, major, advisor)
    elif user_type == "2":
        job_title = input("Enter job title: ")
        department = input("Enter department: ")
        user = Staff(user_id, name, job_title, department)
    elif user_type == "3":
        user = GoldMember(user_id, name)
    else:
        print("Invalid choice!")
        return

    lib.add_user(user)
    print(f"User {name} added successfully!")

def add_item_interface(lib):
    title = input("Enter item title: ")
    author_artist = input("Enter author/artist: ")
    item_id = input("Enter item ID: ")
    item = LibraryItem(title, author_artist, item_id)
    lib.add_item(item)
    print(f"Item {title} added successfully!")

def borrow_item_interface(lib):
    user_id = input("Enter user ID: ")
    item_id = input("Enter item ID: ")

    user = lib.get_user_by_id(user_id)
    item = lib.get_item_by_id(item_id)

    if user and item:
        user.borrow_item(item)
    else:
        print("User or Item not found!")

def return_item_interface(lib):
    user_id = input("Enter user ID: ")
    item_id = input("Enter item ID: ")

    user = lib.get_user_by_id(user_id)
    item = lib.get_item_by_id(item_id)

    if user and item:
        user.return_item(item)
    else:
        print("User or Item not found!")

def display_users_interface(lib):
    lib.display_all_users()

def display_items_interface(lib):
    lib.display_all_items()

# ... [Include all the class definitions: User, Student, Staff, GoldMember, LibraryItem, Reservation, and Library]



# ... [Other interface functions like add_user_interface, add_item_interface, etc.]

def reserve_item_interface(lib):
    user_id = input("Enter user ID: ")
    item_id = input("Enter item ID to reserve: ")

    user = lib.get_user_by_id(user_id)
    item = lib.get_item_by_id(item_id)

    if user and item:
        lib.make_reservation(user, item)
    else:
        print("User or Item not found!")

def fulfill_reservations_interface(lib):
    lib.fulfill_reservations()
    print("Attempted to fulfill reservations!")

def search_item_interface(lib):
    title = input("Enter the title (or part of the title) to search: ")
    results = lib.search_by_title(title)
    if results:
        for item in results:
            print(f"Title: {item.title}, Author/Artist: {item.author_artist}, On Loan: {item.on_loan}")
    else:
        print("No matching items found.")

def check_charge_fines_interface(lib):
    lib.charge_fines_for_overdue()
    print("Charged fines for overdue items.")
    
def authenticate_user_interface(lib):
    user_id = input("Enter user ID: ")
    password = input("Enter password: ")

    user = lib.get_user_by_id(user_id)
    if not user:
        print("User not found!")
        return None
    if user.authenticate(password):
        print(f"Welcome, {user.name}!")
        return user
    else:
        print("Wrong password!")
        return None

def search_by_author_interface(lib):
    author = input("Enter author's name to search: ")
    results = lib.search_by_author(author)
    for item in results:
        print(item.title)

def feedback_interface(lib, user):
    item_id = input("Enter the item ID for which you want to provide feedback: ")
    item = lib.get_item_by_id(item_id)
    
    if not item:
        print("Item not found!")
        return

    if user in [history[0] for history in item.borrow_history]:  # Check if the user has borrowed this item before
        rating = int(input("Rate the item (1-5): "))
        comment = input("Any comments? ")
        item.add_feedback(user, rating, comment)
        print("Thank you for your feedback!")
    else:
        print("Feedback can only be provided for items you have borrowed.")


def recommend_interface(lib, user):
    recommendations = lib.recommend_items(user)
    print("Recommended items for you:")
    for item in recommendations:
        print(item.title)

def renew_item_interface(lib, user):
    item_id = input("Enter item ID to renew: ")
    item = lib.get_item_by_id(item_id)
    if item:
        lib.renew_item(user, item)

def main():
    lib = Library()
    current_user = None  # The user currently using the system

    while True:
        choice = main_menu()
        if choice in ["3", "4", "7", "10"]:  # Actions that require user authentication
            current_user = authenticate_user_interface(lib)
            if not current_user:
                continue

        if choice == "1":
            add_user_interface(lib)
        elif choice == "2":
            add_item_interface(lib)
        elif choice == "3":
            borrow_item_interface(lib)
        elif choice == "4":
            return_item_interface(lib)
        elif choice == "5":
            display_users_interface(lib)
        elif choice == "6":
            display_items_interface(lib)
        elif choice == "7":
            reserve_item_interface(lib)
        elif choice == "8":
            fulfill_reservations_interface(lib)
        elif choice == "9":
            search_item_interface(lib)
        elif choice == "10":
            feedback_interface(lib, current_user)
        elif choice == "11":
            search_by_author_interface(lib)
        elif choice == "12":
            recommend_interface(lib, current_user)
        elif choice == "13":
            renew_item_interface(lib, current_user)
        elif choice == "14":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
