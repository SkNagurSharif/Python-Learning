from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from library import Library

# Create library

from gold_member import GoldMember
from library_item import LibraryItem
from staff import Staff
from student import Student
from ReservationSystem import Reservation

root = tk.Tk()

# [All class definitions: User, Student, Staff, GoldMember, LibraryItem, Reservation, Library]

library = Library()



# Function to add a book
def add_book():
    title = book_title_entry.get()
    author = book_author_entry.get()
    book_id = book_id_entry.get()
    book = LibraryItem(title, author, book_id)
    library.add_item(book)
    update_books_list()
    messagebox.showinfo("Success", f"Added book: {title}")
    
# Update the add user function to accommodate user type selection
def add_user():
    user_id = user_id_entry.get()
    name = user_name_entry.get()
    user_type = user_type_var.get()
    if user_type == "Student":
        library.add_user(Student(user_id, name))
    elif user_type == "Staff":
        library.add_user(Staff(user_id, name, "Librarian", "Library"))  # Assuming defaults for this example
    elif user_type == "GoldMember":
        library.add_user(GoldMember(user_id, name))
    update_users_list()
    messagebox.showinfo("Success", f"Added {user_type}: {name}")

def update_books_list():
    books.delete(0, tk.END)
    for item in library.items:
        books.insert(tk.END, item.title)

def update_users_list():
    users_listbox.delete(0, tk.END)
    for user in library.users:
        users_listbox.insert(tk.END, user.name)

