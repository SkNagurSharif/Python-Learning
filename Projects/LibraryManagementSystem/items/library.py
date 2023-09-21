from items.ReservationSystem import Reservation


class Library:
    def __init__(self):
        self.items = []
        self.users = []
        self.reservations = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def search_by_title(self, title):
        return [item for item in self.items if title.lower() in item.title.lower()]

    def filter_by_availability(self):
        return [item for item in self.items if not item.on_loan]

    def make_reservation(self, user, item):
        if not item.on_loan:
            print(f"{item.title} is available. No need to reserve.")
        else:
            reservation = Reservation(user, item)
            self.reservations.append(reservation)
            print(f"Reservation made for {user.name} for {item.title}.")

    def fulfill_reservations(self):
        for reservation in self.reservations:
            reservation.fulfill_reservation()
            if not reservation.item.on_loan:
                self.reservations.remove(reservation)

    def check_overdue_items(self):
        overdue_items = []
        for item in self.items:
            if item.on_loan and item.days_borrowed() > 14:
                overdue_items.append(item)
        return overdue_items

    def charge_fines_for_overdue(self):
        overdue_items = self.check_overdue_items()
        for item in overdue_items:
            borrower = item.borrow_history[-1][0]
            fine = item.calculate_fine()
            borrower.fines += fine
            print(f"Charged ${fine} fine to {borrower.name} for {item.title}.")

    def display_all_items(self):
        for item in self.items:
            print(f"Title: {item.title}, Author/Artist: {item.author_artist}, On Loan: {item.on_loan}")

    def display_all_users(self):
        for user in self.users:
            print(f"User ID: {user.user_id}, Name: {user.name}, Fines Due: ${user.fines}")
    
    def search_by_author(self, author):
        return [item for item in self.items if author.lower() in item.author_artist.lower()]

    def recommend_items(self, user):
        # A simple recommendation based on average ratings
        rated_items = [item for item in self.items if item.average_rating() is not None]
        rated_items.sort(key=lambda x: x.average_rating(), reverse=True)
        top_5 = rated_items[:5]
        return top_5
    
    def renew_item(self, user, item):
        # Check if item is not reserved by someone else before renewing
        reservations_for_item = [r for r in self.reservations if r.item == item]
        if reservations_for_item:
            print("Cannot renew. Item is reserved by another user.")
            return
        user.borrow_item(item)  # Simplistic way to renew by borrowing again
        print(f"{item.title} has been renewed by {user.name}.")

        """
        The "Library class" will be responsible for managing the entire collection of items, users, and other library operations.
        
        In this enhanced Library class:

            Management of Items and Users: The library can add or remove items and users.

            Searching and Filtering: It can search items by title and filter them by availability.

            Reservations: Users can reserve items that are on loan. The library tries to fulfill these reservations when items are returned.

            Overdue Management: The library can check for overdue items and impose fines on borrowers.

            Display Information: Methods to display all items and all users are included for easy overview.
        
        """
