from datetime import datetime, timedelta


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []
        self.history = []
        self.fines = 0.0
        self.membership_end_date = datetime.now() + timedelta(days=365)  # 1-year membership by default
        self.status = "active"  # can also be "suspended" or "expired"

    def borrow_item(self, item):
        if not item.on_loan and self.can_borrow():
            item.on_loan = True
            self.borrowed_items.append(item)
            self.history.append((item, "borrowed", datetime.now()))
            item.borrow_history.append((self, datetime.now()))
            print(f"{self.name} has borrowed {item.title}.")
        else:
            print(f"{self.name} cannot borrow {item.title} at this time.")

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            item.on_loan = False
            self.history.append((item, "returned", datetime.now()))
            print(f"{self.name} has returned {item.title}.")
        else:
            print(f"{self.name} did not borrow {item.title}.")

    def pay_fine(self, amount):
        if amount > self.fines:
            print("Paid more than the fine amount.")
            return
        self.fines -= amount
        print(f"{self.name} has paid a fine of ${amount}. Remaining fine: ${self.fines}")

    def can_borrow(self):
        # By default, a user can borrow up to 5 items. This method can be overridden in subclasses.
        return len(self.borrowed_items) < 5

    def check_membership_status(self):
        if datetime.now() > self.membership_end_date:
            self.status = "expired"
        return self.status

    def set_password(self, password):
        # For simplicity, we're not hashing passwords here, but you should in a real-world application.
        self.password = password

    def authenticate(self, password_attempt):
        return password_attempt == self.password    
        
        """
        Certainly! The `User` class represents patrons of the library. Let's enhance it by incorporating a more sophisticated design to cater to a broader range of user-related features.

### Enhanced User Class:

#### Features:

1. **History**: Maintain a history of items borrowed by the user.
2. **User Roles and Privileges**: Different roles (e.g., Staff, Student, Gold Member) have different borrowing privileges.
3. **Limit on Borrowed Items**: Users can borrow only a certain number of items at a time.
4. **Membership Duration**: Users might have an expiration date for their library membership.
5. **Account Status**: Account can be active, suspended, or expired.

#### Implementation:

**Base `User` Class**:


**Derived Classes**:

Here, different roles of users are represented by subclasses:
student, staff, gold member

### Summary:

With this enhanced `User` class:

1. **User Behavior** is tracked via a history, allowing the library system to get insights into borrowing patterns and frequent users.
2. **Different User Roles** enable flexibility in assigning borrowing privileges.
3. **Account Management** is improved with statuses that can assist in system operations, such as sending reminders to renew membership or clearing expired accounts.
4. **Fine Management** ensures that users are held accountable for late returns, potentially improving the return rate of borrowed items.

This robust user management setup makes the library system more adaptable and accommodating to various user needs and scenarios.
        """