def borrow_book():
    user_name = users_listbox.get(users_listbox.curselection())
    book_title = books.get(books.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    book = next((b for b in library.items if b.title == book_title), None)
    if user and book:
        user.borrow_item(book)
        update_books_list()
        messagebox.showinfo("Success", f"{user_name} borrowed {book_title}")

def return_book():
    user_name = users_listbox.get(users_listbox.curselection())
    book_title = books.get(books.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    book = next((b for b in library.items if b.title == book_title), None)
    if user and book:
        user.return_item(book)
        update_books_list()
        messagebox.showinfo("Success", f"{user_name} returned {book_title}")
        
# Functions for UI actions
# [Previous functions remain unchanged]

def reserve_book():
    user_name = users_listbox.get(users_listbox.curselection())
    book_title = books.get(books.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    book = next((b for b in library.items if b.title == book_title), None)
    if user and book:
        reservation = Reservation(user, book)
        library.reservations.append(reservation)
        messagebox.showinfo("Success", f"{user_name} reserved {book_title}")

def pay_fines():
    user_name = users_listbox.get(users_listbox.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    if user:
        user.pay_fine(user.fines) # Paying all the fines for simplicity.
        update_user_details(user)
        messagebox.showinfo("Success", f"{user_name}'s fines have been cleared.")

def update_user_details(user):
    borrowed_books.delete(0, tk.END)
    for item in user.borrowed_items:
        borrowed_books.insert(tk.END, item.title)
    user_fines_var.set(f"Fines: ${user.fines:.2f}")       

def renew_membership():
    user_name = users_listbox.get(users_listbox.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    if user:
        user.membership_end_date = datetime.now() + timedelta(days=365)
        messagebox.showinfo("Success", f"{user_name}'s membership has been renewed!")

def search_books():
    query = simpledialog.askstring("Search", "Enter book title:")
    results = library.search_by_title(query)
    books.delete(0, tk.END)
    for item in results:
        books.insert(tk.END, item.title)

def check_overdue_books(user):
    overdue_books = [item for item in user.borrowed_items if item.days_borrowed() > 14]
    for book in overdue_books:
        user.fines += book.calculate_fine()

# Modified function to include checking overdue books
def select_user(event):
    user_name = users_listbox.get(users_listbox.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    if user:
        check_overdue_books(user)
        update_user_details(user)
        
        
def view_reservation_queue():
    book_title = books.get(books.curselection())
    book = next((b for b in library.items if b.title == book_title), None)
    if book:
        queue_window = tk.Toplevel(root)
        queue_window.title(f"Reservation Queue for {book_title}")
        
        queue_listbox = tk.Listbox(queue_window)
        for reservation in library.reservations:
            if reservation.item == book:
                queue_listbox.insert(tk.END, reservation.user.name)
        queue_listbox.grid(row=0, column=0)
        
def view_detailed_user_info():
    user_name = users_listbox.get(users_listbox.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    if user:
        detail_window = tk.Toplevel(root)
        detail_window.title(f"Details for {user_name}")
        
        tk.Label(detail_window, text=f"Name: {user.name}").grid(row=0, column=0)
        tk.Label(detail_window, text=f"User ID: {user.user_id}").grid(row=1, column=0)
        tk.Label(detail_window, text=f"Membership Expires: {user.membership_end_date.date()}").grid(row=2, column=0)
        
        tk.Label(detail_window, text="Borrow History:").grid(row=3, column=0)
        borrow_listbox = tk.Listbox(detail_window)
        for item, action, date in user.history:
            borrow_listbox.insert(tk.END, f"{action} {item.title} on {date.date()}")
        borrow_listbox.grid(row=4, column=0)
           
    user_type = "User"
    if isinstance(user, Student):
        user_type = "Student"
    elif isinstance(user, Staff):
        user_type = "Staff"
    elif isinstance(user, GoldMember):
        user_type = "GoldMember"

    tk.Label(detail_window, text=f"Type: {user_type}").grid(row=3, column=0)

def edit_user():
    user_name = users_listbox.get(users_listbox.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    
    if user:
        edit_window = tk.Toplevel(root)
        edit_window.title(f"Edit {user_name}")
        
        tk.Label(edit_window, text="Name:").grid(row=0, column=0)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, user.name)
        name_entry.grid(row=0, column=1)
        
        tk.Button(edit_window, text="Save", command=lambda: save_user_changes(user, name_entry.get())).grid(row=1, column=1)

def save_user_changes(user, new_name):
    user.name = new_name
    update_users_list()
    messagebox.showinfo("Success", f"Updated user name to {new_name}")
    


def extend_loan_period():
    user_name = users_listbox.get(users_listbox.curselection())
    book_title = borrowed_books.get(borrowed_books.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    book = next((b for b in library.items if b.title == book_title), None)
    if user and book and book in user.borrowed_items:
        book.loan_end_date += timedelta(days=14)  # extend by 14 days
        messagebox.showinfo("Success", f"Extended loan period for {book_title} by 14 days.")

def sort_users():
    library.users.sort(key=lambda x: x.name)
    update_users_list()

def sort_books():
    library.items.sort(key=lambda x: x.title)
    update_books_list()
    
def advanced_search():
    query = search_entry.get()
    criteria = search_criteria_var.get()
    results = []
    
    if criteria == "Title":
        results = library.search_by_title(query)
    elif criteria == "Author":
        results = [book for book in library.items if query.lower() in book.author.lower()]
    elif criteria == "ID":
        results = [book for book in library.items if book.item_id == query]
    
    books.delete(0, tk.END)
    for item in results:
        books.insert(tk.END, item.title)

def view_book_details():
    book_title = books.get(books.curselection())
    book = next((b for b in library.items if b.title == book_title), None)
    if book:
        detail_window = tk.Toplevel(root)
        detail_window.title(f"Details for {book_title}")
        
        tk.Label(detail_window, text=f"Title: {book.title}").grid(row=0, column=0)
        tk.Label(detail_window, text=f"Author: {book.author}").grid(row=1, column=0)
        tk.Label(detail_window, text=f"ID: {book.item_id}").grid(row=2, column=0)
        tk.Label(detail_window, text=f"Available: {'Yes' if book.is_available() else 'No'}").grid(row=3, column=0)

def mock_backup_data():
    # In a real application, this would involve saving data to external storage
    messagebox.showinfo("Backup", "Mock backup completed!")
    
def sort_users_books():
    library.items.sort(key=lambda x: x.title)
    library.users.sort(key=lambda x: x.name)
    update_books_list()
    update_users_list()
    

def delete_selected_user():
    user_name = users_listbox.get(users_listbox.curselection())
    user = next((u for u in library.users if u.name == user_name), None)
    if user:
        library.users.remove(user)
        update_users_list()

def delete_selected_book():
    book_title = books_listbox.get(books_listbox.curselection())
    book = next((b for b in library.items if b.title == book_title), None)
    if book:
        library.items.remove(book)
        update_books_list()


# Main tkinter window
root = tk.Tk()
root.title("Library Management System")

# Create and place labels, entries, and buttons on the window
tk.Label(root, text="Library Management System", font=('Arial', 16)).grid(row=0, column=1)

'''
# Add book section
tk.Label(root, text="Add Book:").grid(row=1, column=0)

book_title_entry = tk.Entry(root)
book_title_entry.grid(row=1, column=1)
tk.Label(root, text="Title").grid(row=2, column=1)

book_author_entry = tk.Entry(root)
book_author_entry.grid(row=1, column=2)
tk.Label(root, text="Author").grid(row=2, column=2)

book_id_entry = tk.Entry(root)
book_id_entry.grid(row=1, column=3)
tk.Label(root, text="Book ID").grid(row=2, column=3)

tk.Button(root, text="Add Book", command=add_book).grid(row=1, column=4)
'''

# [You can expand this UI by adding sections for Users, Borrowing/Returning Books, Reservations, etc.]

# Adding a Book
tk.Label(root, text="Book Details").grid(row=0, column=0, sticky=tk.W)
tk.Label(root, text="Title:").grid(row=1, column=0)
book_title_entry = tk.Entry(root)
book_title_entry.grid(row=1, column=1)
tk.Label(root, text="Author:").grid(row=2, column=0)
book_author_entry = tk.Entry(root)
book_author_entry.grid(row=2, column=1)
tk.Label(root, text="ID:").grid(row=3, column=0)
book_id_entry = tk.Entry(root)
book_id_entry.grid(row=3, column=1)
tk.Button(root, text="Add Book", command=add_book).grid(row=4, column=1)

# Adding a User
tk.Label(root, text="User Details").grid(row=0, column=2, sticky=tk.W)
tk.Label(root, text="Name:").grid(row=1, column=2)
user_name_entry = tk.Entry(root)
user_name_entry.grid(row=1, column=3)
tk.Label(root, text="ID:").grid(row=2, column=2)
user_id_entry = tk.Entry(root)
user_id_entry.grid(row=2, column=3)
user_type_var = tk.StringVar(root)
user_type_var.set("Student")  # default value
user_type_dropdown = tk.OptionMenu(root, user_type_var, "Student", "Staff", "GoldMember")
user_type_dropdown.grid(row=3, column=3)
tk.Button(root, text="Add User", command=add_user).grid(row=4, column=3)

# List of books and users
books = tk.Listbox(root)
books.grid(row=5, column=0, rowspan=4, columnspan=2)
users_listbox = tk.Listbox(root)
users_listbox.grid(row=5, column=2, rowspan=4, columnspan=2)

# Actions for Borrow, Return, Reserve, and Searching Books
tk.Button(root, text="Borrow", command=borrow_book).grid(row=9, column=0)
tk.Button(root, text="Return", command=return_book).grid(row=9, column=1)
tk.Button(root, text="Reserve", command=reserve_book).grid(row=9, column=2)
tk.Button(root, text="Search Books", command=search_books).grid(row=9, column=3)

# Detailed Info for Books and Users
tk.Button(root, text="Book Details", command=view_book_details).grid(row=10, column=0)
tk.Button(root, text="User Details", command=view_detailed_user_info).grid(row=10, column=1)

# Additional Features
tk.Button(root, text="Renew Membership", command=renew_membership).grid(row=10, column=2)
tk.Button(root, text="Backup Data", command=mock_backup_data).grid(row=10, column=3)


notebook = ttk.Notebook(root)

# Create frames for each tab
book_tab = ttk.Frame(notebook)
user_tab = ttk.Frame(notebook)
actions_tab = ttk.Frame(notebook)
details_tab = ttk.Frame(notebook)

# Add tabs to the notebook
notebook.add(book_tab, text="Books")
notebook.add(user_tab, text="Users")
notebook.add(actions_tab, text="Actions")
notebook.add(details_tab, text="Details")

notebook.pack(expand=True, fill="both")

# Books Tab
tk.Label(book_tab, text="Title:").grid(row=0, column=0)
book_title_entry = tk.Entry(book_tab)
book_title_entry.grid(row=0, column=1)
tk.Label(book_tab, text="Author:").grid(row=1, column=0)
book_author_entry = tk.Entry(book_tab)
book_author_entry.grid(row=1, column=1)
tk.Label(book_tab, text="ID:").grid(row=2, column=0)
book_id_entry = tk.Entry(book_tab)
book_id_entry.grid(row=2, column=1)
tk.Button(book_tab, text="Add Book", command=add_book).grid(row=3, column=0, columnspan=2)

# Users Tab
tk.Label(user_tab, text="Name:").grid(row=0, column=0)
user_name_entry = tk.Entry(user_tab)
user_name_entry.grid(row=0, column=1)
tk.Label(user_tab, text="ID:").grid(row=1, column=0)
user_id_entry = tk.Entry(user_tab)
user_id_entry.grid(row=1, column=1)
user_type_var = tk.StringVar(user_tab, value="Student")
user_type_dropdown = ttk.Combobox(user_tab, textvariable=user_type_var, values=["Student", "Staff", "GoldMember"])
user_type_dropdown.grid(row=2, column=1)
tk.Label(user_tab, text="Type:").grid(row=2, column=0)
tk.Button(user_tab, text="Add User", command=add_user).grid(row=3, column=0, columnspan=2)

# Actions Tab
books_listbox = tk.Listbox(actions_tab)
books_listbox.grid(row=0, column=0, rowspan=3)
users_listbox = tk.Listbox(actions_tab)
users_listbox.grid(row=0, column=1, rowspan=3)
tk.Button(actions_tab, text="Borrow", command=borrow_book).grid(row=3, column=0)
tk.Button(actions_tab, text="Return", command=return_book).grid(row=3, column=1)
tk.Button(actions_tab, text="Reserve", command=reserve_book).grid(row=4, column=0)
tk.Button(actions_tab, text="Search Books", command=search_books).grid(row=4, column=1)

# Details Tab
tk.Button(details_tab, text="Book Details", command=view_book_details).grid(row=0, column=0)
tk.Button(details_tab, text="User Details", command=view_detailed_user_info).grid(row=0, column=1)
tk.Button(details_tab, text="Sort Users & Books", command=sort_users_books).grid(row=1, column=0)
tk.Button(details_tab, text="Backup Data", command=mock_backup_data).grid(row=1, column=1)

# Search Entries for Books and Users on the Actions Tab
search_books_entry = tk.Entry(actions_tab)
search_books_entry.grid(row=3, column=2)
tk.Button(actions_tab, text="Search Books", command=lambda: search_books(search_books_entry.get())).grid(row=4, column=2)
search_users_entry = tk.Entry(actions_tab)
search_users_entry.grid(row=3, column=3)
tk.Button(actions_tab, text="Search Users", command=lambda: search_users(search_users_entry.get())).grid(row=4, column=3)

# Delete & Edit Buttons on the Details Tab
tk.Button(details_tab, text="Delete User", command=delete_selected_user).grid(row=1, column=2)
tk.Button(details_tab, text="Delete Book", command=delete_selected_book).grid(row=1, column=3)
tk.Button(details_tab, text="Edit User", command=edit_user).grid(row=2, column=2)
tk.Button(details_tab, text="Edit Book", command=edit_book).grid(row=2, column=3)

# Advanced Search on a new Tab
advanced_search_tab = ttk.Frame(notebook)
notebook.add(advanced_search_tab, text="Advanced Search")
notebook.pack(expand=True, fill="both")

tk.Label(advanced_search_tab, text="Advanced Search:").grid(row=0, column=0)
search_entry = tk.Entry(advanced_search_tab)
search_entry.grid(row=0, column=1)
search_criteria_var = tk.StringVar(advanced_search_tab)
search_criteria_var.set("Title")  # default value
search_criteria_dropdown = ttk.Combobox(advanced_search_tab, textvariable=search_criteria_var, values=["Title", "Author", "ID"])
search_criteria_dropdown.grid(row=0, column=2)
tk.Button(advanced_search_tab, text="Search", command=advanced_search).grid(row=0, column=3)

# Extend Loan Period & User Details on the Actions Tab
tk.Button(actions_tab, text="Extend Loan", command=extend_loan_period).grid(row=5, column=0)
tk.Button(actions_tab, text="Update User Details", command=update_user_details).grid(row=5, column=1)

# Initial population
update_books_list()
update_users_list()

root.mainloop()
